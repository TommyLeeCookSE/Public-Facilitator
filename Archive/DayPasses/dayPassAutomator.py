#Scan a badge, will retrieve the badge ID from the dict and the number, and place in a new dict which will be saved into the final csv to be copy pasted into the form
from functions import *
import csv 

additionToDayPassFile = {}
dayPassDict = {}
dayPassFinalDict = {}
badgeQuantitiesArray = []
batches = 0
batchCounter = 0
batchSize = 0
counter = 0
largestKey = 0
largestValue = 0


with open('DayPasses/dayPassFile.csv', mode = "r") as file: #Opens the dayPassFile which stores all our daypasses
    dayPassFile = csv.reader(file)
    for lines in dayPassFile:
        importDict(dayPassDict,lines)
        if largestKey < int(lines[1]):
            largestKey = int(lines[1])
        if largestValue < int(lines[0]):
            largestValue = int(lines[0])

    


print("Enter the amount of batches you want to print: ")    #Allows the user to enter the # of batches to print,      
while True:                                                 
    try:
        if batches > 0:
            print(f"{batches} batches will be printed.")
            break      
        else:  
            batches = (intChecker(input()))
    except: 
        batches = (intChecker(input()))                                            



while batchCounter < batches:                               #Allows the user to enter the endpoints of the batches, 3 batches of 4,10,10 would be endpoints 4,14,24
        print("Enter the batch sizes: ")
        batchSize += intChecker(input())
        badgeQuantitiesArray.append(batchSize)
        print("Badge batches: ")
        print(badgeQuantitiesArray)
        batchCounter+=1



while len(dayPassFinalDict) < badgeQuantitiesArray[-1]:     #Scans badges and pulls the data from the original dict into the final dict
    print("Scan a Badge:")
    badgeId = intChecker(input())
    if badgeId in dayPassDict:
        appendToDict(badgeId,dayPassDict,dayPassFinalDict,badgeId)
    else:
        print("Not currently in Dict, Please enter the ID number:") #Allows not entered badges to be entered here.
        badgeNumber = intChecker(input())
        while True:
            if badgeNumber < largestKey:
                additionToDayPassFile[badgeId] = badgeNumber
                appendToDict(badgeId,dayPassDict,dayPassFinalDict,badgeNumber)
                break
            else:
                print(str(badgeNumber)+ " Value must be less than: " + str(largestKey))            #If the key is greater than this, enter the values via the dayPassEntry.
                badgeNumber = intChecker(input())
    counter = batchChecker(counter, badgeQuantitiesArray, dayPassFinalDict)



with open('DayPasses\dayPassFileFinal.csv', mode = "w", newline = '') as file:     #Writes the information to the daypassFinal file
    writer = csv.writer(file, delimiter='\t')
    i = 0
    for key, value in dayPassFinalDict.items():
        for batch in badgeQuantitiesArray:
            if int(batch) == i:
                writer.writerow('')
        writer.writerow([value, key])
        i += 1

with open('DayPasses/dayPassFile.csv', mode = 'a', newline = '') as file:           #Writes the missing badges into the badge file.
    writer = csv.writer(file)
    for key,value in additionToDayPassFile.items():
        writer.writerow([key,value])
    
print("Writing complete, operation finished.")
