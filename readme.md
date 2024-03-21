
# Facilitator - Reporting and Automation Suite

This project originally started as individual python scripts used to automate the Facilities Service Desk role at Edwards Lifescience. Due to its value in automating tasks and reducing human error, the project grew into a flask server so that multiple users could interact with a gui vs a command line and update the hosted database.

Each webpage has been designed to minimize human input and utilize python scripts that preferably read directly from files/databases which are also entered into the system via file inputs and not human input. Infact, all human entry has been removed; all pages are designed to only take data directly from one source and transfer to the next source.

In addition to reducing human error and increasing efficiency due to automation of menial/repetitive tasks; due to the inability to gain api access to some of our external software bases, this program downloads files from the external software and recreates the database internally... Reports can be run and generated from this and is used for more accurate reporting.



## Features

- Badge Automator: Recieves data from the CWP spreadsheet. Data is copied to the program (API Access not granted yet to automatically take the date), run through a python program which uppercases all the data, cleans the data for entry into the CCure system, and returns to a table for users to copy directly into the Ccure system (API Access to update the Ccure database not granted yet). Can copy/paste an unlimited amount of entries.

- Moves Automator: Recieves forms via email which have 30+ fields and is generally difficult to read and translate data to the Moves spreadsheet. Users can copy an unlimited amount of emails and paste into the webpage. Python program analyzes the data, selects what is required, reformats data to requirements for the Moves spreadsheet and provides a table formatted properly for pasting.

- Day Pass Automator: Features an interal database which stores all Day Passes generated via the Ccure system. The database stores when Badge Number, Badge ID, expiration date, last user, and last used date. Without this database (which requires an xml and csv upload) security would be unable to track day passes due to multiple seperate software tools they are using. (CCure and Traction Guest which do not communicate) This tool allows users to upload the xml which contains the card ID and expiration date, it checks the database to match the card ID to the Badge Number, if there is no Badge Number, the webpage displays a table to allow users to enter the number which is added to the database. Another form input allows users to upload a csv which includes data on who used the badge and when was the last time it was used, which is uploaded to the database to be tracked.

- Centerstone Reporting Tools: This is a multi-part reporting tool which takes data from our Centerstone software via a very large excel file. Uploads it to the database taking only the required fields, reformatting the dates (as they are in different formats) which allows us to analyze and preforms operations on later. Users can then generate reports and compare multiple dates (which are saved reports, saved whenever a user runs the report page with the date as the unique ID) to see changes and trends.

## Roadmap

- Complete Centerstone Reporting Tools

- Create Meeting and Events Automation Tools

- Add an Event Log to track ongoing events for Users



## Used By

This project is used by the following companies:

- Edwards Lifesciences



## Usage/Examples
 - Data received from Moves Email:
    
    Haley Whitehead has been added
    Haley Whitehead
    3/20/2024 10:29 AM
    Requestor Name:	Haley Whitehead 
    Name of Person Moving:	Haley Whitehead 
    Employee Type::	Regular 
    Preferred Move Date:	Friday, March 29, 2024 
    Workplace Location Assignment:	Onsite 
    If Shared - please add the name of Shared employee.:	 
    Name of person who approved this move request::	Julie Estrada 
    Extension::	1570 
    Email Address::	julie_estrada@edwards.com 
    Old Building:	T&D - Tech & Discovery 
    If "Other," specify here::	 
    Old Floor #::	Fl2 
    Old Cube/Office #:	T2111B 
    New Building:	T&D - Tech & Discovery 
    If "Other," specify here::	 
    New Floor #::	Fl2 
    New Cube/Office #:	T2111C 
    Will moving boxes need be be delivered?:	No 
    If "Yes," please specify how many::	 
    Move electronic equipment?:	Yes 
    If "Yes," please select the types of equipment::	Monitors; Docking station; Phone 
    If "other," please specify::	 
    Is a new name plate needed?:	Yes 
    Work Order #:	 
    Employee ID:	414327 
    Include any other special requests here::	 
    Today's Date:	3/20/2024 

- Formatted data that comes out:
    - 03/29/2024	Haley	Whitehead	T&D	T2111B	T&D	T2111C	414327		0 Boxes just labels	
## About Me
I'm a Business and Comp Sci major working on becoming a Software/Full-Stack/Automation Engineer. My focus in all my jobs is analyzing reptitive/error prone tasks and functions and automating them. I add value to any and every company I have worked for due to going above and beyond my scope as I try to create more efficient processes for myself and for future employees in my role. I enjoy thinking creatively to try and solve problems especially and I especially enjoy automating menial tasks or tasks where human error is prone.

