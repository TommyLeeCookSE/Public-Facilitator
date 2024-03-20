import pandas as pd
import sqlite3, os
def tractionGuestUpload(filename):
    tractionGuestRawDataDF = pd.read_csv(filename)
    employeeName = ""
    cardID = ""
    employeeID = ""
    signinDate = ""

    conn = sqlite3.connect(r'C:\Users\Tommy_Cook\OneDrive - Edwards Lifesciences\Documents\Scripts\Facilitator\WebPages\facilities.db') #Connected to daypass db
    connCursor = conn.cursor()

    for index, row in tractionGuestRawDataDF.iterrows():
        if pd.notnull(row['Employee ID']) and pd.notnull(row['Day Pass Badge Number']) and pd.notnull(row['Please hand the iPad back to the guard to confirm your details']):
            employeeName = row['Please hand the iPad back to the guard to confirm your details']
            cardID = int(row['Day Pass Badge Number'])
            employeeID = row['Employee ID']
            signinDate = row['Signin Date']
            connCursor.execute("UPDATE daypasses SET last_used_by_eid = ? WHERE card_id = ?", (employeeID, cardID))
            connCursor.execute("UPDATE daypasses SET last_used_by_name = ? WHERE card_id = ?", (employeeName, cardID))
            connCursor.execute("UPDATE daypasses SET last_used_date = ? WHERE card_id = ?", (signinDate, cardID))
    conn.commit()
    conn.close()

    os.remove(filename)
    

    