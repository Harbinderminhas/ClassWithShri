class education:
    def __init__(self):
        print("111")

    def __del__(self):
        print("object is going to be deleted, used for clean up actions")

obj = education()
#del obj
print("#"*10)
# If object is deleted then second stmt del
# obj should give some error, if not then wht it is deleting??
