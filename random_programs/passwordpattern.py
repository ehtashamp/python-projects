"""
To check the password strength
It should contain at least
1 character, 
1 digit
1 special character
Length should be greater than 8

"""
import re
import getpass

def checkstrength(pswd):
    # checking length
    flag= 1
    if len(pswd) < 8:
        flag = 0
        # return "length is less than 8 characters"
    m1 = re.search('[a-zA-Z]', pswd)
    m2 = re.search('[0-9]', pswd)
    m3 = re.search('[^a-zA-Z0-9]', pswd) 
    #m3 = re.search('[!@#$%^&*()_+]', pswd) 
    if flag and m1 and m2 and m3:
        return "correct password"
    else:
        return "incorrect password"

pswd = getpass.getpass("Please enter a password without spaces:- ")
result = checkstrength(pswd.strip(' '))
print(result)
