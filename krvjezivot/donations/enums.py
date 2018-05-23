from enumfields import Enum  # Uses Ethan Furman's "enum34" backport


class BloodGroup(Enum):
    ZERO_MINUS = '0-'
    ZERO_PLUS = '0+'
    A_MINUS = 'A-'
    A_PLUS = 'A+'
    B_MINUS = 'B-'
    B_PLUS = 'B+'
    AB_MINUS = 'AB-'
    AB_PLUS = 'AB+'


class RhesusFactor(Enum):
    NEGATIVE = '-'
    POSITIVE = '+'
