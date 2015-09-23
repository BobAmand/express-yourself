

'''
The Iron Works - Exercise 14 express-yourself
- Objective is to test 'regular expressions'
- Three test areas have been established:
   * extractor
   * separator
   * validator  [current file]

'''
import pytest
import re

def binary(inp):      # Glenn Hurley guidance:
    match = re.search(r'([0-1]+)', inp)
    # if not inp is testing if string is empty
    if not inp or inp != match.groups()[0]:
        return False
    return True


def word(text):       # Expecting 4 assert pass, 3 not assert pass.
    return re.findall(r'([a-z]{4,10})[^!+][^*]',text)
    # match = re.search(r'([a-z]{4,10})[^!+][^*]', text)
    # if match:
    #     return True
    # else:
    #     return False


def words(text):       # Expecting
    if re.match(r'(([a-z]{4,10})[^!+][^*])', text):
        return True
    else:
        return False
