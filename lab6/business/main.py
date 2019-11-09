import lab6.business.test as test
from copy import deepcopy

from lab6.business.logic import *


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
    print("10 - Exit")

"""

Features:
F1. Adding an object to inventory
F2. Removing an object from inventory
F3. Updating an object from inventory

Running scenario for F1:
# | User                             | Program                                                                                 | Comment
-----------------------------------------------------------------------------------------------------------------------------------------------------------
1 |                                  | <main>                                                                                  | The program displays the menu
2 |add:1:chair:made of wood:12:room  |                                                                                         | The user chooses to add 
3 |                                  |  [{'ID':1,'name':'chair','description':'made of wood','price': 12, 'location':'room'}]  | The program print the list with the added object
4 |                                  |  What option do you want:                                                               | The program display the menu and asks for another command
5 |add:2:table:made of steel:13:roof |                                                                                         | The user chooses to add 
6 |                                  |  [{'ID':2,'name':'table','description':'made of steel','price': 13,'location':'roof'}]  | The program print the list with the added object
7 |                                  |  What option do you want:                                                               | The program display the menu and asks for another command
8 |                                  | <main>                                                                                  | 
-----------------------------------------------------------------------------------------------------------------------------------------------------------


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
2 |remove:2       |                                                        | We choose to remove the object with ID = 2
3 |               | The program print the modified list of object          | The program delete the object with ID = 2 from the list
4 |               | <main>                                                 | The list has been modified, by deleting the desired object, the menu being displayed again
5 |remove:1       |                                                        | We choose to remove the object with ID = 1
6 |               | The program print the modified list of object          | The program delete the object with ID = 1 from the list
7 | 3             | <main>                                                 | The list has been modified, by deleting the desired object, the menu being displayed again
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Activities for F2:
1. Read a list of dictionaries 
2. Delete one object from list
3. Completion of the user interface

____________________________________________________________________________________________________________________________________________________________________________________________________________

Running scenario for F3:
# | User          | Program                                         | Comment
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1 |                                     | <main>                                                                                  | The program displays the menu
2 |update:1:chair:made of wood:12:room  |                                                                                         | The user chooses to update the object with ID = 1
3 |                                     |  [{'ID':1,'name':'chair','description':'made of wood','price': 12, 'location':'room'}]  | The program print the list with the updated object
4 |                                     |  What option do you want:                                                               | The program display the menu and asks for another command
5 |update:2:table:made of steel:13:roof |                                                                                         | The user chooses to update the object with ID = 2
6 |                                     |  [{'ID':2,'name':'table','description':'made of steel','price': 13,'location':'roof'}]  | The program print the list with the added object
7 |                                     |   What option do you want:                                                              | The program display the menu and asks for another command
8 |                                     | <main>                                                                                  | 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Activities for F3:
1. Read the number for the object which need to updated
2. Read the data for the new expense
3. Modifying an object from the inventory
4. Completion of the user interface

"""


def main():
    list = []
    list_for_undo = []
    while True:
        print_menu()
        operation = int(input("What option do you want:  "))
        if operation == 1:
            ID = int(input("ID= "))
            name = input("name = ")
            description = input("description= ")
            price = float(int(input("price= ")))
            location = input("location= ")
            obj = create_object_dictionary(ID, name, description, price, location)
            list_one = deepcopy(list)
            list_for_undo.append(list_one)
            add_object_dictionary(list, obj)
            print(list)
        elif operation == 2:
            ID = int(input("ID= "))
            list_two = deepcopy(list)
            list_for_undo.append(list_two)
            remove_object_dictionary(list, ID)
            print(list)
        elif operation == 3:
            ID = int(input("ID= "))
            new_name = input("new_name = ")
            new_description = input("new_description= ")
            new_price = float(int(input("new_price= ")))
            new_location = input("new_location= ")
            list_three = deepcopy(list)
            list_for_undo.append(list_three)
            update_object_dictionary(ID, list, new_name, new_description, new_price, new_location)
            print(list)
        elif operation == 4:
            location = input("location= ")
            new_location_to_move = input("new_location_to_move= ")
            list_four = deepcopy(list)
            list_for_undo.append(list_four)
            move_object_dictionary(list, location, new_location_to_move)
            print(list)
        elif operation == 5:
            string = input("string= ")
            price = float(int(input("the given number= ")))
            list_five = deepcopy(list)
            list_for_undo.append(list_five)
            add_string_dictionary(list, string, price)
            print(list)
        elif operation == 6:
            print(max_per_location_dictionary(list))
        elif operation == 7:
            list_seven = deepcopy(list)
            list_for_undo.append(list_seven)
            ascending_order_by_price_dictionary(list)
            print(list)
        elif operation == 8:
            print(sum_by_location_dictionary(list))
        elif operation == 9:
            try:
                list = list_for_undo.pop()
                print(list)
            except IndexError:
                print(" ")
                print("List is empty, Undo cannot be done")
                print(" ")
                print(" ")

        elif operation == 10:
            break


if __name__ == '__main__':
    test.all_tests()
    main()
