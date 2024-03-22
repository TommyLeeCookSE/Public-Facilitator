#Takes a .csv file and uppercase every string

import csv

filename = "Badges/fileToBeRead.csv"
filename2 = "Badges/fileToWriteTo.csv"
rows = []
finalRows = []
tempArray = []
first_name = ""
last_name = ""
employee_ID = ""
title = ""
company = ""
department = ""
supervisor = ""
location = "IRVINE\t"


#Take in CSV file and save CSV File into an array
with open(filename, newline='') as csvfile:
    file = csv.reader(csvfile, delimiter = '\t')
    for line in file:
        rows.append(line)

#Assigns every variable in the array to a new variable, uppercases, strips and then appends to a tempArray which is appeneded to the final array 
for item in rows:
    #Gets firstname
    first_name = item[0].upper().strip() + '\t'

    #Gets lastname
    last_name = item[1].upper().strip() + '\t'

    #Gets Employee ID
    employee_ID = item[2].upper().strip() + '\t'

    #Gets Title
    title = item[3].upper().strip() + '\t'
    title = title.replace(',','')
    title = title.replace('.','')

    #Gets Company name and removes everything past and including DBA, also remove commans and periods
    if "DBA" in item[4]:
        dbaIndex = item[4].find("DBA")
        company = item[4][:dbaIndex].upper().strip() + '\t'
    else:
        company = item[4].upper().strip() + '\t'
    
    #Formats Roth to proper standards
    if "ROTH" in company:
        companyIndex = company.find("COMPANIES")
        company = company[:companyIndex].strip() + '\t'
    
    company = company.replace(',','')
    company = company.replace('.','')
    

    #Gets department name and removes the cost center
    if "-" in item[5]:
        hyphenIndex = item[5].find('-')
        department = item[5][hyphenIndex + 2:].upper().strip() + '\t'
    else:
        department = item[5].upper().strip() + '\t'
    
    #Gets supervisor name
    supervisor = item[6].upper().strip() + '\t'

    #Appends all the information above into an array in the order required for the script
    finalRows.append(f'{last_name}{first_name}{employee_ID}{title}{company}{department}{location}{supervisor}')
    # print(finalRows)


#Writes in the fields to the file
with open(filename2, 'w',newline = '') as csvfile:
    file = csv.writer(csvfile)
    for item in finalRows:
        file.writerow([item.strip()])
    print("Badges uppercasing complete.")

