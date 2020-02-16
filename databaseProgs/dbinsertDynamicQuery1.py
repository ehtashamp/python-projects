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
        cursor =db.cursor() #step 3 - create a cursor
        #dynamic query - foramt the tring to add the values from user input
        sql = '''insert into emp values ({}, '{}', {}, {}, '{}')'''.format(id, name, salary, age, dept)
        cursor.execute(sql) #step4 ddl query
        db.commit() #whenever data is added or updated
except Exception as E:
    print('Error: ', E)
else:
    print(sql)
    print('Data inserted into the table')
    #to view the data in the database install sqlite browser, there you can view the db.
