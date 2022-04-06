# user defined exception

import sys

class WrongValue(Exception):
    pass


val = input("Enter a list:")
val = eval(val)
try:
    if not isinstance(val, list):
        raise WrongValue("Only list value is allowed")
        # raise keyword raises the exception
    val.append("education rocks")  # this works with list object only.
    print(val)
except WrongValue:
    print("Wrong value entered by the user")
    print(sys.exc_info())