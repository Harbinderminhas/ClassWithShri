class education:
    def __init__(self):
        self.pub = "public attribute"
        self._prot = "protected attr"
        self.__pri = "private attr"

    def method(self):
        print("public method")

    def __private_my_method(self):
        print("Private method")

    def method2(self):
        self.__private_my_method()
        print("calling private attr without name mangling:", self.__pri)


### client code  #
obj = education() # it would call init method

print(obj.pub)

print(obj._prot)
print(obj._education__pri)  # name mangling
obj._education__private_my_method()
obj.method2()



"""
self.pub and self.prot is created in INIT method, how come call it in out side of that  method?
similar like can we create these variables from other methd as well?
"""
