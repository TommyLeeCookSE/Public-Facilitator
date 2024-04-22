import sqlite3

conn = sqlite3.connect(r'WebPages/facilities.db')
cursor = conn.cursor()

cursor.execute('''
            
               ''')

conn.commit()
conn.close()