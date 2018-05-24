import sklearn
import csv

from krvjezivot.constants import *
import pandas as pd
from krvjezivot.model_generator import ucitaj_model, ucitaj_dataset, predobradi_dataset
from krvjezivot.constants import BLOOD_GROUP_MAP as BGMP


def clean2group(data):
    groups = data.groupby('blood_group')
    return groups


class Solution:
    # TODO podesiti!
    ODZIV = 0.12
    # TODO postotak koji odreduje kada treba zahtjevati nove zalihe
    DELTA_THRESHOLD = 0.1
    FEMALE_LIMIT = 120
    MALE_LIMIT = 90

    def __init__(self, model_file, o_min, o_max, o_z, p, dataset):
        self.o_min = o_min
        self.o_max = o_max
        self.o_z = o_z
        self.p = p

        self.model = ucitaj_model(model_file)
        self.original_df = dataset
        self.original_df = self.original_df.drop(self.original_df.columns[0], axis=1)
        # self.original_df = self.original_df.rename({'Unnamed: 0': 'id'}, axis='columns')
        # self.scaler = sklearn.preprocessing.StandardScaler()
        self.used_ids = set()

    @property
    def r(self):
        return self.o_max - self.o_min

    def _calculate_delta(self, supply):
        delta = supply - self.o_z
        where = np.abs(delta) > Solution.DELTA_THRESHOLD * self.r
        delta = delta * where
        return delta

    def _clean_dataset(self, days_passed):
        cleaned = self.original_df.copy(deep=True)
        to_drop = []
        for index, row in cleaned.iterrows():
            if row.sex == 'Z' and row.last_donation + days_passed < self.FEMALE_LIMIT or row.sex == 'M' and row.last_donation + days_passed < self.MALE_LIMIT or row.id in self.used_ids:
                to_drop.append(index)
        cleaned = cleaned.drop(to_drop)
        return cleaned

    def pozovi_donore(self, supply: np.ndarray, days_passed):
        delta = self._calculate_delta(supply)
        cleaned_data = self._clean_dataset(days_passed)
        features = ['frequency', 'last_donation', 'blood_group', 'sex', 'distance']

        total_donor_indices = set()
        for gf in PRIORITY_GF_LIST:
            delta_i = BLOOD_GROUP_MAP[gf]
            available = cleaned_data.copy(deep=True)
            to_drop = []
            for index, row in available.iterrows():
                if not row.blood_group in GROUP_FACTOR_PRIMA[gf]:
                    to_drop.append(index)
            available = available.drop(to_drop)
            features = [x for x in available.columns if x in features]
            can_receive_obradeni = predobradi_dataset(available[features], drop=False)
            pred = self.model.predict_proba(can_receive_obradeni)
            how_many_to_call = int(delta[delta_i] / self.ODZIV)
            if how_many_to_call != 0:
                top = pred.argsort(axis=0)[how_many_to_call:][::-1]
                top_indices = top[:, 0]

                ids = set(available.iloc[top_indices].index)
                total_donor_indices = total_donor_indices | set(available.iloc[top_indices].id)
                # self.used_ids = self.used_ids | total_donor_indices
                cleaned_data = cleaned_data.drop(ids)
        return total_donor_indices


if __name__ == '__main__':
    dataset = ucitaj_dataset('dataset.csv')

    s = Solution('model', O_MIN, O_MAX, O_Z, P, dataset)

    while True:
        # days_passed = 0
        # supply = '50,130,60,150,50,30,8,20'
        days_passed = int(input(f'unesi days passed:'))
        supply = input(f'unesi supply:').strip()
        supply = np.array(list(map(int, supply.split(','))))
        ids_to_call = s.pozovi_donore(supply, days_passed)
        ids_to_call_csv = ','.join(map(str, ids_to_call))
        ids_to_call = list(ids_to_call)
        print(ids_to_call)
        with open(f'/home/david/Downloads/output_{days_passed}days.csv', 'w') as myfile:
            myfile.write(ids_to_call_csv)

        odziv_donora = input(f'unesi one koji su dosli').strip()
        odziv_donora = np.array(list(map(int, odziv_donora.split(','))))
        s.used_ids = s.used_ids | set(odziv_donora)
