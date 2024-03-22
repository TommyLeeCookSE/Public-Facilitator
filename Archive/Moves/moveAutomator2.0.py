import csv
moveDate = fname = lname = employeeId = oldBuilding = oldCube = newBuilding = newCube = boxes = "EMPTY"
moveDate = month = day = year = "EMPTY"
finalList = []
#TODO Have it pick the building name from the first char in the cubicle num
#TODO Feburary seems to be broken
def buildingFormatter(buildingName):
    if "Pod 6" in buildingName or "Pod 7" in buildingName:
        return "BIG 6-7"
    elif "Pod 1" in buildingName or "Pod 2" in buildingName or "Pod 3" in buildingName or "Pod 4" in buildingName or "Pod 5" in buildingName:
        return "BIG 1-5"
    elif "1901" in buildingName:
        return "1901"
    elif "1921" in buildingName:
        return "1921"
    elif "LINC" in buildingName:
        return "LINC"
    elif "Community" in buildingName:
        return "COM"
    elif "Daimler" in buildingName:
        return "Daimler"
    elif "ERC" in buildingName:
        return "ERC"
    elif "HVC" in buildingName:
        return "HVC"
    elif "LFSX" in buildingName:
        return "LFSX"
    elif "LFS" in buildingName:
        return "LFS"
    elif "MLE" in buildingName:
        return "MLE"
    elif "PRT" in buildingName:
        return "PRT"
    elif "T&D" in buildingName:
        return "T&D"
    elif "Other" in buildingName:
        return '\t'
    else:
        return "WORK IN PROGRESS" 
#TODO This needs to have variables that store the slice information so we don't have to search multiple times per string
def moveDateFormatter(sentance):
    # print(sentance)
    moveDate = sentance[sentance.find("\t"):].strip()
    # print(moveDate)
    month = moveDate[moveDate.find(" "):moveDate.find(' ',moveDate.find(' ',moveDate.find(' ')+1))].strip()
    # print(month)
    day = moveDate[moveDate.find(" ",moveDate.find(' ')+1):moveDate.find(",",moveDate.find(',')+1)].strip()
    # print(day)
    year = moveDate[moveDate.find(",",moveDate.find(',')+1)+1:].strip()
    # print(year)
    
    if month == "January":
        month = "01"
    elif month == "February":
        month = "02"
    elif month == "March":
        month = "03"
    elif month == "April":
        month = "0/"
    elif month == "May":
        month = "05"
    elif month == "June":
        month = "06"
    elif month == "July":
        month = "07"
    elif month == "August":
        month = "08"
    elif month == "September":
        month = "09"
    elif month == "October":
        month = "10"
    elif month == "November":
        month = "11"
    elif month == "December":
        month = "12"
    else:
        month = "ERROR IN MONTH "
    # print(month)

    moveDate = month + "/" + day + "/" + year
    
    # print(moveDate)
    return moveDate


#Clears the writeFile so that the following script can append to an empty file
with open('Moves\writeFile.csv', 'w') as file:
  overWriter = csv.writer(file)

with open("Moves/readFile.csv", 'r') as file:
    reader = csv.reader(file, delimiter = '\n')
    for lines in reader:
        for sentance in lines:
            
            if "Preferred" in sentance:                 #Finds the move date
                moveDate = moveDateFormatter(sentance) 
            
            elif "Name of Person Moving" in sentance:   #Finds the first and last name, middle name is lumped with last name
                name = sentance[sentance.find("\t"):].strip()
                fname = name[:name.find(' ')].title()
                lname = name[name.find(' '):].strip().title()

            elif "If Shared" in sentance:
                newSentance = sentance[sentance.find("\t"):].strip()
                if newSentance != "":
                    print(newSentance)
                    fname = name
                    lname = newSentance
        
            elif "Employee ID" in sentance:             #Finds the employee ID
                employeeId = sentance[sentance.find('\t'):].strip()
            
            elif "Old Building" in sentance:            #Finds the old building name
                oldBuilding = sentance[sentance.find('\t'):].strip()
                oldBuilding = buildingFormatter(oldBuilding)         
            elif "Old Cube/Office" in sentance:         #Finds the old building number
                oldCube = sentance[sentance.find('\t'):].strip()
            
            elif "New Building" in sentance:            #Finds the new building name
                newBuilding = sentance[sentance.find("\t"):].strip()
                newBuilding = buildingFormatter(newBuilding)            
            
            elif "New Cube" in sentance:                #Finds the new building number
                newCube = sentance[sentance.find('\t'):].strip()
            
            elif "please specify how many" in sentance: #Finds the number of boxes
                boxes = sentance[sentance.find('\t'):].strip()
                try:
                    if int(boxes) >= 0:
                        boxes = boxes + " boxes and labels"
                except:
                    boxes = "0 boxes just labels"

            elif "Today's Date" in sentance: #Appends the list after reaching end of the current move request, restarts loop and continues till done
                finalList = [moveDate, fname, lname, oldBuilding, oldCube, newBuilding, newCube, employeeId, '\t', boxes]
                print(finalList)
                with open('Moves\writeFile.csv', 'a', newline = '') as file:
                    writer = csv.writer(file, delimiter = '\t',)
                    writer.writerow(finalList)
                finalList = []

