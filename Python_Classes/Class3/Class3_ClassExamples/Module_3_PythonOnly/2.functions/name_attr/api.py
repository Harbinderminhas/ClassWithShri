# what is __name__ == '__main__'

# pradeep's code

def square(a):
    print(a**2)


def cube(i):
    print(i**3)

print(__name__)
if __name__ == '__main__':
    square(10)
    cube(8)
# Is name reffering tp Pradeep's code?
# is this __name__ is standard variable for this kind of execution ?
