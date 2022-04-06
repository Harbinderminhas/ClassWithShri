# +, /d, {}, [], ^, $, search, match, sub, findall

import re
# match_obj = re.search('xy', 'hello ab and ab is ab')  # first occurence search(pattern, input)
# if match_obj:
#     print("found match")
#     print(match_obj.group())  # to see the matched value
# else:
#     print("No match")
#
#
# # findall() it gives all the matches
#
# out_list = re.findall('ab', "hello ab and ab is ab")
# print(out_list)
#

# match() it tries to match at the beginning only
match_obj = re.match('ab', 'ab hello')
if match_obj:
    print("found match")
    print(match_obj.group())  # to see the matched value
else:
    print("No match")

