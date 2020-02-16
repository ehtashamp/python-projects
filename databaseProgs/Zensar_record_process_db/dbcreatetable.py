"""
Database connection program
"""
import sqlite3 #step 1
# db = sqlite3.connect('Employee') #step2 - create or setup a connection with database
# cursor =db.cursor() #step 3 - create a cursor
# cursor.execute('''create table emp(id int, name text, salary int, age int, dept text)''') #step4 ddl query
# db.close()
try:
    with sqlite3.connect('Zensar_records') as db: #using context manager
        cursor =db.cursor() #step 3 - create a cursor
        cursor.execute('''create table zensar_data(
        Date TEXT, 
        Open REAL,
        High REAL ,
        Low REAL ,
        Close REAL,
        WAP REAL,
        NoofShares REAL,
        NoofTrades REAL ,
        Totalturnover REAL,
        DeliverableQuantity REAL ,
        DeliQtytoTradedQty REAL ,
        SpreadHL REAL,
        SpreadCO REAL
        )''') #step4 ddl query
except Exception as E:
    print('Error: ', E)
else:
    print('Table already exisits')
