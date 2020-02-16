"""
To read from  csv file and add the data into the database.
"""
import sqlite3 #step 1
def avg_bse():
    all_rec = list()
    with open('BSE-BOM504067.csv','r') as fileobj:
        for line in fileobj:
            line = line.strip()
            cols = line.split(',')
            ind_rec = dict()
            ind_rec['Date'] = cols[0]
            ind_rec['Open'] = cols[1]
            ind_rec['High'] = cols[2]
            ind_rec['Low'] = cols[3]
            ind_rec['Close'] = cols[4]
            ind_rec['WAP'] = cols[5]
            ind_rec['NoofShares'] = cols[6]
            ind_rec['NoofTrades'] = cols[7]
            ind_rec['Totalturnover'] = cols[8]
            ind_rec['DeliverableQuantity'] = cols[9]
            ind_rec['DeliQtytoTradedQty'] = cols[10]
            ind_rec['SpreadHL'] = cols[11]
            ind_rec['SpreadCO'] = cols[12]
            all_rec.append(ind_rec)
        return all_rec

zensar_rec_list = avg_bse()
try:
    with sqlite3.connect('Zensar_records') as db: #using context manager
        cursor = db.cursor() #step 3 - create a cursor
        cursor.executemany('''insert into zensar_data values (:Date,:Open,:High,:Low,:Close, :WAP,
        :NoofShares, :NoofTrades, :Totalturnover,
        :DeliverableQuantity, :DeliQtytoTradedQty , :SpreadHL, :SpreadCO)''', zensar_rec_list)
        db.commit()
except Exception as E:
    print('Error: ', E)
else:
    print('Data added in the table.')
