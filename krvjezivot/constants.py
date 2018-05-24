import numpy as np

# minimalna vrijednost
O_MIN = np.array([
    38,
    115,
    46,
    100,
    38,
    23,
    8,
    16,
])

# maksimalna vrijednost
O_MAX = np.array([
    78,
    240,
    96,
    210,
    82,
    50,
    18,
    36,
])

# srednja vrijdnost
O_Z = np.array([
    58,
    177,
    71,
    155,
    60,
    36,
    13,
    26,
])

# potrosnja
P = np.array([
    35,
    105,
    42,
    91,
    35,
    21,
    7,
    14,
])

GROUP_O_minus = 0
GROUP_O_plus = 1
GROUP_A_minus = 2
GROUP_A_plus = 3
GROUP_B_minus = 4
GROUP_B_plus = 5
GROUP_AB_minus = 4
GROUP_AB_plus = 5

PRIMA_GROUPU = {
    '0': ['0'],
    'A': ['0', 'A'],
    'B': ['0', 'B'],
    'AB': ['0', 'A', 'B', 'AB'],
}

PRIMA_FAKTOR = {
    '-': ['-'],
    '+': ['-', '+'],
}

# for model learning
BLOOD_GROUP_MAP = {
    '0-': 0,
    '0+': 1,
    'A-': 2,
    'A+': 3,
    'B-': 4,
    'B+': 5,
    'AB-': 6,
    'AB+': 7,
}

SEX_MAP = {
    'Z': 0,
    'M': 1,
}


GROUP_FACTOR_PRIMA = {
    f'{k1}{k2}': [vi1 + v2i for vi1 in v1 for v2i in v2]
    for k1, v1 in PRIMA_GROUPU.items()
    for k2, v2 in PRIMA_FAKTOR.items()
}

PRIORITY_GF_LIST = sorted(GROUP_FACTOR_PRIMA, key=lambda x: len(GROUP_FACTOR_PRIMA[x]))


if __name__ == '__main__':
    print(GROUP_FACTOR_PRIMA)
    print(PRIORITY_GF_LIST)
