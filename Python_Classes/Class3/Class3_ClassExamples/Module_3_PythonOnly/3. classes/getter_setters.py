class education:
    def __init__(self, courseName):
        self.courseName = courseName

    def getter_courseName(self):
        return self.courseName

    def setter_courseName(self, new_val):
        self.courseName = new_val

########## user code###

obj = education("Python")
# print(obj.courseName)
# obj.courseName = "Django"
# print(obj.courseName)

print(obj.getter_courseName())
obj.setter_courseName("Django")
print(obj.getter_courseName())
