class education():
    def __init__(self):
        self.__pri="I am Private"
        self.__pro="I am Protected"
        self.pub="I am Public"

ob=education()

#Accessing Public Attribute
ob.pub

#Accessing Protected Attributes
ob.__pro

#Accessing Private Attributes
ob.__pri