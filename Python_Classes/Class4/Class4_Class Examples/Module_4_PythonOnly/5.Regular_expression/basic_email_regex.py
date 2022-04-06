import re
with open('emails.txt', 'r') as fo:
    pattern = '[a-zA-Z]+[_0-9]+@gmail.com'
    correct_emails = re.findall(pattern, fo.read())
    print(correct_emails)

