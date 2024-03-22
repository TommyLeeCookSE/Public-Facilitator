#Then figure out if the name is 1 person (1 space) 1 person with multiple names (2+ spaces) 2 people (& symbol) or blank ("blank")
#Then use .title() on them to properly uppercase them, strip() them and arrange them in the proper order, fname, lnmae, cubeNumber and export to namePlateEntryCompleted.csv

import csv
namePlateDictList = []
fieldnames = ["firstName", "lastName", "buildingName"]
def buildingNameFirst(words):
    if words[0].isnumeric() or words[1].isnumeric() or words[2].isnumeric():
        # print(f"Building name first: {words}")
        return True

def andChecker(words):
    if '&' in words:
        return True
    else:
        return False

def hypenCorrecter(words):
    if words.find("–"):
        return words.replace('–','-')
    
def multipleNameChecker(words):
    buildingNameRemoved = words[words.find("- "):].strip()
    if buildingNameRemoved.count(' ') > 2:
        return True

def buildingNameReturner(words):
    if buildingNameFirst(words): #If true than the building name is first
        return words[:words.find(' ')].replace('-','').strip().title()
    else:
        return words[words.find('-')+1:].replace('-','').strip().title()
    # return words[:words.find(' ')].strip()

def fnameReturner(words):
    if buildingNameFirst(words): #If true than the building name is first
        if "Blank" in words.title():
            return "Blank"
        elif andChecker(words): #Checks if this is a shared nameplate
            return words[words.find(' ',words.find('-')):words.find('&')].strip().title()
        elif multipleNameChecker(words):  #Checks if they have more than first and last, places the middle in the last name
            return words[words.find('-')+1:words.find(' ',words.find(' ')+4)].strip().title()
        else: #Returns a normal first name if they only have a first and last
            return words[words.find('-')+1:words.find(' ',words.find("-")+2)].strip().title()
    else:#Startings with first name not building name
        return words[:words.find(' ')].title()
        
def lnameReturner(words):
    if buildingNameFirst(words): #If true than the building name is first
        if fname == "Blank":
            return "Blank"
        elif andChecker(words):
            return words[words.find('&')+1:].strip().title()
        elif multipleNameChecker(words):
            return words[words.find(' ',words.find("-")+2):].strip().title()
        else:
            return words[words.find(' ',words.find('-')+2):].strip().title()
    else:#Startings with first name not building name
        return words[words.find(' '):words.find('-')].strip().title()



with open("Nameplates/nameplateEntry.csv",'r',encoding='utf8') as file:
    fileReader = csv.reader(file, delimiter = '\n')
    for lines in fileReader:
        lines[0] = hypenCorrecter(lines[0])
        fname = fnameReturner(lines[0])
        # print(f"FirstName: {fname} FROM: {lines[0]}")
        lname = lnameReturner(lines[0])
        # print(f"LastName: {lname} FROM: {lines[0]}")
        buildingName = buildingNameReturner(lines[0])
        # print(f"Building: {buildingName} FROM: {lines[0]}")
        namePlateDictList.append({'firstName': fname, "lastName" : lname, "buildingName":buildingName})
                
# print(namePlateDictList)
with open('Nameplates/namePlateFinal.csv','w', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames,delimiter = '\t')

    writer.writeheader()

    writer.writerows(namePlateDictList)