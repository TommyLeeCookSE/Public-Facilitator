import pandas as pd
import sqlite3, os

def tractionGuestUpload(filename):
    tractionGuestRawDataDF = pd.read_csv(filename)
    update_eid_query = "UPDATE daypasses SET last_used_by_eid = ? WHERE card_id = ?"
    update_name_query = "UPDATE daypasses SET last_used_by_name = ? WHERE card_id = ?"
    update_date_query = "UPDATE daypasses SET last_used_date = ? WHERE card_id = ?"
    
    conn = sqlite3.connect(r'C:\Users\Tommy_Cook\OneDrive - Edwards Lifesciences\Documents\Scripts\Facilitator\WebPages\facilities.db',timeout=300) #Connected to daypass db
    connCursor = conn.cursor()

    for index, row in tractionGuestRawDataDF.iterrows():
        if pd.notnull(row['Employee ID']) and pd.notnull(row['Day Pass Badge Number']) and pd.notnull(row['Please hand the iPad back to the guard to confirm your details']):
            employeeName = row['Please hand the iPad back to the guard to confirm your details']
            try:
                cardID = int(row['Day Pass Badge Number'])
                employeeID = row['Employee ID']
                signinDate = row['Signin Date']
                connCursor.execute(update_eid_query, (employeeID, cardID))
                connCursor.execute(update_name_query, (employeeName, cardID))
                connCursor.execute(update_date_query, (signinDate, cardID))
            except:
                print(f"FAILED: {employeeName}")

            
            
    conn.commit()
    conn.close()

    os.remove(filename)
    

    