"""
r+ allows both read and write but the file has to be present
w+ allows both read and write and if file is not present the it would be created
"""

fo = open('esha.txt', 'w+')
fo.write("Data science")
fo.seek(0)
print(fo.read())
fo.close()