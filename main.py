#Lists
passenger_name_list = []
destination = []
number_of_passengers = []
import time
import os
#Defining function
def clear(): 
    os.system('clear')
 
#Dictionaries
list_merge = {}
selection = {'auckland' : 295, 'wellington' : 230, 'rotorua' : 145}

#Main while loop
start = True
while start == True:
    name = input("Hello I am Waikato Air Bot here to calculate your discount, please enter your name for this order (Minimum of 2 charecters): ")
    if len(name) >= 3:
        locations = True

    else:
        print("please have a minimum of 2 charecters")
        locations = False
        
    while locations == True:
        location = input("Firstly, where are you looking to fly to out of our available destinations. (Type: Auckland, Wellington, Rotorua or fares to see their standared costs): ")
        if location == 'auckland':
            destination.append(location)
            time.sleep(2)
            print("hi")
        elif location == 'wellington':
            destination.append(location)
            time.sleep(2)
            print("hi wellington")
        elif location == 'Rotorua':
            destination.append(location)
            time.sleep(2)
            print("hi Rotorua")