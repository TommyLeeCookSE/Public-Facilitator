#TODO Instead of using a range function, scan the largest key in the dayPassFile and use that as the max, if a larger value is found, update that to be the max value.

def intChecker(num):
    try:
        return int(num)
    except:
        print(f"Incorrect value ({num}) entered, must be integer, please enter an integer:")





def batchChecker(counter, badgeQuantitiesArray,dayPassFinalDict): #Checks to see if the current counter index inside badgeQuantitiesArray, if so, print a message, increment counter, reset batchCounter
    if  len(dayPassFinalDict) == badgeQuantitiesArray[counter]:
            print()
            print("Batch: " + str(badgeQuantitiesArray[counter]) + " completed.")
            print()
            counter += 1
    return counter




def dictVerifier(lines0, lines1):                           #Checks to makesure each entry is a int and not a string/char/etc
    if(lines0 != (int) or lines0 not in range(1000000)):
       print(str(lines0) + " is not a valid value. Value is greater than 1000000.")
    if(lines1 != (int) or lines1 not in range(1000)):
        print(str(lines1) + " is not a valid key. Value is greater than 1000.")




def printCurrentBadges(dayPassFinalDict):                      #Prints the current badges in the working dict
    print("Current Badges: ")
    print(dayPassFinalDict)
    print("Badges Scanned: " + str(len(dayPassFinalDict)))  




def appendToDict(key,masterDict,finalDict,badgeNumber):         #Appends the values to the working dict
    try:
        finalDict[key] = masterDict[key]
    except:
        finalDict[key] = badgeNumber
    printCurrentBadges(finalDict)
    



def importDict(appendDict,index):                      #Appends and verifies from the master dict.
    try:
        appendDict[int(index[0])] = int(index[1])
    except:
        dictVerifier(index[0],index[1])