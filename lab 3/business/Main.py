from .Test import *

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


def main():
    from copy import deepcopy
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

