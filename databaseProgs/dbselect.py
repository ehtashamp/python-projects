import sqlite3
try:
    with sqlite3.connect('Employee') as db:
        cursor = db.cursor()
        cursor.execute('''select * from emp''')
        for row in cursor.fetchall():
            print(row)
except Exception as E:
    print('Error ', E)
else:
    print('Table data is fetched')