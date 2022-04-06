import re

data = 'abcde abcdef abcdef'
# 1
# print(re.sub('[adc]', '*', data))
# print(re.sub('ad', '*', data))
#2 two square brackets
# print(re.sub('[abc][123]', '*', "a1+b2+d4+e5"))

# 3: . dot operator: matches any character except new line
#print(re.sub('A.B', '*', 'A2B A:B A,C'))

# 4: \d: matches a single number
# my_str = "my phone number is 87389357784588586"
# print(re.sub('\d', '&', my_str))

# 5: + operator makes the search greedy
# here /d+ is matching a continuous complete number
# my_str = "my phone number is 87389357784588586"
# print(re.sub('\d+', '&', my_str))

# 6: +
# print(re.sub('AB+', '*', 'ABC ABBBBBBBC AC BBBB'))

#7 :{m,n}
# print(re.sub('AB{3,6}', '*', 'ABB ABBB ABBBBBBBBBBB'))

#8: ^: matches start of a string
#print(re.sub('^abc', '*', 'abc abc abcdef'))

# 9: $ : matches the end of line
# print(re.sub('abc$', '*', 'abc def')) # NO O/P
# print(re.sub('abc$', '*', 'abc def abc'))

# 10: * : matches 0 or more
#     + : matches 1 or more

# str1= "my phone no is 123"
# print(re.sub("\d+","&",str1))
# str1= " 123 my phone no is"
# print(re.sub("\d*","&",str1))

# 11. search(pattern, input_str):
# 1. matches only the first match ignores remaining.
# 2. returns an match object
# 3. you can call .group() on it to get a matched value
# my_str = "my phone number is 87343784574875 prateek number is 7847855"
# match_obj = re.search('\d+', my_str)
# if match_obj:
#     print(match_obj.group())
# else:
#     print("No match")

# 12. match(pattern, input_str):
# 1. matches the beginning of the string only
# 2. returns an match object
# 3. you can call .group() on it to get a matched value
# my_str = "87343784574875 my phone number is  prateek number is 7847855"
# match_obj = re.match('\d+', my_str)
# if match_obj:
#     print(match_obj.group())
# else:
#     print("No match")

# 13
"""
'r' designates a python raw string
 it is used to avoid the interpretation of special symbols like /n, /t, /b
"""

# 14: /b is for word boundary
# word boundary:
# 1.start of a string
# 2. end of the string
# 3. space between words
#task: find a number that has word boundary at both ends
# my_str = r"welcome 123 the456 678course"
#
# match_obj = re.search(r'\b\d+\b', my_str)
# if match_obj:
#     print(match_obj.group())
# else:
#     print("No match")

# 14: findall(): returns all the matches but search() method returns the first match
# returns the matches as list of string

# my_str = "number is 27676 87857 kjfjhjrhg 8e7875  jhrhrgi85485"
# output = re.findall(r'\d+', my_str)
# print(output)

"""
For example: Sandstrom, Miss. Marguerite Rut
Bonnell, Miss. Elizabeth
Saundercock, Mr. William Henry
Andersson, Mr. Anders Johan.
If i have a file that contains a column with such data how can
I use the regular expression to separate first name and last name
"""









