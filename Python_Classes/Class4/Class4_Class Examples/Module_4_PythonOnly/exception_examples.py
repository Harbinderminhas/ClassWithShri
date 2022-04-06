import sys
"""
#1
a = 12
b = 13
try:
    c = a/0
    print("111")
except ZeroDivisionError:
    print("you have entered the wrong value for division")
    #a, b, c = sys.exc_info()

print("2222")
"""

"""
#2
# catch multiple exceptions
try:
    a = 12
    b = 13
    c = a + b
    print(d)
except NameError:
    print("wrong var")

except TypeError:
    pass
except KeyError:
    pass
else:
    print("No exception was raised")
"""

"""
#3
# catch all the exceptions

try:
    print(g)
    a = 2/0
except:
    print("I will catch all the exceptions")
    print(sys.exc_info())  # to get exception info
"""

"""
#4
# finally block gets executed in all scenarios(exception and no exception)
# used for the cleanup actions: ex: closing the connection to a server

try:
    #a = 12 + "hello"
    a = 12 + 13

except TypeError:
    print("OOps")
finally:
    print("executed all the times")
"""