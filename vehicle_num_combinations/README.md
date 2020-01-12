Python program
	To get all possible combinations of vehicle numbers whoes sum is equivalent to the users lucky number.
calc_lucky_number
	- This function is defined for processing the numbers to generate the lucky number input by the
	  end user.
	- called recursively
	- accepts int and int as parameters, iterated number and lucky number input by the end user 
	- returns 'int' , the number(single digit value)
getLuckyNum
	- This is parent funciton from the calc_lucky_number is called.
	- accepts int as parameter, lucky number input by the end user
	- returns list, final list to the getInput function for displaying the output
getInput
	- This is user input function, written to prompt the user to enter a valid input, with a descriptive error/help message.
	- recursive, till a correct value is entered by the end user.
	- accpets no parameters
	- returns no parameters
	- calls getLuckyNum function and prints the return value from it as a result to the end user.












