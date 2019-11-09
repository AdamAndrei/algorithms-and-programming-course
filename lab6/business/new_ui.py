from copy import deepcopy

from lab6.business.test import *
from lab6.business.logic import *


def get_new_menu():
    return """
    Usage: <instruction>[;<instruction>]                                         (One or more instructions separated by ;)
    Available instructions:
        - add:<ID>:<name>:<description>:<price>:<location>                       (Add object to inventory)
        - remove:<ID>                                                            (Remove object from the list)
        - update:<ID>:<new name>:<new description>:<new price>:<new location>    (Update object from list)
        - move object:<location>:<new location>                                  (Move objects from one place to another)
        - append string:<string>:<number>                                        (Add a string to the objects description with a higher price than a given number)
        - max price per location                                                 (Determine the highest price from each location)
        - ascending by price                                                     (Ordering items in ascending order after the purchase price)
        - sum by location                                                        (Display the price amounts for each location)
        - undo                                                                   (Undoes the last operation) 
        - exit
       """


def parse_command(command_string):
    command_and_args = command_string.split(sep=";")
    # am o lista cu comenzile si argumentele legate
    instructions_list = []
    for command in command_and_args:
        command_splited = command.split(sep=":")
        # am o lista cu coamnda si argumentele separate
        instruction = {
            "operation": command_splited.pop(0),
            "args": command_splited
        }
        if instruction["operation"] != "":
            instructions_list.append(instruction)

    return instructions_list


def test_parse_command():
    assert_equals(
        # instructions
        [
            # add instruction
            {
                "operation": "add",
                "args": ["1", "chair", "made of wood", "123", "room"]
            },
            # update instruction
            {
                "operation": "update",
                "args": ["1", "table", "made of steel", "12", "room"]
            }
        ],
        parse_command("add:1:chair:made of wood:123:room;update:1:table:made of steel:12:room")
    )

    assert_equals([], parse_command(""))


def assert_argument_count(args, expected):
    if len(args) != expected:
        raise ValueError("Expected {0} args, got {1} instead".format(expected, args))


def apply_instruction(instruction, list, list_for_undo):
    """

    :param instruction:
    :param list:
    :param list_for_undo:
    :return: True If the operation was applied
             False If the operation is exit
    """
    operation = instruction["operation"]
    args = instruction["args"]
    if operation == "add":
        assert_argument_count(args, 5)
        obj = create_object_dictionary(int(args[0]), args[1], args[2], float(args[3]), args[4])
        list_one = deepcopy(list)
        list_for_undo.append(list_one)
        add_object_dictionary(list, obj)
        print(list)
    elif operation == "remove":
        assert_argument_count(args, 1)
        list_two = deepcopy(list)
        list_for_undo.append(list_two)
        remove_object_dictionary(list, int(args[0]))
        print(list)
    elif operation == "update":
        assert_argument_count(args, 5)
        list_three = deepcopy(list)
        list_for_undo.append(list_three)
        update_object_dictionary(int(args[0]), list, args[1], args[2], float(args[3]), args[4])
        print(list)
    elif operation == "move object":
        assert_argument_count(args, 2)
        list_four = deepcopy(list)
        list_for_undo.append(list_four)
        move_object_dictionary(list, args[0], args[1])
        print(list)
    elif operation == "append string":
        assert_argument_count(args, 2)
        list_five = deepcopy(list)
        list_for_undo.append(list_five)
        add_string_dictionary(list, args[0], float(args[1]))
        print(list)
    elif operation == "max price per location":
        print(max_per_location_dictionary(list))
    elif operation == "ascending by price":
        list_seven = deepcopy(list)
        list_for_undo.append(list_seven)
        ascending_order_by_price_dictionary(list)
        print(list)
    elif operation == "sum by location":
        print(sum_by_location_dictionary(list))
    elif operation == "undo":
        list = list_for_undo.pop()
        print(list)
    elif operation == "exit":
        return False
    else:
        raise Exception("Invalid operation: '{0}'".format(operation))

    return True


"""
Features:
F1. Adding an object to inventory
F2. Removing an object from inventory
F3. Updating an object from inventory
F4. Move objects from one place to another
F5. Add string to description

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
3 |               | The program prints the modified list of object          | The program delete the object with ID = 2 from the list
4 |               | <main>                                                 | The list has been modified, by deleting the desired object, the menu being displayed again
5 |remove:1       |                                                        | We choose to remove the object with ID = 1
6 |               | The program prints the modified list of object          | The program delete the object with ID = 1 from the list
7 | 3             | <main>                                                 | The list has been modified, by deleting the desired object, the menu being displayed again
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


____________________________________________________________________________________________________________________________________________________________________________________________________________

Running scenario for F4:
# | User                                | Program                                           | Comment
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1 |                                     | <main>                                            | The program displays the menu
2 |move:roof:room                       |                                                   | The user chooses to move the objects from roof to room
3 |                                     |  The program prints the modified list of objects   | The program print the list with the object moved into the new location
4 |                                     |  What option do you want:                         | The program display the menu and asks for another command
5 |move:bath:roof                       |                                                   | The user chooses to move the objects from bath to roof
6 |                                     |  The program prints the modified list of objects   | The program print the list with the added object
7 |                                     |   What option do you want:                        | The program display the menu and asks for another command
8 |                                     | <main>                                            | 
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
2 |append string:ANDREI:34   |                                                   | The user chooses to add string ANDREI to the object descriptions that have higher price than 34 
3 |                          |  The program prints the modified list of objects   | The program print the list with the object description modified
4 |                          |  What option do you want:                         | The program display the menu and asks for another command
5 |append string:ADAM:23     |                                                   | The user chooses to add string ADAM to the object descriptions that have higher price than 23 
6 |                          |  The program prints the modified list of objects   | The program print the list with the added object
7 |                          |   What option do you want:                        | The program display the menu and asks for another command
8 |                          | <main>                                            | 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Activities for F5:
1. Read the string you want to add and the minim value of price
2. Modifying object descriptions from the inventory
3. Completion of the user interface

"""


def new_ui():
    list = []
    list_for_undo = []
    is_running = True
    while is_running:
        print(get_new_menu())
        command_string = input("What do you want to do: ")
        instructions_list = parse_command(command_string)
        for instruction in instructions_list:
            try:
                is_running = apply_instruction(instruction, list, list_for_undo)
            except Exception as e:
                print("Instruction {0} failed: {1}".format(instruction, str(e)))


all_tests()
test_parse_command()
new_ui()
