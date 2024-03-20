#Take a csv file which is a copy paste of the move list. Scan each line for the required key words, paste in a row so it can be copy pasted into excel.
#------------------------------------------------------------------------------------------------------------------------------------------------------
import csv

otherBuildingCount = 1 #Used to differentiate between Old and New building 1 = Old 2 = New, as seen in the move request form
refNum = "\t"
data = []
validData = []
fullList = []
header = [
  "First Name", "Last Name", "Employee ID", "From Bldg", "Office/Cube",
  "To Building", "Office/Cube", "Reference #", "Comments"
]
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Writes a header for understanding of format, also overwrites previous file for ease of use.
with open('Moves/writeFile.csv', 'w') as file:
  writer = csv.writer(file)
  writer.writerow(header)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Reads the file by line and saves it into an array, import has lots of whitespace, original used to remove the whitespace before appending to array.
with open('Moves/readFile.csv', 'r') as file:
  csvFile = csv.reader(file, delimiter='\n')
  for lines in csvFile:
    for word in lines:
      if word != '\n':
        data.append(lines)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Looks through the array and only selects the useful information that we need adding it to a new array, could likely just use the original array. Used at first because didn't know we couse use \n or \t as a way to check before appending. Not fixing at the moment due to the script working fine.
for item in data:
  for word in item:
    if word.__contains__("Name of Person Moving:") or word.__contains__(
        "Employee ID:"
    ) or word.__contains__("Old Building:") or word.__contains__(
        "Old Cube/Office #:") or word.__contains__("New Building:") or word.__contains__("New Cube/Office #:") or word.__contains__("If \"Yes,\" please specify how many:") or word.__contains__("Today's Date:") or word.__contains__("Preferred Move Date:") or word.__contains__("If \"Other,\" specify here:"):
      validData.append(item)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Looks through the new array, verifies the information we are looking for, then using slices selects the information we need to be put into a csv
for item in validData:
  for word in item:
    if word.__contains__("Name of Person Moving:"):
      #TO DO: Need to add functionality to allow for 2 names if the desk is shared
      #TO DO: Need to add functionality to allow for people with two last names
      name = word[23:-1]
      charIndex = 0
      for char in name:
        if char.isspace() == True:
          fname = name[0:charIndex].strip()
          lname = name[charIndex:].strip()
        else:
          charIndex += 1
   
    elif word.__contains__("Employee ID:"):
      eID = word[13:].strip()

    elif word.__contains__("Old Building:"):
      oldBuilding = word[14:].strip()
    
    elif word.__contains__("If \"Other,\" specify here:"):
      placeholder = word[27:]
      if placeholder == " ":
        otherBuildingCount += 1
        continue
      else:
        if otherBuildingCount == 1:
          oldBuilding = word[27:].strip()
          otherBuildingCount += 1
        elif otherBuildingCount == 2:
          newBuilding = word[27:].strip()
          otherBuildingCount = 1
    
    elif word.__contains__("Old Cube/Office #:"):
      oldCube = word[19:].strip()
      
    elif word.__contains__("New Building:"):
      newBuilding = word[14:].strip()
    elif word.__contains__("New Cube/Office #:"):
      newCube = word[19:].strip()

    elif word.__contains__("If \"Yes,\" please specify how many:"):
      boxes = word[36:].strip()
      
    elif word.__contains__("Preferred Move Date:"):
      moveDate = word[20:].strip()
#------------------------------------------------------------------------------------------------------------------------------------------------------ 
    elif word.__contains__("Today's Date:"):
      #Uses Today's Date as it is the last line in a request form
      #Formats the building name into the correct pasteable for the google sheet.
      if oldBuilding.__contains__("Pod 1") or oldBuilding.__contains__("Pod 2") or oldBuilding.__contains__("Pod 3") or oldBuilding.__contains__("Pod 4") or oldBuilding.__contains__("Pod 5") or oldBuilding.__contains__("BIG1") or oldBuilding.__contains__("BIG2") or oldBuilding.__contains__("BIG3") or oldBuilding.__contains__("BIG4") or oldBuilding.__contains__("BIG5"):
        oldBuilding = "BIG 1-5"
      
      elif oldBuilding.__contains__("Pod 6") or oldBuilding.__contains__("Pod 7") or oldBuilding.__contains__("BIG6") or oldBuilding.__contains__("BIG7"):
        oldBuilding = "BIG 6-7"
      
      elif oldBuilding.__contains__("Other"):
        if oldCube.__contains__("B1") or oldCube.__contains__("B2") or oldCube.__contains__("B3") or oldCube.__contains__("B4") or oldCube.__contains__("B5"):
          oldBuilding = "BIG 1-5"
        
        elif oldCube.__contains__("B6") or oldCube.__contains__("B7"):
          oldBuilding = "BIG 1-6"
       
      elif oldBuilding.__contains__("LINC"):
        oldBuilding ="LINC"
      elif oldBuilding.__contains__("LFSX"):
        oldBuilding="LFSX"
      elif oldBuilding.__contains__("LFS"):
        oldBuilding="LFS"
      elif oldBuilding.__contains__("MLE"):
        oldBuilding="MLE"
      elif oldBuilding.__contains__("T&D"):
        oldBuilding="T&D"

        
      if newBuilding.__contains__("Pod 1") or newBuilding.__contains__("Pod 2") or newBuilding.__contains__("Pod 3") or newBuilding.__contains__("Pod 4") or newBuilding.__contains__("Pod 5") or newBuilding.__contains__("BIG1") or newBuilding.__contains__("BIG2") or newBuilding.__contains__("BIG3") or newBuilding.__contains__("BIG4") or newBuilding.__contains__("BIG5"):
        newBuilding = "BIG 1-5"
      
      elif newBuilding.__contains__("Pod 6") or newBuilding.__contains__("Pod 7") or newBuilding.__contains__("BIG6") or newBuilding.__contains__("BIG7"):
        newBuilding = "BIG 6-7"
        
      elif newBuilding.__contains__("Other"):
        print("New Building Contains Other")
        if newCube.__contains__("B1") or newCube.__contains__("B2") or newCube.__contains__("B3") or newCube.__contains__("B4") or oldCube.__contains__("B5"):
          newBuilding = "BIG 1-5"
        
        elif newCube.__contains__("B6") or newCube.__contains__("B7"):
          newBuilding = "BIG 1-6"

      elif newBuilding.__contains__("LINC"):
        newBuilding ="LINC"
      elif newBuilding.__contains__("LFSX"):
        newBuilding="LFSX"
      elif newBuilding.__contains__("LFS"):
        newBuilding="LFS"
      elif newBuilding.__contains__("MLE"):
        newBuilding="MLE"
      elif newBuilding.__contains__("T&D"):
        newBuilding="T&D"
#------------------------------------------------------------------------------------------------------------------------------------------------------ #Appends the date to the final list that we will export to the csv in pasteable format.      
      fullList = [
        fname, lname, eID, oldBuilding, oldCube, newBuilding, newCube, refNum,
        boxes, moveDate
      ]
#------------------------------------------------------------------------------------------------------------------------------------------------------ #Writes to the .csv and then reset the fullList (though technically because we arent appending but setting the fullList to the values, there is no need to erase the list) so we can do unlimited amounts of moves at once.      
      print(f'First Name: {fname}\nLast Name: {lname}\nEmployee ID: {eID}\nOld Building: {oldBuilding}\nOld Office/Cube: {oldCube}\nNew Building: {newBuilding}\nNew Office\Cube: {newCube}\nRef Num: {refNum}\nBoxes: {boxes}\nMove Date: {moveDate}\n')
      with open('Moves/writeFile.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(fullList)
      fullList = []
    