import sqlite3

def pullFromDatabase():

    conn = sqlite3.connect(r'C:\Users\Tommy_Cook\OneDrive - Edwards Lifesciences\Documents\Scripts\Facilitator\WebPages\facilities.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM biweekly_centerstone_report")

    rows = cursor.fetchall()

    conn.close()
    return(reversed(rows))