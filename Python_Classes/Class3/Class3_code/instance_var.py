class education:
    domain=("Data Science")
    def Setcourse(self,name):
        self.name=name

ob1=education()
ob2=education()

ob1.Setcourse("Python")
ob2.Setcourse("Machine Learning")

print(ob1.domain)
ob1.domain = 'GOD'
print(ob1.domain)
print(ob2.domain)

print(ob1.name)
print(ob2.name)
