'''
Extractor functions

'''
import re

def phone_numbers(text):
    return re.findall(r'\(?\d{3}\W*\d{3}\-?\d{4}',text)

    #
    # phone_nums = []
    # text_list = text.split()
    # for num in text_list:
    #     match = re.search(r'\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}', num)
    #     if match:
    #         phone_nums.append(match.groups())
    # return phone_nums
