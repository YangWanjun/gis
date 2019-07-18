import re
from utils import constants


def is_digit(s):
    return re.match(constants.REG_DIGIT, s) is not None
