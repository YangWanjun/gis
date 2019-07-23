import re
from utils import constants


def is_digit(s):
    return re.match(constants.REG_DIGIT, s) is not None


def parse_querystring(params):

    def split(string):
        matches = re.split(r"[\[\]]+", string)
        matches.remove('')
        return matches

    def mr_parse(params):
        results = {}
        for key in params:
            if '[' in key:
                key_list = split(key)
                d = results
                for partial_key in key_list[:-1]:
                    if partial_key not in d:
                        d[partial_key] = dict()
                    d = d[partial_key]
                d[key_list[-1]] = params[key]
            else:
                results[key] = params[key]
        return results

    return mr_parse(params)
