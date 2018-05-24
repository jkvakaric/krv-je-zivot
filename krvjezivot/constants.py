import numpy as np

# minimalna vrijednost
O_MIN = [
    38,
    115,
    46,
    100,
    38,
    23,
    8,
    16,
]

# maksimalna vrijednost
O_MAX = [
    78,
    240,
    96,
    210,
    82,
    50,
    18,
    36,
]

# srednja vrijdnost
O_Z = [
    58,
    177,
    71,
    155,
    60,
    36,
    13,
    26,
]

# potrosnja
P = [
    35,
    105,
    42,
    91,
    35,
    21,
    7,
    14,
]

GROUP_O_minus = 0
GROUP_O_plus = 1
GROUP_A_minus = 2
GROUP_A_plus = 3
GROUP_B_minus = 4
GROUP_B_plus = 5
GROUP_AB_minus = 4
GROUP_AB_plus = 5

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
