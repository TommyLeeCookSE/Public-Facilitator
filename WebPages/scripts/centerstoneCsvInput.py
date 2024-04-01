import pandas as pd
import sqlite3, os
from dateutil import parser

#Process every line in this file, each line will be edited and then comitted, no saving to list or anything, we may split into list in line to manipulate
def saveToWorkOrderTable(filename):

    #Create variables to store the data coming in from the file
    woNum = laborName = requestedBy = woStatus = completionDue = completionDate = building = locationNumber = description = workOrderType = isPm = creationDate = ""
   
   #Open the file
    df = pd.read_csv(filename)
    conn = sqlite3.connect(r'WebPages/facilities.db')
    cursor = conn.cursor()

    #Read the file line by lane
    for index, row in df.iterrows():
        creation_date = parser.parse(row['Created Date']).strftime('%Y-%m-%d')
        query = '''
        INSERT OR REPLACE INTO work_order_table
        (wo_num, labor_name, requested_by, status, completion_due, completion_date,
        building, location_number, description, work_order_type, is_pm, creation_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

        parameters = (
        row['Work Order Number'], row['Labor Name'], row['Requested By'], row['Status'], row['Completion Due'], 
        row['Completion Date'], row['Building'], row['Location Number'], row['Description'], 
        row['Work Order Name'], row['Is For MaintenanceProgram'], creation_date)

        cursor.execute(query, parameters)

    #Updates date format for future comparisson
    cursor.execute("UPDATE work_order_table SET completion_due = strftime('%Y-%m-%d', completion_due)")
    cursor.execute("UPDATE work_order_table SET completion_date = strftime('%Y-%m-%d', completion_date)")
    cursor.execute("UPDATE work_order_table SET creation_date = strftime('%Y-%m-%d', creation_date)")
    
    #Commit the variables to the database
    conn.commit()
    #close file
    conn.close()
    #delete file
    os.remove(filename)
    
    print("Files Comitted")
    
