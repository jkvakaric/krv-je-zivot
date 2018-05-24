from enumfields import Enum  # Uses Ethan Furman's "enum34" backport


class BloodGroup(Enum):
    ZERO = '0'
    A = 'A'
    B = 'B'
    AB = 'AB'


class RhesusFactor(Enum):
    NEGATIVE = '-'
    POSITIVE = '+'
