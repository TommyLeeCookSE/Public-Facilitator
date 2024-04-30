from datetime import datetime
def process(data):
        processingData = []
        processedData = []
        results = []
        date = fname = lname = fromBuilding = fromOfficeCube = toBuilding = toOfficeCube = eid = refnum = comments = name = ""
        processingData = data.split("\n")
        for line in (processingData):
                if "Name of Person Moving" in line:
                        name,fname,lname = nameParser(line,name)

                elif "Shared - please add" in line and line.strip()[-1] != ":": 
                        name,fname, lname = nameParser(line, name)
                
                elif "Old Cube/Office #" in line:
                        fromOfficeCube = cubeParser(line)
                        fromBuilding = buildingParser(fromOfficeCube)
                
                elif "New Cube/Office #" in line:
                        toOfficeCube = cubeParser(line)
                        toBuilding = buildingParser(toOfficeCube)
                elif "Employee ID" in line:
                        eid = employeeIDParser(line)
                        processedData = [date, fname, lname, fromBuilding, fromOfficeCube, toBuilding, toOfficeCube, eid, refnum, comments]
                        results.append(processedData)
                        processedData = []
                elif "Preferred Move Date" in line:
                        date = moveDateParser(line)
                elif "please specify how many" in line:
                        comments = commentsParser(line)
                # elif "Today's Date" in line:
                #         processedData = [date, fname, lname, fromBuilding, fromOfficeCube, toBuilding, toOfficeCube, eid, refnum, comments]
                #         results.append(processedData)
                #         processedData = []
        return results
                        


def nameParser(line,name):
        if "Name of Person Moving" in line:
                start = line.find("\t")
                name = line[start:].strip().title()
                fname,lname = nameSeperator(name)
                return [name, fname,lname] 
        
        elif "If Shared" in line:
                start = line.find("\t")
                lname = line[start:].strip().title()
                fname = name.strip().title()
                return name,fname,lname
        
        
                
def nameSeperator(name):
        fname = name[:name.find(" ")].strip().title()
        lname = name[name.find(" "):].strip().title()
        return [fname,lname]
        
def cubeParser(line):
        start = line.find("\t")
        cube = line[start:].strip().title().upper()
        buildingParser(cube)
        return cube

def buildingParser(cube):
        buildingLetter = buildingLetterFinder(cube)
        building = buildingFinder(buildingLetter)
        return building


def buildingLetterFinder(cube):
        #TODO: Add a validator that checks the building letters as well as some people forget to include the letter and that makes it look like Daimler
        stringBuilder = ""
        for letter in cube:
                if cube[0] == "B":
                        return f"{cube[0]}{cube[1]}"
                elif letter.isdigit():
                        return stringBuilder
                elif letter.isalpha():
                        stringBuilder += letter


def buildingFinder(letters):
        if letters == "A":
                return "1901"
        elif letters == "AA":
                return "1921"
        elif letters == "C":
                return "COM"
        elif letters =="":
                return "Daimler"
        elif letters == "B1" or letters == "B2" or letters == "B3" or letters == "B4" or letters == "B5":
                return "BIG 1-5"
        elif letters == "B6" or letters == "B7":
                return "BIG 6-7"
        elif letters == "E":
                return "ERC"
        elif letters == "H":
                return "HVC"
        elif letters == "LS":
                return "LFS"
        elif letters == "X":
                return "LFSX"
        elif letters == "L":
                return "LINC"
        elif letters == "M":
                return "MLE"
        elif letters == "P":
                return "PRT"
        elif letters == "T":
                return "T&D"
        elif letters == "MIC":
                return "MIC"
        else:
                return "Not in List"

def employeeIDParser(line):
        eid = line[line.find("\t"):].strip()
        return eid

def moveDateParser(line):
        unFormattedDate = line[line.find("\t"):].strip()
        date_object = datetime.strptime(unFormattedDate, "%A, %B %d, %Y")
        formattedDate = date_object.strftime("%m/%d/%Y")
        return formattedDate

def commentsParser(line):
        data = line[line.find('\t'):].strip()
        if data == "":
                return "0 Boxes just labels"
        else:
                return  data + " Boxes and labels"
        