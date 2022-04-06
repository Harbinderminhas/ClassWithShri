class education():
    def __init__(self):
        self.__pri=("I am Private")
        self._pro=("I am Protected")
        self.pub=("I am Public")

ob=education()
print(ob.pub)
print(ob._pro)
print(ob.__pri)