import csv
from datetime import *

filename = "c:/Users/Tommy_Cook/Downloads/Export (1).csv"
# Return the number of Current Wo, Current WO not including PMs, Total Past Due, and Total Past Due, Total Past Due Excluding PMS
with open(filename, mode = "r",encoding='utf8') as file:
    woFile = csv.reader(file)
    currentWOCounter = 0
    currentWoCounterNoPM = 0
    pastDueWOCounter = 0
    pastDueWOCounterNoPm = 0
    today = date.today()
    formattedDate = today.strftime("%Y-%m-%d %H:%M").strip()
    previous_line = None

    for lines in woFile:
            if previous_line is not None and previous_line == lines[0]:
                # print(f"The first element in the current line is the same as in the previous line {lines[0]} and {previous_line}")
                continue
            else:
                # print(f"The first element in the current line is not the same as in the previous line {lines[0]} and {previous_line}")
                previous_line = lines[0]
                if lines[3] == "":
                    currentWOCounter += 1
                    continue
                if lines[4] == "Assigned*":                                             #Gets all assigned WOs 
                    currentWOCounter += 1
                    if formattedDate > lines[3]:                                        #Gets all assigned past due WOs 
                        pastDueWOCounter +=1
                if lines[4] == "Assigned*" and lines[6] != "Preventative Maintenance":  #Gets all non pm wos
                    currentWoCounterNoPM +=1
                    if formattedDate > lines[3]:                                        #Gets all past due non pm wos
                        pastDueWOCounterNoPm +=1
            

    print(f"All Current WO: {currentWOCounter}")
    print(f"Current WO not including PMS: {currentWoCounterNoPM}")
    print(f"Past Due WO including PMS: {pastDueWOCounter}")
    print(f"Past Due WO not including PMS: {pastDueWOCounterNoPm}")
