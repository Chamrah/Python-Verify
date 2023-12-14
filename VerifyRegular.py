import re
def is_digits(str):
    return bool(re.search(r'\d', str))