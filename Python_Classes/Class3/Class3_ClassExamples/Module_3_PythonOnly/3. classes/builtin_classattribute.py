class A:
    pass
class education(A):
    """
    this is a
    education class
    """

    var = 100
    def func(self):
        pass


#1. __dict__
print(education.__dict__)

#2. __doc__
print(education.__doc__)

#3. __name__
print(education.__name__)

#4. __module__
print(education.__module__)

#5. __bases__
print(education.__bases__)
