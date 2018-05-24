import pandas as pd
import numpy as np
from krvjezivot.constants import *
import pickle
from sklearn.metrics import fbeta_score, make_scorer
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
import requests
from imblearn.metrics import geometric_mean_score
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, GridSearchCV, cross_validate, cross_val_score
from sklearn.neural_network import MLPClassifier
import warnings
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils import shuffle
from sklearn.linear_model import LogisticRegression
from typing import List

from sklearn.model_selection import train_test_split, KFold, GridSearchCV


def dohvati_rj_za(donors, indices: List[int], days_past):
    r = requests.post('http://hackaton.westeurope.cloudapp.azure.com/api/evaluate',
                      json={"input_ids": all_indices, "days_past": days_past})
    dosli = set(map(int, r.text.split(',')))
    dataset = pd.concat([donors, pd.DataFrame({'dosao': np.zeros(len(indices))})], axis=1)
    for index, row in dataset.iterrows():
        if row.id in dosli:
            dataset.loc[index, 'dosao'] = 1
    # dataset = dataset.drop('id', axis=1)
    dataset.to_csv(f'dataset.csv')
    return dataset


def nested_cross_validation(df, features, estimator, p_grid, n_trials=5, outer_splits=4, inner_splits=6, skip_cv=False):
    # rus = RandomUnderSampler(return_indices=True)
    # X_resampled, y_resampled, idx_resampled = rus.fit_sample(df[features], df['dosao'])
    rus = RandomOverSampler()
    X_resampled, y_resampled = rus.fit_sample(df[features], df['dosao'])
    # splitting dataset
    # train, test = train_test_split(df, test_size=0.2, shuffle=True)
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, shuffle=True)
    # X_train, y_train = train[features], train['dosao']
    # X_test, y_test = test[features], test['dosao']
    #     print(f'train: X: {X_train.shape}, Y: {y_train.shape}')
    #     print(f'test: X: {X_test.shape}, Y: {y_test.shape}')

    # outer_cv = KFold(n_splits=outer_splits)
    inner_cv = KFold(n_splits=inner_splits, shuffle=True)

    #     clfs, scores = [], []
    #     for i in range(n_trials):
    # Nested CV with GRID SEARCH parameter optimization
    # inner used for finding optimal parameters
    # clf = GridSearchCV(estimator=estimator, param_grid=p_grid, cv=inner_cv, n_jobs=-1, scoring=make_scorer(geometric_mean_score))
    clf = GridSearchCV(estimator=estimator, param_grid=p_grid, cv=inner_cv, n_jobs=-1)
    clf.fit(X_train, y_train)
    # outer used for evaluating the model
    #         if skip_cv:
    #             score = clf.score(X_train, y_train)
    #         else:
    #             score = cross_val_score(clf, X=X_train, y=y_train, cv=outer_cv)
    #         scores.append(score.mean())
    #         clfs.append(clf)
    #     scores = np.array(scores)
    #     best_val_score = scores.max()
    #     print(f'best validation score from {n_trials} trials: {best_val_score}')
    #     best_clf = clfs[scores.argmax()]

    best_clf = clf
    print(f'best params:\n{best_clf.best_params_}')
    print(f'best model:\n{best_clf.best_estimator_}')
    print(f'\nTEST')
    test_set_accuracy = clf.score(X_test, y_test)
    print(f'test accuracy: {test_set_accuracy}')
    z = clf.predict_proba(X_test)
    # measurements = model_evaluation(y_test, best_clf.predict(X_test))
    # return best_clf, measurements  # return grid search object which contains best estimator
    return best_clf



def ucitaj_dataset(file):
    dataset = pd.read_csv(file)
    return dataset


def predobradi_dataset(df, drop=True):
    if drop:
        df = df.drop(df.columns[0], axis=1)
    df['blood_group'] = df['blood_group'].map(BLOOD_GROUP_MAP)
    df['sex'] = df['sex'].map(SEX_MAP)
    scaler = sklearn.preprocessing.StandardScaler()
    df = scaler.fit_transform(df)
    return df


def buildaj_model(task):
    dataset = ucitaj_dataset('dataset.csv')
    features = [x for x in dataset.columns if x != 'dosao']
    dataset = predobradi_dataset(dataset)

    clf = None
    if task == 'LR':
        lr_estimator = LogisticRegression()
        lr_grid = {"C": np.linspace(0.1, 100, 20)}
        clf = nested_cross_validation(dataset, features, lr_estimator, p_grid=lr_grid)
    elif task == 'NN':
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            # nn_grid = {'alpha': (1e-2, 1e-1, 1), 'hidden_layer_sizes': range(10, 100, 10)}
            nn_grid = {'alpha': (1e-3, 1e-2, 1e-1), 'hidden_layer_sizes': [[10, 100], [10, 150]]}
            # nn_grid = {'alpha': (1e-3, 1e-4), 'hidden_layer_sizes': range(10, 100)}
            clf = nested_cross_validation(dataset, features,
                                          MLPClassifier(activation='logistic', solver='adam', max_iter=300, batch_size=100),
                                          nn_grid, n_trials=1)
    with open(f'model_{task}', 'wb') as of:
        pickle.dump(clf, of)


def ucitaj_model(model_file):
    with open('model', 'rb') as in_file:
        model = pickle.load(in_file)
    return model


if __name__ == '__main__':
    # donors = pd.read_csv('donors.txt')
    # all_indices = list(donors.id)
    # dohvati_rj_za(donors, all_indices, 0)
    # # dataset = dohvati_rj_za(donors, all_indices, days_past=0)

    buildaj_model('NN')
