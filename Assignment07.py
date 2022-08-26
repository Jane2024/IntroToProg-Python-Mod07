#==============================================================================
#Title           :Assignment07.py
#Description     :Demo of Pickle and Error Handling
#Author          :MBruce
#Date            :08212022
#Version         :1.0
#Usage           :python Assignment07.py
#Python_version  :3.10.5
#Change Log      :(who, when, what)
#                :mbruce, 08.21.2022, initial version
#==============================================================================



#############     Import Modules        ################
import pickle


#############     Define Functions      ################

def create_file():
    num_list = []                               # Define list to hold numbers
    for k in range(25):                         # Loop to create list of numbers 1 to 25
        num_list.append(k + 1)                  # append each number to list

    file_out = open("Numbers.dat", 'wb')        # Open file to write binary data
    pickle.dump(num_list, file_out)             # Employ pickle to dump the data into the file
    file_out.close()

def num_search():
    strFilename = 'Numbers.dat'                                # Assign the binary data file to variable
    bolFoundIt = False                                         # boolean to be set if number is found
    list_of_numbers = []                                                        # List for numbers
    int_FindNum = int(input("Enter number to search for between 1 and 25: "))   # prompt user for number

    try:                                                        # Start of Try/except error handling block to check if file is found
        file = open(strFilename,'rb')                           # Opens the file for reading binary data
        list_of_numbers = pickle.load(file)                     # unpickles data from file into list

        for x in range(len(list_of_numbers)):                   # loop to cycle through in search of user number

            if list_of_numbers[x] == int_FindNum:               # If number is found, print found it!
                print("Found your number in list:", int_FindNum)
                file.close()
                bolFoundIt = True                               # Set boolean flag to true if number is found
                break
            else:                                               # If not found, continue to cycle through the list
                continue
        if bolFoundIt != True:                                            # When for loop exits, if flag is not true, number was not found
            print("Reached end of list and your number was not found.")
            file.close()
    except IOError:                                             # If file was not found, then except clause executes and informs the user.
        print("ERROR...cannot locate", strFilename, "file.")


#############       Main         ###########################
# create a binary file of a list of numbers using pickle
create_file()

# load the file and let user search for a number
num_search()
