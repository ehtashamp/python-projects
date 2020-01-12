"""
Documentation interlude
Program to accept a lucky number from the end user and return
all possible combinations of vehicle numbers he can opt for.
This is based on the logic that the final sum of the digits of the vehicle
should be equal to the user's lucky number.
"""
def calc_lucky_number(number,lucky_num):
    '''
    Called recursively
    Accepts int and int as parameters, iterated number and lucky number input by the end user
    Returns 'int' , the number(single digit value)
    '''
    temp_list = list()
    if(len(str(number)) != 1):
        for i in str(number):
            temp_list.append(int(i))
        return calc_lucky_number(sum(temp_list),lucky_num)
    elif len(str(number)) == 1:
        return number

def getLuckyNum(lucky_num):
    '''
    Accepts int as parameter, lucky number input by the end user
    Returns list, final list to the getInput function for displaying the output
    '''
    lucky_list = list()    
    for number in range(1,10000):
        final_val = calc_lucky_number(number,lucky_num)
        if final_val == lucky_num:
            lucky_list.append(str(number).rjust(4,'0'))
    return lucky_list


def getInput():
    '''
    Recursive, till a correct value is entered by the end user.
    Accpets no parameters
    Returns no parameters
    Calls getLuckyNum function and prints the return value from it as a result to the end user.
    '''
    lucky_num = input('Enter your lucky number(0-9) for vehicle number generation:- ')
    if len(lucky_num) == 1 and ord(lucky_num) in range(48,58):
        list_num = getLuckyNum(int(lucky_num))
        print(list_num)
        del list_num
        
    else:
        print('Invalid input. Please provide a single digit numner between 0-9)')
        #recursion added to prompt user to enter correct input
        getInput()
# Execution begins!!!
getInput()
