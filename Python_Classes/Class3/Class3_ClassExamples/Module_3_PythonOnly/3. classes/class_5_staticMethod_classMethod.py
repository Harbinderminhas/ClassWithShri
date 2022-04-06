"""
1.class method:
- By putting the in-built decorator @classmethod makes a method
a class method.
- Class method would take first parameter as class whenever it is called.
- It can be called by both object as well as Class name, however it
should be called with class Name only.

2. static method
- no extra parameter like self or cls is passed to this method
"""

class education:
    i = 100
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod  # it will prevent self being passed as arg
    def square(val):
        return val**2

    @classmethod  # first param would be class
    def cube(cls, val):
        print(cls.i)  # same as education.i
        #print(cls(1,2)) # instantiating the class

# same like java for static operation, meaning it is not a memeber of class


# class and static methods can be called without object, can be called with class name
education.square(2)
education.cube(3)

# can also be called with object:
obj = education(1, 2)
print(obj.square(10))# obj.square()