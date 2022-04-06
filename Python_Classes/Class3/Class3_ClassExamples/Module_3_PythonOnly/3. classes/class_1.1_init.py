"""
1. __init__ is a constructor(not exactly but closest to it)
2. self : object reference

'init' stands for initialisation i.e when you create an  object if you wish
to have some attributes defined with the value then you would use __init__
"""


class educationStudent:
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.course = c

    def show_name(celina):
        print(celina.name)

################### creating object(education student)#####

ravi = educationStudent("Ravi singh", 25, 'Py')  # ravi.__init__(ravi)

# calling a method
ravi.show_name()  # ravi.show_name(ravi)

# accessing an object's attribute
print(ravi.name)
print(ravi.age)
# is self a keyword ?
# Ans: No
