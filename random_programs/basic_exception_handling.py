"""
To two numbers as input
print their difference if the first number is greater than the second number
otherwise print their sum.

first_num = int(input('Enter first number:- '))
second_num = int(input('Enter second number:- '))
if first_num > second_num:
    print(first_num - second_num)
else:
    print(first_num + second_num)
"""


# Diffsum
# num = [1, 2]
# num[0] = int(input('Enter first number:- '))
# num[1] = int(input('Enter second number:- '))
# print(num[0] - num[1]) if (num[0] > num[1]) else print(num[0] + num[1])
# try:
#     print('reuslt {}'.format(num[0]/num[1]))
# except ZeroDivisionError:
#     print("0 added as inout for division")

# simple try and except
# count = 0
# while count < 5:
#     try:
#         divisor = int(input('Enter divisor number:- '))
#         print('result {}'.format(100 / divisor))
#         break
#     except ZeroDivisionError:
#         count += 1
#         print("divisor is given as 0")
#         print('enter another divisor')
# print("program endsss")






#multiple except for a try block
# count = 0
# while count < 5:
#     try:
#         divisor = int(input('Enter divisor number:- '))
#         print('result {}'.format(100 / divisor))
#         print(divisor + 'number')
#         break
#     except ZeroDivisionError:
#         count += 1
#         print("divisor is given as 0")
#         print('enter another divisor')
#     except TypeError as E:
#         print('Error:', E)
#
# print("program endsss")
#


# nested try except
count = 0
# while count < 5:
# try:
#     divisor = int(input('Enter divisor number:- '))
#     print('result {}'.format(100 / divisor))
#     print(divisor + 'number')
#     # break
# except ZeroDivisionError:
#     # count += 1
#     try:
#         divisor = int(input('Enter divisor number:- '))
#         print('result {}'.format(100 / divisor))
#     except ZeroDivisionError as Z:
#         print('Error:', Z)
# except TypeError as E:
#     print('Error:', E)
#
# print("program endsss")

#else with try block
# try:
#     divisor = int(input('Enter divisor number:- '))
#     print('result {}'.format(100 / divisor))
#     print(divisor + 'number')
#     # break
# except ZeroDivisionError:
#     # count += 1
#     try:
#         divisor = int(input('Enter divisor number:- '))
#         print('result {}'.format(100 / divisor))
#     except ZeroDivisionError as Z:
#         print('Error:', Z)
# except TypeError as E:
#     print('Error:', E)
# else:
#     print("program endsss")

#finally block with try
# try:
#     divisor = int(input('Enter divisor number:- '))
#     print('result {}'.format(100 / divisor))
#     print(divisor + 'number')
#     # break
# except ZeroDivisionError:
#     # count += 1
#     try:
#         divisor = int(input('Enter divisor number:- '))
#         print('result {}'.format(100 / divisor))
#     except ZeroDivisionError as Z:
#         print('Error:', Z)
# except TypeError as E:
#     print('Error:', E)
# finally:
#     print("program endsss")
import sys
#generic exception
try:
    divisor = int(input('Enter divisor number:- '))
    print('result {}'.format(100 / divisor))
    print(divisor + 'number')
    # break
except ZeroDivisionError:
    # count += 1
    try:
        divisor = int(input('Enter divisor number:- '))
        print('result {}'.format(100 / divisor))
    except ZeroDivisionError as Z:
        print('Error:', Z, sys.exc_info()[0])
except TypeError as E:
    print('Error:', E, sys.exc_info()[0])
except Exception as E:
    print('Generic Exception Error:', E, sys.exc_info()[0]) #it provides the information about the exception
finally:
    print("program endsss")