import sqlite3
from datetime import datetime

class Walkin:
        def __init__(self, date,security,value):
            self.date = date
            self.security = security
            self.value = value

def walkin_table_info():
    #Returns the entire table soreted such that the most recent is ontop date, security, reason
    conn = sqlite3.connect(r'WebPages/facilities.db')
    cursor = conn.cursor()

    query = ('''SELECT * FROM walkin_tracker''')
    cursor.execute(query)
    list_of_objects = []
    rows = cursor.fetchall()
    for item in rows:
         list_of_objects.append(Walkin(item[0],item[1],item[2]))

    conn.close()
    return list_of_objects

def process_walkin(value):
    #Using the value, execute a sql query that will take the current date and time, (security/nonsecurity via algorithm), and value and insert into the table
    conn = sqlite3.connect(r'WebPages/facilities.db')
    cursor = conn.cursor()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%y %I:%M %p")
    security = False
    if "Badge:" in value:
        security = True
    
    query = ('''
            INSERT INTO walkin_tracker (date,security,reason)
             VALUES (?,?,?)
''')
    
    cursor.execute(query, (date_time, security, value))

    conn.commit()
    conn.close()

