"""
There are two types of variables
1. object/instance variable (or object attributes) : are not shared
2. class variable: shared by all objects

class attributes are owned by class
"""

class education:
    a = 12 # class var
    b = 13  # clas var

# How to access a class var
# best way is via class name
print(education.a)

# can access via object also
obj1 = education()
obj2 = education()
print(obj1.a)
print(obj2.a)

# Modify a class variable
# It can only be done via class
education.a = 500
print(education.a)
print(obj1.a)
print(obj2.a)