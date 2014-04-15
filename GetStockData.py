# This file downloads stock market data and writes it to a SQLite table
import sqlite3
import os #operating system 
DATA_PATH = 'C:\Users\Dave\Documents\StockData'
conn = sqlite3.connect('stockanalysis.db')
c = conn.cursor()
for fname in os.listdir(DATA_PATH):
	print(fname)
	f = open(os.path.join(DATA_PATH, fname))

	for line in f.readlines():
		[date, stock_open, high, low, stock_close, volume, adj_close] = line.rstrip().split(',')
		c.execute('INSERT INTO raw_data VALUES (?,?,?)', (os.path.splitext(fname)[0], date, float(adj_close))) 
		#tuple, replace question marks by those 3 values
	
	f.close() 

conn.commit()
conn.close()