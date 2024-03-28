#Open database

#Pull all work orders that are meeting requests

#Return information to webpage with Tech Name, WO Time, WO Date, and WO Description

#Allow users to paste new events into form input
#Allow users to select from a dropdown people who are not available
##Popualte this dropdown from list of techs 

#Once user submits, process events and grab the pertinent information, WO Time, WO Date, WO Description
##Also have buffer times set up, 1hr after and 5 hour buffer for 4 hour requests

#Anothe table stores tech availability start/end/lunch which needs to be checked for each assignment
###MORE ThOUGHT HERE

#On each request it will see who is available and provide a list which will be returned to the page to show who is available
##For example if tech x y z are in db but only x,z are available, return tech x,z for the event in a drop down

##Users can select the techs in the dropdowns, and press submit again
### Process the request by creating "dummy" work orders and seeing if it follows all the rules and does not conflict, if it does
### Return some way for the page to display that the option will not work.
### Probably start at the top and see if good, if so, return the tech and remove availabilty for the time 
### Go down the list, if user tried to double book the user will not be available anymore anyways

### Probably need a way to allow users to manually double book but return something that displays that the user is double booked

### Try to have a counter that shows how many currents events a tech is currently doing to try and balance the workload

