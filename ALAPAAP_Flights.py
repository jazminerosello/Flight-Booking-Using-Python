from tabulate import tabulate
from datetime import date
from datetime import time
from datetime import datetime
import time
import os
import pandas as pd

#---------------CODES FOR OPTIONS----------------#

#these are the functions to print choices for users, either aadmin or passengers and each of these functions will return the answer, 
# user have been input to the respective other functions

def person(): #this is for the choice to know whether a user is an admin or a passenger
    print("\n[1] Admin \n[2] Passenger \n[3] Exit \n")
    choice = int(input("What are you? "))
    return choice

def AdminOption(): #this is to know what an admin wants to do for the flight
    print(""" 
[1] Add Flight Details
[2] Edit a Flight
[3] Delete a Flight
[4] View
[5] Search
[6] Go Back 
[7] Exit \n""")
    choice1 = int(input("What do you want to do? "))
    return choice1

def PassengerOption(): #this is to know what a passenger wants to do
    print(""" 
[1] View
[2] Book
[3] Go Back
[4] Exit\n""")
    select = int(input("\nWhat do you want to do? "))
    return select

#------------------------------------------------------#

#--------------CODES FOR LOADING AND SAVING DATA INTO FILE----------------#

#>>> FOR ADMIN PART <<<#
def LoadFromFile():
    #setting variable filename for opening a relative path for file named ALAPAAP record of flights.txt
    filename = os.path.join(fileDir, 'ROSELLO_project/files/ALAPAAP-record-of-flights.txt') 
    
    #------codes for reading a file-------#
    filehandle = open('files/ALAPAAP-record-of-flights.txt', "r")
    flight_details.clear
    for line in filehandle:
        detail = line[:-1].split(" -> ") #splitting or omitting the delimiter
        data = {} #setting variable data as an empty dictionary
        
        #-----saving every detail using their indexes to dictionary data------#
        data['Aircraft Name'] = detail[1]
        data['Departure Location'] = detail[2]
        data['Destination Location'] = detail[3]
        data['Departure Date'] = detail[4]
        data['Departure Time'] = detail[5]
        data['Arrival Date'] = detail[6]
        data['Arrival Time'] = detail[7]
        data['Maximum Number of Passengers'] = detail[8]
        
        #----putting the data dictionary to the local dictionary of flight details
        flight_details[detail[0]] = data
    filehandle.close() #closing the filehandle

def writetofile():
     #setting variable filename for opening a relative path for file named ALAPAAP record of flights.txt
    filename = os.path.join(fileDir, 'ROSELLO_project/files/ALAPAAP-record-of-flights.txt')
    
     #------codes for writing to a file-------#
    filehandle = open('files/ALAPAAP-record-of-flights.txt', "w")
    
    for k in flight_details: #accessing every key in flight details dictionary
        key = flight_details[k] #setting the nested dictionary items into variable key
        
        #----setting the following variables with the value of the nested dictionary in flight details----#
        aircraft_name = key['Aircraft Name']
        departure_location = key['Departure Location']
        destination_location = key['Destination Location']
        date_of_departure = key['Departure Date']
        time_of_departure = key['Departure Time']
        date_of_arrival = key['Arrival Date']
        time_of_arrival = key['Arrival Time']
        max_passenger = key['Maximum Number of Passengers']
        
        #writing those variables to a file
        filehandle.write(k + " -> " + aircraft_name + " -> " + str(departure_location) + " -> " + str(destination_location) + " -> " + str(date_of_departure) + " -> " + str(time_of_departure) + 
                        " -> " +  str(date_of_arrival) + " -> " + str(time_of_arrival) + " -> " + str(max_passenger) +  "\n")
    filehandle.close() #closing the filehandle

#>>> FOR THE PASSENGER PART <<<#
def loadPassenger():
    #setting variable filename for opening a relative path for file named ALAPAAP record of flights.txt
    filename = os.path.join(fileDir, 'ROSELLO_project/files/Passenger-Records.txt')
    
    nameHandle = open('files/Passenger-Records.txt', "r") #opening the filename in reading mode
    passengerRecords.clear
    for line in nameHandle:
        info = line[:-1].split(" -> ") #omitting the delimiters used in the file
        content = {} #setting variable content as an empty dictionary
        
        #-----saving every detail using their indexes to dictionary content------#
        content['Flight Id'] = info[1]
        content['Seat Number'] = info[2]
        
        #-----adding the content dictionary into the passengerRecords local dictionary with the key of info[0] in file
        passengerRecords[info[0]] = content

    nameHandle.close()#closing the nameHandle

def writePassenger():
    #setting variable filename for opening a relative path for file named ALAPAAP record of flights.txt
    filename = os.path.join(fileDir, 'ROSELLO_project/files/Passenger-Records.txt')
    
    nameHandle = open('files/Passenger-Records.txt', "w") #opening the file in writing mode
    for k in passengerRecords: #accessing every key in flight details dictionary
        key = passengerRecords[k] 
        flight_id = key['Flight Id']
        seat_number = key['Seat Number']
        
        nameHandle.write(k + " -> " + str(flight_id) + " -> " + str(seat_number) + '\n') #writing the variables iinto a file
        
    nameHandle.close() #closing the nameHandle

#------------------------------------------------------------#



#------------CODES FOR ADMIN PART----------------------#

def addflight(count): #FUNCTION FOR ADDING FLIGHTS
    
#all of the input are being transformed into uppercase so that there will be uniform
#for the DEPARTURE AND ARRIVAL DATE AND TIME, users are being ask for a specific part of the date adn time so that when it writes into a file, there will be uniform form of delimiters used
#variable data is also being set as dictionary to store some inputs from users and the content of dictionary data will be the nested dictionary of local dictionary flight details with the 
#key of flight ID that will be the function call for the function flight ID with the parameter of count

    aircraft_name = input("\nAircraft Name: ").upper()
    departure_location = input("Departure Location: ").upper()
    destination_location = input("Destination Location: ").upper()
    
    print("\nFor the DATE of DEPARTURE: \n")
    month = str(input("Month: ")).upper()
    day = str(input("Day: "))
    year = str(input("Year: "))
    date_of_departure = month + " " + day + ", " + year
    
    print("\nFor the TIME of DEPARTURE: (The format should be 12hr) \n")
    hour = str(input("Hour: "))
    minute = str(input("Minute: "))
    am_pm = str(input("AM/PM: ")).upper()
    
    if len(hour) == 1:
        time_of_departure = '0' + hour + ":" + minute + am_pm
    elif len(hour) == 2:
        time_of_departure = hour + ":" + minute + am_pm

    
    print("\nFor the DATE of ARRIVAL: \n")
    month = str(input("Month: ")).upper()
    day = str(input("Day: "))
    year = str(input("Year: "))
    date_of_arrival = month + " " + day + ", " + year
    
    print("\nFor the TIME of ARRIVAL: (The format should be 12hr) \n")
    hour = str(input("Hour: "))
    minute = str(input("Minute: "))
    am_pm = str(input("AM/PM: ")).upper()
    
    if len(hour) == 1:
        time_of_arrival = '0' + hour + ":" + minute + am_pm
    elif len(hour) == 2:
        time_of_arrival = hour + ":" + minute + am_pm
    
   
    
    
    max_passenger = input("Maximum Passengers: ")
    
    data = {}
    data['Aircraft Name'] = aircraft_name
    data['Departure Location'] = departure_location
    data['Destination Location'] = destination_location
    data['Departure Date'] = date_of_departure
    data['Departure Time'] = time_of_departure
    data['Arrival Date'] = date_of_arrival
    data['Arrival Time'] = time_of_arrival
    data['Maximum Number of Passengers'] = max_passenger
    
    flight_details[flightId(count)] = data
    
    writetofile()
    return ""


def flightId(count):
#for this function, the first thing it will do is to read files of ALAPAAP flight records to know the length of dictionary flight details there
#then the length will be added to the variable count
#There is also an if-else condition, it checks if the count is less than 10, then the flight id will be 000 adn the count and so on...
#Then it will return the flight id to the function of AddFlight because this flight id will be going to used as the key for the dictionary
    LoadFromFile()
    count += len(flight_details)
    if count < 10: 
        flight_id = '000' + str(count) 
    elif count >= 10 and count < 100: 
        flight_id = '00' + str(count) 
    elif count >= 100:
        flight_id = '0' + str(count) 
    return flight_id


def editflight(): #FUNCTION FOR EDITING THE FLIGHT
#The users will be ask first what flight id they want to edit the details
#Then it will read the file of ALAPAAP FLight records to know flights that was being recorded
#It will also check if the flight id the user has input is in the flight details keys and if it is not there, then it will notify users that the flight id they have input 
#is not existing, else, it will ask users what details from this flight id they want to edit
#after they choose, the detail they edit will call the function writetofile() so that the edited version will be rewrite to the file

    flight_id = input("\nEnter flight id: ")
    LoadFromFile()
    if flight_id not in flight_details:
        print("\n-->Flight ID does not exist. <---\n")
    else:
        for k in flight_details:
            if flight_id == k:
                new_info = flight_details[k]
                print("""\nWhat are you going to edit in this flight?
[1] Aircraft Name
[2] Departure Location
[3] Destination Location
[4] Departure Date
[5] Departure Time
[6] Arrival Date4
[7] Arrival Time
                  """)
                choice2 = int(input("\nAnswer: "))
                if choice2 == 1:
                    editaircraft_name = input("Aircraft Name: ").upper()
                    new_info['Aircraft Name'] = editaircraft_name
                    print('\n' + str(editaircraft_name) + " has been edited in flight " + str(flight_id))
                    writetofile()
                    break
                elif choice2 == 2:
                    editdept_location = input("Departure Location: ").upper()
                    new_info['Departure Location'] = editdept_location
                    print('\n=>>' + str(editdept_location) + " has been edited in flight " + str(flight_id))
                    writetofile()
                    break
                elif choice2 == 3:
                    editdestination_location = input("Destination Location: ").upper()
                    new_info['Destination Location'] = editdestination_location
                    print('\n=>>' + str(editdestination_location) + " has been edited in flight " + str(flight_id))
                    writetofile()
                    break
                elif choice2 == 4:
                    editdeparture_date = input("Departure Date: ").upper()
                    new_info['Departure Date'] = editdeparture_date
                    print('\n=>>' + str(editdeparture_date) + " has been edited in flight " + str(flight_id))
                    writetofile()
                    break
                elif choice2 == 5:
                    editdeparture_time = input("Departure Time: ")
                    new_info['Departure Time'] = editdeparture_time
                    print('\n=>>' + str(editdeparture_time) + " has been edited in flight " + str(flight_id))
                    writetofile()
                    break
                elif choice2 == 6:
                    editarrival_date = input("Arrival Date: ").upper()
                    new_info['Arrival Date'] = editarrival_date
                    print('\n=>>' + str(editarrival_date) + " has been edited in flight " + str(flight_id))
                    writetofile()
                    break
                elif choice2 == 7:
                    editarrival_time = input("Arrival Time: ")
                    new_info['Arrival Time'] = editarrival_time
                    print('\n=>>' + str(editarrival_time) + " has been edited in flight " + str(flight_id))
                    writetofile()
                    break
                else:
                    print("Invalid Input!")
     
    return ""

def deleteflight(): #FUNCTION FOR DELETING FLIGHT
#The users will be ask about the flight id they want to delete from the file
#then the loadfile function will be called out to read the flights being recorded
#The if-else part will check if the flight id is in the file and if it is not, they will notify the users that the record does not exist, 
#and if the flight id is in there, then it will remove from the files by calling out the function of writetofile to rewrite it

    flight_id = input("\nEnter Flight Id: ")
    
    LoadFromFile()
    if flight_id in flight_details: 
        print('\n ~~~> Flight ' + flight_id + ' successfully deleted.') 
        del flight_details[flight_id]
        writetofile() 
    else: 
        print('\nSorry the record does not exit') 
    return "" 
            

# ______________________________CODES FOR VIEW PART____________________________________________________________#   

def viewChoice(): #The printing option for the viewchoice 
    print("""
[1] View All Flight Sorted By Departure Time
[2] View All Flight Using Departure Location
[3] View All Flight Using Aircraft Name""")
    pick = int(input("\nHow do you want to view all flights? "))
    return pick #will return the pick variable or the user input



def viewflight(): #FUNCTION FOR VIEWING THE FLIGHT
    pick = ""
    while True:
        pick = viewChoice()#calling out the viewchoice function to know the pick/answer of the user
        if pick == 1: #if the pick is 1 then it will call the viewbysorted function to view flight by sorted departure time
            viewBySorted()
            break
        elif pick == 2: #if the pick is 2 then it will call the viewbydeptloc function to view flight by the departure lcoation
            viewByDeptLoc()
            break
        elif pick == 3: #if the pick is 3 then it will call the viewbyairnmae function to view flight by the aircraft name
            viewByAirName()
            break
        else: #if the users input  was not in the choices then it will notify users that they have invalid input
            print("\nYou have invalid input!")
    return ""


       
def viewBySorted(): #FUNCTION FOR SORTING THE FLIGHT BY THEIR DEPARTURE TIME
    LoadFromFile() #reading file
    
    real = [] #set real variable as an empty list where we will store the departure time to sort them 
    for k in flight_details:
        key = flight_details[k]
        real.append(key['Departure Time']) #append all the departure time value to real list
        
        
    format = '%I:%M%p' #set the format as 12-hour, minute and pm/am
    element_access = [time.strptime(t, format) for t in real] #we access the element of real list with the user of datetime module to declare that it is a time/converting string into time
    sorted_list = [time.strftime(format, h) for h in sorted(element_access)] #accessing every element in the converted string to time and sorting it according to the format of time
    
    
    new = {} #we set an empty dictionary named as new where we will store the flight details that is being sorted by the departure time
    #for this code, since we have already sorted the departure time value only, we will now access it respective key and rest of dictionary using for loop
    #we will check if i in sorted list is equal to flight_details[k]['Departure Time], it will iterate again and again until it meets its equal, and those who have equal value will be store inot new dictionary
    for i in sorted_list:
        for k in flight_details:
            if i == flight_details[k]['Departure Time']:
                new[k] = flight_details[k]
                

    yey = pd.DataFrame(new) #using pandas for new dictionary and storing it to the variable yey
    print("\n ~~~> These are the flights sorted by their departure time...\n") 
    print(tabulate(yey.T, headers="keys", tablefmt='fancy_grid'))#printing the yey variable using tabulate function so that it will be in a form of tabular 
    
    return ""
    
    
    
def viewByDeptLoc(): #FUNCTION FOR VIEWING THE FLIGHTS USING THE DEPARTURE LOCATION
#It will ask the users first what departure location they want to search or view for
    departure_location = input("\nEnter Departure Location: ").upper() 
    
    LoadFromFile()#reading the file
    
    same = {} #setting variable same as an empty dictionary
    for k in flight_details: #accessing the keys of flight details 
        key2 = flight_details[k]#accessing the key-value pair in the nested dictionary of flight details
        if departure_location == key2['Departure Location']: #checking if the departure location(users input) is the same as the departure location value in the nested dictionary
            same[k] = key2 #if it is true, then the k in it will be stored as the key in same dictionary and the value of it will be its corresponding nested dictionary
        
    flight = pd.DataFrame(same) #storing the same using pandas in flight variable

    #checking the count of the keys in same dictionary
    if len(same) == 0: #if the length is just 0, it means that the same dictionary don't have any key-value pair, or in short it is still an empty dictionary, then
        print("\n=>> Departure Location does not exist. <==") #users will be notified that the departure location they have entered does not exist or does not have any in the files
    elif len(same) > 0: #if the length is more than 0, then iw will print the following
        print('\n\n')
        print(tabulate(flight.T, headers="keys", tablefmt='fancy_grid')) #printing the flight variable using tabulate function
        
        combi = {} #also, there will be combi dictionary as an empty dictionary
        for j in same: #accessing the keys in same
            #setting variable filename for opening a relative path for file named ALAPAAP record of flights.txt
            filename = os.path.join(fileDir, 'ROSELLO_project/files/Passenger-Records.txt') #

            nameHandle = open('files/Passenger-Records.txt', "r")
            for line in nameHandle:
                info = line[:-1].split(" -> ")
                if j == info[1]:
                    content = {}
                    content['Flight Id'] = info[1]
                    content['Seat Number'] = info[2]
                    combi[info[0]] = content
            df = pd.DataFrame(combi) #storing the combi dictionary with the use of pandas into the variable named df
            nameHandle.close()
        
        #checking the length of combi dictionary
        if len(combi) == 0: #if the length is just 0, then it means that no one has booked for this flight
            print("\n ~~~> No one has booked for this flight.")  
        else: #however, if the length is more than 0, then the following will be print out
            print('\n\n ~~~> Here are the passengers with their seat number for the flight with an aircraft of ' + str(departure_location) + "...\n") 
            print(tabulate(df.T, headers=("Passenger Names", "Flight Id", "Seat Number"), tablefmt='fancy_grid')) #printing the df in tabulate function
        
    return ""
   
        
def viewByAirName(): #FUCNTION FOR VIEWING THE FLIGHTS USING AIRCRAFT NAME
#the users will be ask for the aircraft name they wannt to view their flights
    aircraft_name = input("\nEnter Aircraft Name: ").upper()
    
    LoadFromFile() #reading the file
    
    similar = {} #setting the similar variable into an empty dictionary
    #accessing the keys in flight details as k and storing the nested dictionary of flight details as key
    for k in flight_details:
        key = flight_details[k]
        #checking if the aircraft name(user's input) is equal to the aircrft name key in nested dictionary
        if aircraft_name == key['Aircraft Name']:
            similar[k] = key #if the if-condition is true then the k in flight details will be the key to the similar dictionary and its value is its nested dictionary
            
    flight = pd.DataFrame(similar) #storing the similar with the use of pandas into the flight variable
    
    #checking the length of the keys in similar dictionary
    if len(similar) == 0: #if the length is equal to 0 then it will notify users that there's no aircraft name such as they input
        print("\n ==> Aircraft Name does not exist. <==")
    elif len(similar) > 0: #if the length is more than 0 then it will print the fligth variable into the tabular using tabulate function
        print('\n\n')
        print(tabulate(flight.T, headers="keys", tablefmt='fancy_grid'))
    
        combi = {} #setting the variable combi into an empty dictionary  
        for j in similar: #accessing the key in similar dictionary
            
            #setting variable filename for opening a relative path for file named ALAPAAP record of flights.txt
            filename = os.path.join(fileDir, 'ROSELLO_project/files/Passenger-Records.txt')

            nameHandle = open('files/Passenger-Records.txt', "r")
            for line in nameHandle:
                info = line[:-1].split(" -> ")
                if j == info[1]:
                    content = {}
                    content['Flight Id'] = info[1]
                    content['Seat Number'] = info[2]
                    combi[info[0]] = content
        
            df = pd.DataFrame(combi) #storing the combi dictionary into pandas to df variable 
            nameHandle.close()
        
        #checking the length of combi dictionary
        if len(combi) == 0: #if the length of combi is equal to 0, then it means that no one has booked this flight
            print("\n ~~~> No one has booked for this flight.")  
        else: #if the length is greater than 0 then the following will be print out
            print('\n ~~~> Here are the passengers with their seat number for the flight with an aircraft of ' + str(aircraft_name) + "...\n")  
            print(tabulate(df.T, headers=("Passenger Names", "Flight Id", "Seat Number"), tablefmt='fancy_grid'))   
    return ""
# ______________________________END OF CODES FOR VIEW PART____________________________________________________________#   

## ______________________________CODES FOR SEARCH PART____________________________________________________________#   

def searchChoice(): #for printing the option for search
    print("""
[1] Flight with Available Seats
[2] Flight of an Aircraft
[3] All flight of a day""")
    pick = int(input("\nHow do you want to view all flights? "))
    return pick

def searchflight(): 
    pick = ""
    while True:
        pick = searchChoice() #function call for searchChoice
        if pick == 1: #if the user's answer is 1 then it will call thr availseats to print out the avaialble and occupied seats
            AvailSeats()
            break
        elif pick == 2:  #if the user's answer is 2 then it will call the viewByAirName to print out the flights in their chosen aircraft
            viewByAirName()
            break
        elif pick == 3: #if the user's answer is 2 then it will call the Day to print out the flights in their chosen day
            Day()
            break
        else:
            print("\nYou have invalid input!")
        return ""
    
def AvailSeats(): #FUNCTION CALL FOR THE AVAILABLE SEATS
#This function is to view the available and occupied seats of a flight
    
    LoadFromFile() #reading the file
    con = {} #setting the variable con as an empty dictionary
    for k in flight_details: #accessing the keys in flight details dictioanry
        key2 = flight_details[k] #storing the nested dictionary in the flight details dictionary into key2
        con[k] = key2 #storing the k as key of con dictionary and the value is the key2 

    flight = pd.DataFrame(con) #storing the con as pandas into fliht dictionary
    print('\n\n')
    print(tabulate(flight.T, headers="keys", tablefmt='fancy_grid')) #printing the flight variable into tabular using tabulate function
    print("\n~~~> These are the OCCUPIED and AVAILABLE SEATS for all flights stated above... \n") #notify the users that the following are the availabel and occupied deats
    
#For the seats, we will check if the key maximum number of passenger in nested dictionary of every key in flight detail dictionary is equal to 10 or 15 to determine the value of seat name
#after knowing and checking the value of maximum number of passengers, we will now access the keys of passenger records dictionary by reading the file for that 
#it is to know if there's a passenger who have been occupying seat, upon checking, if they have occupied sspecific seat number, then its value in list of seat name will be changed into OCCUPIED
#after the process, we will print out the seat_name variable into tabular format using the tabulate function
    for m in con: 
        keyvalue = con[m] 
        if keyvalue['Maximum Number of Passengers'] == '10':
            loadPassenger() 
            occupied2 = [] 
            seat_name2 = [['A1 \nAvailable', 'B1 \nAvailable'], ['A2 \nAvailable', 'B2 \nAvailable'], ['A3 \nAvailable', 'B3 \nAvailable'], ['A4 \nAvailable', 'B4 \nAvailable'], ['A5 \nAvailable', 'B5 \nAvailable']]
            for j in passengerRecords:
                name2 = passengerRecords[j] 
                if m == name2['Flight Id']: 
                    occupied2.append(name2['Seat Number'])
                    for i in range(len(occupied2)):
                        if occupied2[i] == 'A1':
                            seat_name2[0][0] = 'OCCUPIED'
                        elif occupied2[i] == 'B1':
                            seat_name2[0][1] = 'OCCUPIED'
                        elif occupied2[i] == 'A2':
                            seat_name2[1][0] = 'OCCUPIED'
                        elif occupied2[i] == 'B2':
                            seat_name2[1][1] = 'OCCUPIED'
                        elif occupied2[i] == 'A3':
                            seat_name2[2][0] = 'OCCUPIED'
                        elif occupied2[i] == 'B3':
                            seat_name2[2][1] = 'OCCUPIED'
                        elif occupied2[i] == 'A4':
                            seat_name2[3][0] = 'OCCUPIED'
                        elif occupied2[i] == 'B4':
                            seat_name2[3][1] = 'OCCUPIED'
                        elif occupied2[i] == 'A5':
                            seat_name2[4][0] = 'OCCUPIED'
                        elif occupied2[i] == 'B5':
                            seat_name2[4][1] = 'OCCUPIED'
                       
                            
            pdtabulate=lambda df:tabulate(df,headers='',tablefmt='fancy_grid')
            print("\n  FLIGHT " + str(m) + ' <<--\n')
            print(pdtabulate(seat_name2))
           
            
            
        elif keyvalue['Maximum Number of Passengers'] == '15':
            loadPassenger()
            seat_name = [['A1 \nAvailable', 'B1 \nAvailable', 'C1 \nAvailable'], ['A2 \nAvailable', 'B2 \nAvailable', 'C2 \nAvailable'], ['A3 \nAvailable', 'B3 \nAvailable', 'C3 \nAvailable'], ['A4 \nAvailable', '   B4 \nAvailable', 'C4 \nAvailable'], ['A5 \nAvailable', '   B5 \nAvailable', 'C5 \nAvailable']]   
            occupied = []
            for k in passengerRecords:
                name = passengerRecords[k]
                if m == name['Flight Id']:
                    occupied.append(name['Seat Number'])
                    for i in range(len(occupied)):
                        if occupied[i] == 'A1':
                            seat_name[0][0] = 'OCCUPIED'
                        elif occupied[i] == 'B1':
                            seat_name[0][1] = 'OCCUPIED'
                        elif occupied[i] == 'C1':
                            seat_name[0][2] = 'OCCUPIED'
                        elif occupied[i] == 'A2':
                            seat_name[1][0] = 'OCCUPIED'
                        elif occupied[i] == 'B2':
                            seat_name[1][1] = 'OCCUPIED'
                        elif occupied[i] == 'C2':
                            seat_name[1][2] = 'OCCUPIED'
                        elif occupied[i] == 'A3':
                            seat_name[2][0] = 'OCCUPIED'
                        elif occupied[i] == 'B3':
                            seat_name[2][1] = 'OCCUPIED'
                        elif occupied[i] == 'C3':
                            seat_name[2][2] = 'OCCUPIED'
                        elif occupied[i] == 'A4':
                            seat_name[3][0] = 'OCCUPIED'
                        elif occupied[i] == 'B4':
                            seat_name[3][1] = 'OCCUPIED'
                        elif occupied[i] == 'C4':
                            seat_name[3][2] = ' OCCUPIED'
                        elif occupied[i] == 'A5':
                            seat_name[4][0] = 'OCCUPIED'
                        elif occupied[i] == 'B5':
                            seat_name[4][1] = 'OCCUPIED'
                        elif occupied[i] == 'C5':
                            seat_name[4][2] = 'OCCUPIED'
                     
            pdtabulate=lambda df:tabulate(df,headers='',tablefmt='fancy_grid')
            print("\n-->> FLIGHT " + str(m) + ' <<--\n')
            print(pdtabulate(seat_name))

            
    return ""
            
def Day(): #FUNCTION FOR VIEWING ALL FLIGHT BY THE SPECIFIC DAY GIVEN BY THE USERS
#The users will be ask by the month, day and year for the flight they want to view, then from reading the file we will access the keys in flight details by using for loop
#after that we check whether the value in departure date key in nested dictionary of flight details is the same as the usr's input
#if it is true then we store that dictionary into the variable/dictionary named check
#we will also going to use pandas for the check dicitonary and store it to the variable df, after that we are going to check the length of check dictionary to know if it is empty or not
#if it is empty then it means that there is no flight for the specific day the users have input, and if it is not empty then we print the df variable into the tabular format using the tabulate function

    month = str(input("\nMonth: ")).upper()
    day = str(input("Day: "))
    year = str(input("Year: "))
    date = month + " " + day + ", " + year
    LoadFromFile()
    check = {}
    for k in flight_details:
        if flight_details[k]['Departure Date'] == date:
            check[k] = flight_details[k]
    
    df = pd.DataFrame(check)   
            
    if len(check) == 0:
        print("\n ==> There is no flight for " + str(date) + '<==')
    else:
        print('\n ~~~> Flight for this day is the following: \n')
        print(tabulate(df.T, headers="keys", tablefmt='fancy_grid'))
    

    return ""
 
#---------------------END FOR CODES FOR SEARCH PART-------------------------------------------#


#----------------CODES FOR PASSENGER PART------------------------#
def PassViewOption(): #FUNCTIONS FOR PRINTING THE OPTIONS IN VIEWING THE FLIGHTS
    print("""
[1] View All Flight Sorted By Departure Time 
[2] View All Flight Using Departure Location
[3] View Flight Using Departure Location And Destination Location""")
    select1 = int(input("\nHow do you want to view the flights? "))
    return select1

def PassView(): 
    select1 = ""
    while True:
        select1 = PassViewOption() #funtion call for PassViewOption()
        if select1 == 1: #if the users input is 1, then the viewbysorted function will be called out
            viewBySorted()
            break
        elif select1 == 2: #if the users input is 2, then the viewbydepartureloc function will be called out
            viewByDepartureLoc()
            break
        elif select1 == 3: #if the users input is 3, then the viewbydeptdestloc function will be called out
            viewByDeptDestLoc()
            break
        else:
            print("\nYou have invalid input!")
    return ""

def viewByDepartureLoc(): #FUNCTIONS FOR VIEWING FLIGHTS BY THE DEPARTURE LOCATION GIVEN BY THE USER
    
#they will be ask first what departure location they want to see the flight
#then we will open the file of ALAPAAP flights record in reading mode to determine the flights being recorded
#we will going to access the key of flight_details and set every keys nexted dictionary into the variable names key2, then we will check if the users input is equal to the
#value of departure location in the nested dict of k, then we will store those keys and its nested dictionary into the same dictionary
#then we set the same dictionary as pandas and store it into flight variable. 
#we will determine the length of same dictionary to determine if it is empty or not, if it is then we will tell the user that the location they have input do not have flights, 
#if it is not then we will print out the flight variable into tabular format using tabulate function 
    departure_location = input("\nEnter Departure Location: ").upper()
    
    LoadFromFile()
    
    same = {}
    for k in flight_details:
        key2 = flight_details[k]
        if departure_location == key2['Departure Location']:
            same[k] = key2
        
    flight = pd.DataFrame(same) 

    if len(same) == 0:
        print("\nDeparture Location does not exist.")
    elif len(same) > 0:
        print('\n\n')
        print(tabulate(flight.T, headers="keys", tablefmt='fancy_grid'))
        
    return ""

def viewByDeptDestLoc(): #FUNCTIONS FOR VIEWING FLIGHTS BY THE DEPARTURE LOCATION AND DESTINATION LOCATION GIVEN BY THE USER
    
#they will be ask first what departure and destination location  they want to see the flight
#then we will open the file of ALAPAAP flights record in reading mode to determine the flights being recorded
#we will going to access the key of flight_details and set every keys nexted dictionary into the variable names key2, then we will check if the users input is equal to the
#value of departure location and destination location in the nested dictionary of k, then we will store those keys and its nested dictionary into the same dictionary
#then we set the same dictionary as pandas and store it into flight variable. 
#we will determine the length of same dictionary to determine if it is empty or not, if it is, then we will tell the user that the location they have input do not have flights, 
#if it is not then we will print out the flight variable into tabular format using tabulate function 
    
    departure_location = input("\nEnter Departure Location: ").upper()
    destination_location = input("Enter Destination Location: ").upper()
    
    filename = os.path.join(fileDir, 'ROSELLO_project/files/ALAPAAP-record-of-flights.txt')
    
    filehandle = open('files/ALAPAAP-record-of-flights.txt', "r")
    for line in filehandle:
        detail = line[:-1].split(" -> ")
        data = {}
        data['Aircraft Name'] = detail[1]
        data['Departure Location'] = detail[2]
        data['Destination Location'] = detail[3]
        data['Departure Date'] = detail[4]
        data['Departure Time'] = detail[5]
        data['Arrival Date'] = detail[6]
        data['Arrival Time'] = detail[7]
        data['Maximum Number of Passengers'] = detail[8]
        flight_details[detail[0]] = data

    same = {}
    for k in flight_details:
        key2 = flight_details[k]
        if departure_location == key2['Departure Location'] and destination_location == key2['Destination Location']:
            same[k] = key2
        
    if len(same) == 0:
        print("\n === There is no flight for the " + str(departure_location) + " to " + str(destination_location) +" . ===\n")

    df = pd.DataFrame(same)
    print(tabulate(df.T, headers="keys", tablefmt='fancy_grid'))
    
    filehandle.close()
    
    return ""

def PassBook(): #FUNCTION FOR PASSENGERS BOOKING PROCEDURE
#we will ask first the user for the flight id they want to book a flight, then we will open the ALAPAAP flights record using reading mode
#then we will check if the flight id, user have input is in the flight details dictionary from the file, if it is not in there then we will tell the user that the 
#flight id they have input does not exist, if it is not, then we will ask for the users name then for them to view available and occupied seats, we will call the seat function with the parameter
#of flight id, after that we will ask user for their choice of seat number to marked it as an occupied as they book for this flight
#then the flight id, names and seat number they have input will be stored in dictionary and will be written into the passenger records file

    content = {}
    
    flight_id = input("\nFlight Id: ")
    
    LoadFromFile()
    if flight_id not in flight_details:
        print("\nFlight Id does not exist!")
    else:
        names = input("Enter your Name: ").upper()
        Seats(flight_id)
        seat = input("\nSeat Number: ").upper()
        print('\n ~~~> You have successfully booked into FLIGHT ' + str(flight_id) + ' with SEAT NUMBER ' + str(seat) + '.')
        
        content['Flight Id'] = flight_id
        content['Seat Number'] = seat
        passengerRecords[names] = content
        writePassenger()
    return ""
    
def Seats(flight_id): #FUNCTION FOR SHOWING SEATS FORMATION TO PASSENGERS
#first we will open the alapaap flights record using the reading mode
#then we will tell the users to choose seats upon the given tabular formation of seat in their chosen fligth
#upon reading the alapaap file, we will access the nested dictionary value of maximum number of passengers of the flight id(key of flight details) to know if their value is either 15 or 10
#which is also the process to know how many seats there would be in this flight.Upon knowing the number of seats, we will open the passenger records file to know the passengers
#who has been booked for this flight and their seat number so we can display to the seat number as occupied.

    LoadFromFile()
    print("\n ~~~> Select your seat number for this flight " + str(flight_id) + " \n")
    if flight_details[flight_id]['Maximum Number of Passengers'] == '10':
        
        loadPassenger()
            
        seat_name2 = [['A1 \nAvailable', 'B1 \nAvailable'], ['A2 \nAvailable', 'B2 \nAvailable'], ['A3 \nAvailable', 'B3 \nAvailable'], ['A4 \nAvailable', 'B4 \nAvailable'], ['A5 \nAvailable', 'B5 \nAvailable']]
        occupied2 = []
        for j in passengerRecords:
            name2 = passengerRecords[j]
            if flight_id == name2['Flight Id']:
                occupied2.append(name2['Seat Number'])
                for i in range(len(occupied2)):
                    if occupied2[i] == 'A1':
                        seat_name2[0][0] = 'OCCUPIED'
                    elif occupied2[i] == 'B1':
                        seat_name2[0][1] = 'OCCUPIED'
                    elif occupied2[i] == 'A2':
                        seat_name2[1][0] = 'OCCUPIED'
                    elif occupied2[i] == 'B2':
                        seat_name2[1][1] = 'OCCUPIED'
                    elif occupied2[i] == 'A3':
                        seat_name2[2][0] = 'OCCUPIED'
                    elif occupied2[i] == 'B3':
                        seat_name2[2][1] = 'OCCUPIED'
                    elif occupied2[i] == 'A4':
                        seat_name2[3][0] = 'OCCUPIED'
                    elif occupied2[i] == 'B4':
                        seat_name2[3][1] = 'OCCUPIED'
                    elif occupied2[i] == 'A5':
                        seat_name2[4][0] = 'OCCUPIED'
                    elif occupied2[i] == 'B5':
                        seat_name2[4][1] = 'OCCUPIED'
                       
                            
        pdtabulate=lambda df:tabulate(df,headers='',tablefmt='fancy_grid')
        print(pdtabulate(seat_name2))
            
    elif flight_details[flight_id]['Maximum Number of Passengers'] == '15':
        
        loadPassenger()
            
        seat_name = [['A1 \nAvailable', 'B1 \nAvailable', 'C1 \nAvailable'], ['A2 \nAvailable', 'B2 \nAvailable', 'C2 \nAvailable'], ['A3 \nAvailable', 'B3 \nAvailable', 'C3 \nAvailable'], ['A4 \nAvailable', '   B4 \nAvailable', 'C4 \nAvailable'], ['A5 \nAvailable', '   B5 \nAvailable', 'C5 \nAvailable']]   
        occupied = []
        for k in passengerRecords:
            name = passengerRecords[k]
            if flight_id == name['Flight Id']:
                occupied.append(name['Seat Number'])
                for i in range(len(occupied)):
                    if occupied[i] == 'A1':
                        seat_name[0][0] = 'OCCUPIED'
                    elif occupied[i] == 'B1':
                        seat_name[0][1] = 'OCCUPIED'
                    elif occupied[i] == 'C1':
                        seat_name[0][2] = 'OCCUPIED'
                    elif occupied[i] == 'A2':
                        seat_name[1][0] = 'OCCUPIED'
                    elif occupied[i] == 'B2':
                        seat_name[1][1] = 'OCCUPIED'
                    elif occupied[i] == 'C2':
                        seat_name[1][2] = 'OCCUPIED'
                    elif occupied[i] == 'A3':
                        seat_name[2][0] = 'OCCUPIED'
                    elif occupied[i] == 'B3':
                        seat_name[2][1] = 'OCCUPIED'
                    elif occupied[i] == 'C3':
                        seat_name[2][2] = 'OCCUPIED'
                    elif occupied[i] == 'A4':
                        seat_name[3][0] = 'OCCUPIED'
                    elif occupied[i] == 'B4':
                        seat_name[3][1] = 'OCCUPIED'
                    elif occupied[i] == 'C4':
                        seat_name[3][2] = 'OCCUPIED'
                    elif occupied[i] == 'A5':
                        seat_name[4][0] = 'OCCUPIED'
                    elif occupied[i] == 'B5':
                        seat_name[4][1] = 'OCCUPIED'
                    elif occupied[i] == 'C5':
                        seat_name[4][2] = 'OCCUPIED'
                     
        pdtabulate=lambda df:tabulate(df,headers='',tablefmt='fancy_grid')
        print(pdtabulate(seat_name))
    return ""
#-----------------------------------------------------------------# 
 
 
 
    
#--------------FUNCTION CALL AND WHILE LOOPS FOR OPTION----------#     
def Admin():
    choice1 = ""
    count = 1 #we set the variable count for 1, this count will be going to use for the flight id of the flight
    while True:
        choice1 = AdminOption() #function call for adminoption
        if choice1 == 1: #if the users input is 1, then addflight will be called out
            addflight(count)
            continue
            break
        elif choice1== 2:#if the users input is 2, then editflight will be called out
            editflight()
            continue
        elif choice1 == 3:#if the users input is 3, then deleteflight will be called out
            deleteflight()
            continue
            break
        elif choice1 == 4:#if the users input is 4, then viewflight will be called out
            viewflight()
            continue
            break
        elif choice1 == 5:#if the users input is 5, then searchflight will be called out
            searchflight()
            continue
            break
        elif choice1 == 6:#if the users input is 6, then choice will be called out
            choice()
            continue
            break
        elif choice1 == 7:#if the users input is 7, then it will terminate the program
            thanks('''
                                        Thank you for checking, Admin!\n
                                        Have a very great day! :)\n''')
            break
        else:#but if the user input is none of the above then there will be notification that they have invalid input
            print("Invalid input")
    return ""

def Passenger(): 
    select = ""
    while True:
        select = PassengerOption() #function call for PassengerOption()
        if select == 1:#if the users input is 1, then PassView will be called out
            PassView()
            continue
            break
        elif select == 2:#if the users input is 2, then passbook will be called out
            PassBook()
            continue
            break
        elif select == 3: #if the users input is 3, then choice will be called out
            choice()
            continue
            break
        elif select == 4: #if the users input is 4, then ait will terminate the loop for passenger
            print('\n\n')
            thanks('''
                                        Thank you for checking on us!\n
                            We hope to see you onboard to one of our airplanes!\n\n
                             "ALAPAAP Flights, our priority is your security."\n\n
                                        Have a very great day! :)\n''')
            break
        else: #if the users input is none of the above, then it will notify them that they have invalid input
            print("You have invalid input!")

#the thanks and hello message is for the border of the message when the user choose to exit.
def thanks(msg):
    row = 100 #we set the row as 100 
    joinforce = ''.join(['+'] + ['-' *row] + ['+']) #an empty stry will be joined by a plus sign and a hypen(times 100) and plus sign again to form the row
    finish = joinforce + '\n'"|"+msg+"|"'\n' + joinforce #this is for the next line
    print(finish) 
    
def hello(msg):
    row = len(msg)  #we set the row as the length of the message that will be inout inside the box/border
    joinforce = ''.join(['+'] + ['-' *row] + ['+']) #an empty stry will be joined by a plus sign and a hypen(times 100) and plus sign again to form the row
    finish = joinforce + '\n'"|"+msg+"|"'\n' + joinforce #this is for the next line
    print(finish)

def choice():
    choice= ""
    while True:
        choice = person() #function call for the person()
        if choice == 1:#if the users input is 1, then Admin will be called out
            print(""" 
                  *-*-*-*-*-*   WELCOME TO ALAPAAP FLIGHTS ADMIN   *-*-*-*-*-*""")
            Admin()
            break
        elif choice == 2: #if the users input is 2, then Passenger will be called out
            print(""" 
                              *-*-*-*-*-*   WELCOME TO ALAPAAP FLIGHTS FUTURE PASSENGER   *-*-*-*-*-*\n
                        ALAPAAP Flights are ready to serve and give you a safety trip towards your destination...
                                                 "Our priority is your security." """)
            Passenger()
            break
        elif choice == 3: #if the users input is 3, then it will terminate the program
            print("\nThank you for checking on us! Have a great day!")
            break
        else: #if the users input none of the choices then it will notify them that they have invalid input
            print("\nYou have invalid input")
    return ""

print('\n')
hello("WELCOME ABOARD USER!")

fileDir = os.path.dirname(os.path.realpath('__file__')) #for the directory of files using the os      

flight_details = {}
passengerRecords = {}
choice()
