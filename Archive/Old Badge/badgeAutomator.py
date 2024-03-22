def badgeFileReader():
#Variables------------------------------------------------------------------------------------------------------------------------------
  
  dataArray = []
  dataDict = {
    "Last Name":"",
    "First Name":"",
    "EID":"",
    "Title":"",
    "Department":"",
    "Location":"",
    "Manager":""
  }

#Helper Methods----------------------------------------------------------------------------------------------------------------------------------
  def tempStringHelper(index):
    tempString = dataArray[index] + dataArray[index+1] + dataArray[index+2] + dataArray[index+3]
    return tempString

#Main--------------------------------------------------------------------------------------------------------------  
  file = open("Archive\Old Badge/readFromBadgeFile.txt", "r")
  for line in file:
    if line != "\n":
      dataArray.append(line.strip())
  file.close()
  
  file = open("Archive\Old Badge/finalizedBadges.csv", "w")
  file.write("Last Name,First Name,EID,Title,Department,Location,Manager\n")

  
  for i in range(len(dataArray)):
    index = i
    #Extracting the Last Name----------------------------------------------------------------------------------------------------------
    if "Last Name" in dataArray[i]:
      tempString = tempStringHelper(index)
      lnameIndex = tempString.index("Last Name:")
      fnameIndex = tempString.index("First Name:")
      dataDict["Last Name"]= tempString[lnameIndex+10:fnameIndex].strip().upper()
    
    #Extracing the First Name---------------------------------------------------------------------------------------------------------
    if "First Name" in dataArray[i]:
      tempString = tempStringHelper(index)
      fnameIndex = tempString.index("First Name:")
      edwardsIndex = tempString.index("Edwards ID #")
      dataDict["First Name"] = tempString[fnameIndex+11:edwardsIndex].strip().upper()
    
    #Extracting the Employee ID--------------------------------------------------------------------------------------------------------
    if "Edwards ID #" in dataArray[i]:
      #This takes the line the EIN header appears on as well as the following line the EIN is on and extracts the substring that is the EIN.
      tempString = tempStringHelper(index)
      idIndex = tempString.index("ID#:")
      dataDict["EID"] = tempString[idIndex+4:idIndex+10].strip().upper()
    
    #Extracting the Job Title--------------------------------------------------------------------------------------------------------
    if "Job Title:" in dataArray[i]:
      tempString = tempStringHelper(index)
      titleIndex = tempString.index("Job Title:")
      try: #Some forms use Building some use Bldg
        bldgIndex = tempString.index("Bldg:")
      except:
        bldgIndex = tempString.index("Building:")
      dataDict["Title"]= tempString[titleIndex+10:bldgIndex].strip().upper()
      dataDict["Title"] = dataDict["Title"].replace(","," ")
      
    #Extracting the Department--------------------------------------------------------------------------------------------------------
    if "Dept Name: " in dataArray[i]:
      tempString = tempStringHelper(index)
      dnameIndex = tempString.index("Dept Name:")
      rIndex = tempString.index("Reason")
      dataDict["Department"] = tempString[dnameIndex+10:rIndex].strip().upper()
    
    #Extracting the Location--------------------------------------------------------------------------------------------------------
    if "Bldg: " in dataArray[i] or "Building:" in dataArray[i]:
      tempString = tempStringHelper(index)
      bIndex = tempString.index("g:")
      cIndex = tempString.index("Cube")
      dataDict["Location"] = tempString[bIndex+3:cIndex].strip().upper()
    
    #Extracting the Manager Name--------------------------------------------------------------------------------------------------------
    if "Manager or Supervisor Name:" in dataArray[i]:
      tempString = tempStringHelper(index)
      nameIndex = tempString.index("e:")
      newIndex = tempString.index("New Badge Number")
      dataDict["Manager"] = tempString[nameIndex+2:newIndex].strip().upper()
    
    #Saving to file---------------------------------------------------------------------------------------------------------------------
    if "Check box if employee requires Jamboree Parking or After Hours Access" in dataArray[i]:
      file.write(f'{dataDict["Last Name"]},{dataDict["First Name"]},{dataDict["EID"]},{dataDict["Title"]},{dataDict["Department"]},{dataDict["Location"]},{dataDict["Manager"]}\n')
      # print(dataDict["Last Name"])
      # print(dataDict["First Name"])
      # print(dataDict["EID"])
      # print(dataDict["Title"])
      # print(dataDict["Department"])
      # print(dataDict["Location"])
      # print(dataDict["Manager"]+"\n")
  file.close()

badgeFileReader()