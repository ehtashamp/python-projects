"""
Database connection program
Insert query using dynamic query
"""
import sqlite3 #step 1
#take input from the user to be added into the database.
id = int(input('Enter emp id - '))
name = input('Enter emp name - ')
age = int(input('Enter emp age - '))
salary = int(input('Enter emp salary - '))
dept = input('Enter emp department - ')

try:
    with sqlite3.connect('Employee') as db: #using context manager
        cursor = db.cursor() #step 3 - create a cursor
        #dynamic query - foramt the tring to add the values from user input
        # inserting data with dictionary - key value pair
        cursor.executemany('''insert into emp values (:id,:name,:salary,:age,:dept)''',
        [{'id':id, 'name':name, 'salary':salary, 'age':age, 'dept':dept},
        {'id':id, 'name':name, 'salary':salary, 'age':age, 'dept':dept}])
        db.commit() #whenever data is added or updated
except Exception as E:
    print('Error: ', E)
else:
    print('Data inserted into the table')
    #to view the data in the database install sqlite browser, there you can view the db.
