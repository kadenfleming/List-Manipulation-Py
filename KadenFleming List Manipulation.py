#Shopping list main variable to add and remove items from
shopping_list = []
#Start to main code printing all avaible options in terminal 
while True:
    print("1. Add")
    print("2. Remove")
    print("3. Print list")
    print("4. Quit")
#Choice variable to point to when using elif, input allowing users input to be read from terminal
    choice = input("Enter your choice (1-4): ")
#Using if condition for option 1 if option 1 is sent as input prompt user to enter the item name into terminal
    if choice == "1":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        #Using append to add item to list using the shopping_list variable to point it
        print(f"{item} added to the list.")
        #Ending option 1 by printing msg to user that f most recent item was succesfully added to the list
    elif choice == "2":
        #using elif to continue to the next command if option 2 was input instead of option 1
        if shopping_list:
            index = int(input("Enter the item number to remove: "))
            #prompting user to select an item based on the displayed number when printing list
            if 0 <= index < len(shopping_list):
                #Using user input number check index for corralating list item number
                removed_item = shopping_list.pop(index)
                #After item selected use removed item/shopping_list.pop to remove item from list
                print(f"Item number {index} was removed.")
                #Print msg to user displaying "Item at corralating list number was removed
            else:
                print("Invalid item. Please enter a valid item.")
                #If no item was found with corralating number in list display "Invalid item. Please enter a valid item."
        else:
            print("The list is empty.")
            #If no items are in list the error msg "The list is empty." is displayed to user
    elif choice == "3":
        #If option 3 selected print list variable
        if shopping_list:
            print("Current Shopping List:")
            #Start print with title "Current Shopping List."
            for i, item in enumerate(shopping_list):
                print(f"{i}. {item}")
                #Display list items and corresponding index numbers
        else:
            print("The list is empty.")
            #If list is empy print error msg "The list is empty."

    elif choice == "4":
        print("Final Shopping List:")
        for i, item in enumerate(shopping_list):
            print(f"{i}. {item}")
        print("Exiting the program.")
        break
    #If option 4 selected print full list with corresponding item numbers next to item once completed end program using break function to end program loop

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
        #If none of the avaible options were selected printing error msg to user 

#Sources: Network Chuck Python Lists youtube series, Chat GPT for code refrance and layout
#Comments: Used Network chuck series to understand and create shopping list variables, append function, elif/else/if, and general python list knowlage
# Chat GPT Used for code refrance to understand correct order elif functions 