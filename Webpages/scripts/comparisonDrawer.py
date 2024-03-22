import sqlite3

def pullFromDatabase():

    conn = sqlite3.connect(r'C:\Users\Tommy_Cook\OneDrive - Edwards Lifesciences\Documents\Scripts\Facilitator\WebPages\facilities.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM biweekly_centerstone_report")

    rows = cursor.fetchall()

    conn.close()
    return(reversed(rows))


## Function that takes the 2 dates, selects everything from the db where the 2 dates =
## Have the 2 dates in a list and then subtract the first from the second on everything but the date and have that as the third item in the row
##Return the list to main

def pullAndCompareDates(listOfDates):
    
    finalListOfDates = []
    conn = sqlite3.connect(r'C:\Users\Tommy_Cook\OneDrive - Edwards Lifesciences\Documents\Scripts\Facilitator\WebPages\facilities.db')
    cursor = conn.cursor()

    for item in listOfDates:
        cursor.execute("SELECT * FROM biweekly_centerstone_report WHERE date = ?",(item,))
        finalListOfDates+= [item for item in cursor.fetchall()]
    
    temp_list = []
    for x in range(1, len(finalListOfDates[0])):
        temp_list.append(finalListOfDates[0][x] - finalListOfDates[1][x])
    temp_list.insert(0,"Difference")
    finalListOfDates.append(temp_list)
    conn.close()
    
    return finalListOfDates