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
    security_count = 0
    non_security_count = 0
    list_of_objects = []
    query = ('''SELECT * FROM walkin_tracker''')
    cursor.execute(query)
    
    rows = cursor.fetchall()

    for item in rows:
        list_of_objects.append(Walkin(item[0],item[1],item[2]))
        if item[1] == 1:
            security_count += 1
        else:
             non_security_count +=1

    conn.close()

    return list_of_objects[::-1], [security_count, non_security_count]

def process_walkin(value):
    conn = sqlite3.connect(r'WebPages/facilities.db')
    cursor = conn.cursor()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%y %I:%M %p")
    security = 0
    if "Badge" in value:
        security = 1
    
    query = ('''
            INSERT INTO walkin_tracker (date,security,reason)
             VALUES (?,?,?)
''')
    
    cursor.execute(query, (date_time, security, value))

    conn.commit()
    conn.close()

