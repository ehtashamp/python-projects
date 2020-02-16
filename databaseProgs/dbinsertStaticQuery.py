"""
Database connection program
Insert query using static query
"""
import sqlite3 #step 1
try:
    with sqlite3.connect('Employee') as db: #using context manager
        cursor =db.cursor() #step 3 - create a cursor
        #static query
        cursor.execute('''insert into emp values (1, 'Jatin', 10000, 34, 'IT')''') #step4 ddl query
        db.commit() #whenever data is added or updated
except Exception as E:
    print('Error: ', E)
else:
    print('Data inserted into the table')
    #to view the data in the database install sqlite browser, there you can view the db.
