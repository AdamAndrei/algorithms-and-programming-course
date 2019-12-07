import lab6_string.test as test

from lab6_string.logic import *


def print_menu():
    print("1 - Add object")
    print("2 - Remove object")
    print("3 - Update object")
    print("4 - Move object from one place to another")
    print("5 - Add a string to the objects description with a higher price than a given number")
    print("6 - Determine the highest price from each location")
    print("7 - Ordering items in ascending order after the purchase price")
    print("8 - Display the price amounts for each location")
    print("9 - Undo")
    print("10 - Redo")
    print("11 - Exit")


"""
Features:
F1. Adding an object to inventory
F2. Removing an object from inventory
F3. Updating an object from inventory
F4. Move objects from one place to another
F5. Add string to description

Features:
F1. Adding an expense
F2. Removing an expense
F3. Modifying an expense

Running scenario for F1:
# | User          | Program                           | Comment
-----------------------------------------------------------------------------------------------------------------------------------------------------------
1 |               | <main>                            | The program displays the menu
2 | 1             |                                   | The user chooses the addition
3 |               | Give the object ID:               | The program asks for the object ID
4 | 1             | Give the name of the object:      | The user gives the number 1 and the program asks for the name
5 | chair         | Give the description of the object| The user gives the name 'chair' and the program requests the description
6 | made of wood  | Give the price of object          | The user gives description 'made of wood' and the program asks for the price
7 | 23            | Give the location                 | The user gives the price 23 and the program asks for location
8 | room          | Add and print object              | The program displays the menu


Activities for F1:
1. Representation of object as a dictionary
2. Read the data for an object
3. Adding the object to the inventory
4. Completion of the user interface

____________________________________________________________________________________________________________________________________________________________________________________________________________

Running scenario for F2:
# | User          | Program                                                | Comment
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1 |               | <main>                                                 | The program displays the menu
2 |2              | Give the id                                            | We choose to remove an object and the program asks for the id of the object wanted to be removed
3 |1              | The program remove object and print the inventory      | The program delete the object with ID = 1 from the list
4 |               | <main>                                                 | The list has been modified, by deleting the desired object, the menu being displayed again
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Activities for F2:
1. Read a list of dictionaries 
2. Delete one object from list
3. Completion of the user interface

____________________________________________________________________________________________________________________________________________________________________________________________________________

Running scenario for F3:
# | User                                | Program                                                                                 | Comment
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1 |                                     | <main>                                                                                  | The program displays the menu
2 | 3                                   |  Give the id                                                                            | The user choose to updare and the program asks for for the id 
3 |                                     |  Update object and print list                                                           | The program print the list with the updated object
4 |                                     |  What option do you want:                                                               | The program display the menu and asks for another command
8 |                                     | <main>                                                                                  | 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Activities for F3:
1. Read the number for the object which need to updated
2. Read the data for the new expense
3. Modifying an object from the inventory
4. Completion of the user interface


____________________________________________________________________________________________________________________________________________________________________________________________________________

Running scenario for F4:
# | User                                | Program                                           | Comment
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1 |                                     | <main>                                            | The program displays the menu
2 |4                                    |  Give location                                    | The user chooses to move the
3 |room                                 |  Give new location                                | The program asks for the new location
4 |roof                                 |  What option do you want:                         | The program print the list with the object moved into the new location and print menu
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Activities for F4:
1. Read the location for the objects which need to be moved
2. Read the data for the new location
3. Modifying objects from the inventory
4. Completion of the user interface


____________________________________________________________________________________________________________________________________________________________________________________________________________

Running scenario for F5:
# | User                     | Program                                           | Comment
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1 |                          | <main>                                            | The program displays the menu
2 |5                         |                                                   | The user chooses to add string to the object descriptions 
3 |                          |  Give string                                      | The program asks for the string
4 |ANDREI                    |  Give number                                      | The program  asks for the number to compare
5 |                          |  Print list modified and menu                     | The program prints the modified repository
8 |                          | <main>                                            | 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Activities for F5:
1. Read the string you want to add and the minim value of price
2. Modifying object descriptions from the inventory
3. Completion of the user interface

"""

ITEMS_DB_FILE = "items_db.json"


def main():
    list = []
    list_for_undo = []
    list_for_redo = []
    while True:
        print_menu()
        try:
            operation = int(input("What option do you want:  "))
            if operation == 1:
                ID = int(input("ID= "))
                name = input("name = ")
                description = input("description= ")
                price = float(int(input("price= ")))
                location = input("location= ")
                obj = create_object_dictionary(ID, name, description, price, location)
                validate_item(obj)
                if len(list) > 0:
                    validate_unique_id(obj, list)
                add_object_dictionary(list, obj, ITEMS_DB_FILE)
                list_for_undo.append([remove_object_dictionary, list, ID, ITEMS_DB_FILE])
                list_for_redo = []
            elif operation == 2:
                ID = int(input("ID= "))
                list_for_undo.append([add_object_dictionary, list, get_obj_by_id(ID, list), ITEMS_DB_FILE])
                remove_object_dictionary(list, ID, ITEMS_DB_FILE)
                list_for_redo = []
            elif operation == 3:
                ID = int(input("ID= "))
                new_name = input("new_name = ")
                new_description = input("new_description= ")
                new_price = float(int(input("new_price= ")))
                new_location = input("new_location= ")
                update_object_dictionary(ID, list, new_name, new_description, new_price, new_location, ITEMS_DB_FILE)
            elif operation == 4:
                location = input("location= ")
                new_location_to_move = input("new_location_to_move= ")
                move_object_dictionary(list, location, new_location_to_move, ITEMS_DB_FILE)
            elif operation == 5:
                string = input("string= ")
                price = float(int(input("the given number= ")))
                add_string_dictionary(list, string, price, ITEMS_DB_FILE)
            elif operation == 6:
                print(max_per_location_dictionary(list))
            elif operation == 7:
                ascending_order_by_price_dictionary(list, ITEMS_DB_FILE)
            elif operation == 8:
                print(sum_by_location_dictionary(list))
            elif operation == 9:
                if len(list_for_undo) > 0:
                    oper = list_for_undo[-1]
                    ope_string = "{}".format(oper[0])
                    if "remove" in ope_string:
                        list_for_redo.append([add_object_dictionary, list, get_obj_by_id(oper[2], list), ITEMS_DB_FILE])
                    if "add" in ope_string:
                        list_for_redo.append([remove_object_dictionary, list, get_ID_dictionary(oper[2]),
                                              ITEMS_DB_FILE])
                    op = list_for_undo.pop()
                    op[0](op[1], op[2], op[3])
                else:
                    print("You have nothing to undo")
            elif operation == 10:
                if len(list_for_redo) > 0:
                    oper = list_for_redo[-1]
                    ope_string = "{}".format(oper[0])
                    if "remove" in ope_string:
                        list_for_undo.append([add_object_dictionary, list, get_obj_by_id(oper[2], list), ITEMS_DB_FILE])
                    if "add" in ope_string:
                        list_for_undo.append([remove_object_dictionary, list, get_ID_dictionary(oper[2]), ITEMS_DB_FILE])
                    ope = list_for_redo.pop()
                    ope[0](ope[1], ope[2], ope[3])
                else:
                    print("Redo cannot be done")
            elif operation == 11:
                break
        except ValueError as ve:
            print(ve)
        print("Actual list:")
        print(list)
        print("")
        print("")
        print("List for undo:")
        print(list_for_undo)
        print("")
        print("")
        print("List for redo:")
        print(list_for_redo)


if __name__ == '__main__':
    test.all_tests()
    main()
