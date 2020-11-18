# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add  each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,01.01.2020,Created started script
# Susan Paulen,11.16.2020,Added code to complete Assignment 5 Step 1
#                         Load ToDoList.txt data into lstTable via dicRow
# Susan Paulen,11.16.2020,Added code to complete Assignment 5 Step 3
#                         Show the current items in the lstTable
# Susan Paulen,11.16.2020,Added code to complete Assignment 5 Step 4
#                         Add a New Item from User Input
# Susan Paulen,11.16.2020,Added code to complete Assignment 5 Step 5
#                         Remove an existing item from User Input
# Susan Paulen,11.16.2020,Added code to complete Assignment 5 Step 6
#                         Save lstTable Data to File
# Susan Paulen,11.16.2020,Added code to complete assignment 5 Step 7
#                         Exit Program
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
strItem = ""  # An item's name
strValue = ""  # An item's value
strMenu = ""   # A menu of user options
strChoice = ""  # Capture the user option selection
dicRow = {}    # A row of data separated into elements of a dictionary {Item,Value}
lstTable = []  # A list that acts as a 'table' of rows

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Done

try:
    objFile = open("ToDoList.txt", "r")
    print("ITEM | VALUE")
    for row in objFile:
        strItem, strValue = row.split(",")
        dicRow = {"Item": strItem, "Value": strValue.strip()}
        lstTable.append(dicRow)
        print(dicRow["Item"] + ' | ' + dicRow["Value"])
    objFile.close
except:
    print("There is no previous ToDoList.txt available.  It will be created upon Save.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    #  Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Done
        for objRow in lstTable:
            print(objRow["Item"] + ' | ' + objRow["Value"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Done
        strItem = input("Item: ")
        strValue = input("Value: ")
        lstTable.append({"Item": strItem, "Value": strValue})
        continue

    # Step 5 - Remove an existing item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Done
        strItem = input("Item to Remove: ")
        for objRow in lstTable:
            if objRow["Item"].lower() == strItem.lower():
                lstTable.remove(objRow)
                print("Item Removed")

    # Step 6 - Save items and values to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Done
        objFile = open("ToDoList.txt", "w")  # This saves the text file to same py location
        for row in lstTable:
            objFile.write(str(row["Item"]) + "," + str(row["Value"]) + "\n")
        objFile.close()
        #objFile = open("ToDoList.txt", "w")
        #for objRow in lstTable:
        #    objFile.write(str(objRow["Item"]) + ',' + str(objRow["Value"])+ '\n')
        #objFile.close
        print("Data Saved to ToDoList.txt")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Done
        print("Exiting Program")
        # Delay the message so the user has time to read it
        import time
        x = 0
        while x < 3:
            time.sleep(3)
            x = x+1
        break  # Exit the program
