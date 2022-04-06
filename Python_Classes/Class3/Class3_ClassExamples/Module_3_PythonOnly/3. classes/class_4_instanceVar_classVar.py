# any attribute starting with self is an instance attr
class education:
    a = "class variable"   # can be accessed via class or obj
    def __init__(self, n):
        self.name = n  # name is an instance/object attr
        self.dept = "Data science" #


ravi = education("ravi")
shyam = education("shyam")

print(ravi.name)
print(shyam.name)

# class var can be accessed via class or objects
print(ravi.a)
print(shyam.a)
print(education.a)  # prefered way to access class var

print("#"*10)
# class var can only be modified by class name
education.a = 'new value'
print(ravi.a)
print(shyam.a)
print(education.a)

# class var can onl