
# adding attribute dynamically

class educationStudent:
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.course = c
        self.fees = '$300'

    def show_name(celina):
        print(celina.name)


ravi = educationStudent("Ravi singh", 25, 'Py')  # ravi.__init__(ravi)

# adding an user defined attribute dynamically
ravi.sudipta = "hello"
print(dir(ravi))

shyam = educationStudent("Shyam sundar", 28, 'Py')
print(dir(shyam))
