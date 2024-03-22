#Takes input of badges and stores the badge id as the key with the badge number as the value
#When badge is scanned, the value is returend in the left column, and the key in the right column
#Purpose is so users can scan badges in whatever qts they desire, copy the exported csv into the proper template, and print the file without having to manually type.
import csv
daypassDict = {}


with open('DayPasses/dayPassFile.csv', mode = "r") as file:
    dayPassFile = csv.reader(file)

    for lines in dayPassFile:
        daypassDict[lines[0]] = lines[1]



while True: 
    print("Scan the badge: ")
    badgeID = input()
    if badgeID == "done":
        break
    
    print("Type the badge number:")
    badgeNumber = input()
    if badgeNumber == "done":
        break
    
    daypassDict[badgeID] = badgeNumber

print(daypassDict)

with open('DayPasses\dayPassFile.csv', 'w', newline = '') as csvfile:
    # creating a csv dict writer object 
    writer = csv.writer(csvfile) 
        
        
    # writing data rows 
    for key, value in daypassDict.items():
        writer.writerow([key, value])