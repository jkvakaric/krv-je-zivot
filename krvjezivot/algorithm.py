import pandas as pd
import requests
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

from krvjezivot.constants import *


def calculate_who_to_invite(O_MIN, O_MAX, O_Z, P, Z):
    pass


def dohvati_rj_za(donors, indices: List[int], days_past):
    r = requests.post('http://hackaton.westeurope.cloudapp.azure.com/api/evaluate',
                      json={"input_ids": all_indices, "days_past": days_past})
    dosli = set(map(int, r.text.split(',')))
    dataset = pd.concat([donors, pd.DataFrame({'dosao': np.zeros(len(indices))})], axis=1)
    for index, row in dataset.iterrows():
        if row.id in dosli:
            dataset.loc[index, 'dosao'] = 1
    dataset = dataset.drop('id', axis=1)
    dataset.to_csv(f'dataset.csv')
    return dataset


def nested_cross_validation(df, features, estimator, p_grid, n_trials=5, outer_splits=4, inner_splits=6, skip_cv=False):
    # splitting dataset
    train, test = train_test_split(df, test_size=0.3, shuffle=True)
    X_train, y_train = train[features], train['dosao']
    X_test, y_test = test[features], test['dosao']
    #     print(f'train: X: {X_train.shape}, Y: {y_train.shape}')
    #     print(f'test: X: {X_test.shape}, Y: {y_test.shape}')

    # outer_cv = KFold(n_splits=outer_splits)
    inner_cv = KFold(n_splits=inner_splits, shuffle=True)

    #     clfs, scores = [], []
    #     for i in range(n_trials):
    # Nested CV with GRID SEARCH parameter optimization
    # inner used for finding optimal parameters
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


donors = pd.read_csv('donors.txt')
all_indices = list(donors.id)
# dataset = dohvati_rj_za(donors, all_indices, days_past=0)

dataset = pd.read_csv('dataset.csv')


def predobradi_dataset(df, features):
    dataset['blood_group'] = dataset['blood_group'].map(BLOOD_GROUP_MAP)
    dataset['sex'] = dataset['sex'].map(SEX_MAP)
    scaler = sklearn.preprocessing.StandardScaler()
    all_features_list = list(features)
    df[all_features_list] = scaler.fit_transform(df[all_features_list])
    return df


dataset = dataset.drop(dataset.columns[0], axis=1)
features = [x for x in dataset.columns if x != 'dosao']
dataset = predobradi_dataset(dataset, features)


task = 'NN'

if task == 'LR':
    lr_estimator = LogisticRegression()
    lr_grid = {"C": np.linspace(0.1, 100, 20)}
    clf = nested_cross_validation(dataset, features, lr_estimator, p_grid=lr_grid)
elif task == 'NN':
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        nn_grid = {'alpha': (1e-2, 1e-1, 1), 'hidden_layer_sizes': range(10, 100, 10)}
        # nn_grid = {'alpha': (1e-3, 1e-4), 'hidden_layer_sizes': range(10, 100)}
        best_nn = nested_cross_validation(dataset, features, MLPClassifier(activation='logistic', solver='adam', max_iter=300, batch_size=100), nn_grid, n_trials=1)
