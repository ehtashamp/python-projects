"""
To select avg Closing value for Zensar for individual year.
"""
import sqlite3
try:
    with sqlite3.connect('Zensar_records') as db:
        cursor = db.cursor()
        cursor.execute('''select strftime('%Y',Date), avg(Close) 
                       from zensar_data group by strftime('%Y',Date)''')
        for row in cursor.fetchall():
            print(row)
except Exception as E:
    print('Error: ', E)
