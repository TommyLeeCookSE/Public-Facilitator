import csv

with open('MeetingsAndEvents\currentWO.csv', mode = "r",encoding='utf8') as file:
    woFile = csv.reader(file)
    counter = 0
    for lines in woFile:
        try:
            if lines[4] == "Assigned*" and lines[6] == "Meeting Request":
                print(f"{lines[1]} {lines[9]}")
                counter += 1
        except:
            print("Error on this line")

    #Create an array for each tech, 
    #append the wo to the tech if it is assigned to them, 
    #Use a data structure that can keep track of all the times of the day and see who is availalbe/not available
    #develop algorithm that extracts the time and date from description
    #Make sure to include prompting to allow users to enter if a tech is out of office
    #Make sure to include start/end times + notifaction if a tech is at lunch
    #Have the program output suggested techs for the event.
        