import csv, os, sqlite3
from datetime import *

def process(filename):
    with open(filename, mode = "r",encoding='utf8') as file:
        woFile = csv.reader(file)
        totalWO = 0
        totalNonPM = 0
        totalPM = 0
        totalCurrentWO = 0
        totalCurrentPM = 0
        totalPastDueWO = 0
        custodialRequestCounter = 0
        custodial30days = 0
        custodial7days = 0
        
        totalCurrentNonPM = 0
        totalPastNonPM = 0

        totalCurrentPM = 0
        totalPastPM = 0

        today = date.today()
        formattedToday = today.strftime("%Y-%m-%d %H:%M").strip()
        formattedToday = datetime.strptime(formattedToday, "%Y-%m-%d %H:%M").date()
        previous_line = None

        for lines in woFile:
                if previous_line is not None and previous_line == lines[0]:
                    continue
                else:
                    previous_line = lines[0]
                    try:
                        if lines[4]:
                            completetionDue = datetime.strptime(lines[4], "%Y-%m-%d %H:%M").date()
                        if lines[10]:
                            createdDate = datetime.strptime(lines[10], "%Y-%m-%d %H:%M").date()
                    except ValueError:
                        print(f"Cannot parse date: {lines[4]} or {lines[10]}")
                        continue

                    if  "ASSIGNED*" in lines[3].upper():    # This is checking to see if its assigned aka Current                           
                        totalWO += 1       # Increments ALL work orders
                        
                        if "FALSE" in lines[11].upper():
                            totalNonPM +=1

                        if "TRUE" in lines[11].upper():
                            totalPM +=1

                        if formattedToday < completetionDue:                                       
                            totalCurrentWO +=1    

                        if formattedToday > completetionDue:                                       
                            totalPastDueWO +=1    

                        if formattedToday < completetionDue and "FALSE" in lines[11].upper():
                            totalCurrentNonPM +=1
                        
                        if formattedToday > completetionDue and "FALSE" in lines[11].upper():
                            totalPastNonPM +=1

                        if formattedToday < completetionDue and "TRUE" in lines[11].upper():
                            totalCurrentPM +=1
                        
                        if formattedToday > completetionDue and "TRUE" in lines[11].upper():
                            totalPastPM +=1


                    if  "Custodial Request" in lines[9]:                    #Checks if its a custodial request
                        custodialRequestCounter +=1
                        if lines[10]:
                            delta = today - createdDate                     #Checks if it was within last 30 days
                            if delta.days <=30:
                                custodial30days +=1
                            if delta.days <= 7:
                                custodial7days +=1
        file.close()
        os.remove(filename)


        
        return [formattedToday,totalWO,totalCurrentWO,totalPastDueWO,custodialRequestCounter,totalNonPM,totalCurrentNonPM,totalPastNonPM,totalPM,totalCurrentPM,totalPastPM,custodial7days,custodial30days]
    