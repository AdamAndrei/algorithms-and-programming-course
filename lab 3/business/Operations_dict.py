from copy import deepcopy

EPSILON = 0.0001


def all_tests():
    test_get_location()
    test_get_description_dictionary()
    test_get_ID_dictionary()
    test_get_name_dictionary()
    test_get_price_dictionary()
    test_set_ID_dictionary()
    test_set_name_dictionary()
    test_set_description_dictionary()
    test_set_price_dictionary()
    test_set_location_dictionary()
    test_add_object_dictionary()
    test_remove_object_dictionary()
    test_update_object_dictionary()
    test_move_object_dictionary()
    test_add_string_dictionary()
    test_max_per_location_dictionary()
    test_sum_by_location_dictionary()


def test_create_object_dictionary():
    import math
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert len(one_object) == 5
    assert one_object["ID"] == 1
    assert math.fabs(one_object["price"] - 23) < EPSILON
    assert one_object["name"] == "chair"


def create_object_dictionary(ID, name, description, price, location):
    """
    Description: create an object
    :param ID: int
    :param name: string
    :param description: string
    :param price: float
    :param location: string
    :return: an dictionary
    """
    obj = {}
    set_ID_dictionary(obj, ID)
    set_name_dictionary(obj, name)
    set_description_dictionary(obj, description)
    set_price_dictionary(obj, price)
    set_location_dictionary(obj, location)

    return obj


def test_get_ID_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_ID_dictionary(one_object) == 1


def get_ID_dictionary(one_object):
    """
    Description: get the ID of an object
    :param one_object: dictionary
    :return: ID of the object
    """
    return one_object["ID"]


def test_get_name_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "masa")
    assert get_name_dictionary(one_object) == "chair"


def get_name_dictionary(one_object):
    """
    Description: get the name of an object
    :param one_object: dictionary
    :return: name of the object
    """
    return one_object["name"]


def test_get_description_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_description_dictionary(one_object) == "made of wood"
    assert get_description_dictionary(one_object) != ""


def get_description_dictionary(one_object):
    """
    Description: get the description of an object
    :param one_object: dictionary
    :return: description of the object
    """
    return one_object["description"]


def test_get_price_dictionary():
    object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_price_dictionary(object) == 23


def get_price_dictionary(one_object):
    """
    Description: get the price of an object
    :param one_object: dictionary
    :return: price of the object
    """
    return one_object["price"]


def test_get_location():
    object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_location_dictionary(object) == "table"


def get_location_dictionary(one_object):
    """
    Description: get the location of an object
    :param one_object: dictionary
    :return: location of the object
    """
    return one_object["location"]


def test_set_ID_dictionary():
    object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_ID_dictionary(object) == 1
    set_ID_dictionary(object, 2)
    assert get_ID_dictionary(object) == 2


def set_ID_dictionary(one_object, new_ID):
    """
    Description: set the new ID of an object
    :param one_object: dictionary
    :return: new ID of the object
    """
    one_object["ID"] = int(new_ID)


def test_set_name_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "masa")
    assert get_name_dictionary(one_object) == "chair"
    set_name_dictionary(one_object, "table")
    assert get_name_dictionary(one_object) == "table"


def set_name_dictionary(one_object, new_name):
    """
    Description: set the new name of an object
    :param one_object: dictionary
    :return: new name of the object
    """
    one_object["name"] = new_name


def test_set_description_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_description_dictionary(one_object) == "made of wood"
    set_description_dictionary(one_object, "made of steel")
    assert get_description_dictionary(one_object) == "made of steel"


def set_description_dictionary(one_object, new_description):
    """
    Description: set the new description of an object
    :param one_object: dictionary
    :return: new description of the object
    """
    one_object["description"] = new_description


def test_set_price_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_price_dictionary(one_object) == 23
    set_price_dictionary(one_object, 12)
    assert get_price_dictionary(one_object) == 12


def set_price_dictionary(one_object, new_price):
    """
    Description: set the new price of an object
    :param one_object: dictionary
    :return: new price of the object
    """
    one_object["price"] = float(new_price)


def test_set_location_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_location_dictionary(one_object) == "table"
    set_location_dictionary(one_object, "roof")
    assert get_location_dictionary(one_object) == "roof"


def set_location_dictionary(one_object, new_location):
    """
    Description: set the new location of an object
    :param one_object: dictionary
    :return: new location of the object
    """
    one_object["location"] = new_location


def test_add_object_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    list_of_objects = []
    add_object_dictionary(list_of_objects, one_object)
    assert len(list_of_objects) == 1
    assert get_ID_dictionary(list_of_objects[0]) == 1
    assert get_location_dictionary(list_of_objects[0]) == "table"
    try:
        add_object_dictionary(list_of_objects, one_object)
        assert False
    except ValueError:
        # expected error
        assert True


def add_object_dictionary(list_of_objects, one_object):
    """
    Description: Add an object to inventory
    :param list_of_objects: list
    :param one_object: list
    :return: A list of objects
    """
    for obj in list_of_objects:
        if get_ID_dictionary(obj) == get_ID_dictionary(one_object):
            raise ValueError("Object with same ID already exists")

    list_of_objects.append(one_object)


def test_remove_object_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    list = [one_object]
    remove_object_dictionary(list, get_ID_dictionary(one_object))
    assert len(list) == 0


def remove_object_dictionary(list_of_objects, ID):
    """
    Description: remove an object from inventory
    :param list_of_objects:  list
    :param ID:  int
    :return: a list of objects
    """
    for i in range(len(list_of_objects)):
        if get_ID_dictionary(list_of_objects[i]) == ID:
            list_of_objects.pop(i)
            break


def test_update_object_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    list = [one_object]
    update_object_dictionary(1, list, "table", "made of glass", 34, "room")
    assert get_description_dictionary(list[0]) == "made of glass"
    assert get_price_dictionary(list[0]) == 34


def update_object_dictionary(ID, list_of_objects, new_name, new_description, new_price, new_location):
    """
    Description: It modify the object with ID given from list
    :param ID: int
    :param list_of_objects: list
    :param new_name: string
    :param new_description: string
    :param new_price: float
    :param new_location: string
    :return:
    """
    for one_object in list_of_objects:
        if get_ID_dictionary(one_object) == ID:
            set_name_dictionary(one_object, new_name)
            set_description_dictionary(one_object, new_description)
            set_price_dictionary(one_object, new_price)
            set_location_dictionary(one_object, new_location)


def test_move_object_dictionary():
    object_one = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    object_two = create_object_dictionary(2, "table", "made of steel", 42, "room")
    list = [object_one, object_two]
    move_object_dictionary(list, "table", "room")
    assert get_location_dictionary(list[0]) == "room"


def move_object_dictionary(list_of_objects, location, new_location):
    """
    Description: Move all the object from one location ta a new location
    :param list_of_objects: list
    :param location: string
    :param new_location: string
    :return: list
    """
    for obj in list_of_objects:
        if get_location_dictionary(obj) == location:
            set_location_dictionary(obj, new_location)


def test_add_string_dictionary():
    object_one = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    object_two = create_object_dictionary(2, "table", "made of steel", 42, "room")
    list = [object_one, object_two]
    add_string_dictionary(list, " blue", 24)
    assert get_description_dictionary(list[1]) == "made of steel blue"


def add_string_dictionary(list_of_objects, string, price):
    for object_one in list_of_objects:
        if get_price_dictionary(object_one) > price:
            new_description = get_description_dictionary(object_one) + string
            set_description_dictionary(object_one, new_description)


def test_max_per_location_dictionary():
    object_one = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    object_two = create_object_dictionary(2, "table", "made of steel", 42, "room")
    object_three = create_object_dictionary(3, "table", "made of steel", 44, "room")
    list = [object_one, object_two, object_three]
    dictionary = max_per_location_dictionary(list)
    assert len(dictionary) == 2
    assert ((dictionary["room"]) == 44)


def max_per_location_dictionary(list_of_objects):
    """
    Description: Function returns a dictionary that contains the maximum price per location
    :param list_of_objects: list
    :return: dictionary
    """
    max_price_by_location = {}
    for object_one in list_of_objects:
        location = get_location_dictionary(object_one)
        current_price = get_price_dictionary(object_one)
        if location not in max_price_by_location:
            max_price_by_location[location] = get_price_dictionary(object_one)

        previous_price = max_price_by_location[location]
        if previous_price < current_price:
            max_price_by_location[location] = current_price

    return max_price_by_location


def ascending_order_by_price_dictionary(list_of_objects):
    """

    :param list_of_objects:
    :return:
    """
    for i in range(len(list_of_objects) - 1):
        for k in range(i, len(list_of_objects)):
            object_i = list_of_objects[i]
            object_k = list_of_objects[k]
            if get_price_dictionary(object_i) > get_price_dictionary(object_k):
                list_of_objects[i] = object_k
                list_of_objects[k] = object_i


def assert_equals(expected, actual):
    if expected == actual:
        return

    raise AssertionError("Failed asserting that actual {0} equals expected {1}".format(actual, expected))


def test_sum_by_location_dictionary():
    obj = create_object_dictionary(1, "chair", "made of wood", 23, "room")
    obj_one = create_object_dictionary(2, "table", "made of steel", 7, "room")
    obj_two = create_object_dictionary(3, "mirror", "made of glass", 20, "bath")
    list_of_objects = [obj, obj_one, obj_two]
    assert_equals(30, sum_by_location_dictionary(list_of_objects)["room"])


def sum_by_location_dictionary(list_of_objects):
    """

    :param list_of_objects:
    :return: dictionary
    """
    price_sum_by_location = {}
    for obj in list_of_objects:
        location = get_location_dictionary(obj)
        price = get_price_dictionary(obj)
        if location not in price_sum_by_location:
            price_sum_by_location[location] = 0

        price_sum_by_location[location] += price
    return price_sum_by_location


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
            try:
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
            except ValueError :
                print("Nu ai bagat valori valide")
        elif operation == 2:
            try:
                ID = int(input("ID= "))
                list_two = deepcopy(list)
                list_for_undo.append(list_two)
                remove_object_dictionary(list, ID)
                print(list)
            except Exception:
                print("")
                print("Da un ID valid ")
                print("")
        elif operation == 3:
            try:
                ID = int(input("ID= "))
                new_name = input("new_name = ")
                new_description = input("new_description= ")
                new_price = float(int(input("new_price= ")))
                new_location = input("new_location= ")
                list_three = deepcopy(list)
                list_for_undo.append(list_three)
                update_object_dictionary(ID, list, new_name, new_description, new_price, new_location)
                print(list)
            except ValueError:
                print("")
                print("Da niste valori bune")
                print("")
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


def get_new_menu():
    return """
    Usage: <instruction>[;<instruction>]                                         (One or more instructions separated by ;)
    Available instructions:
        - add:<ID>:<name>:<description>:<price>:<location>                       (Add object to inventory)
        - remove:<ID>                                                            (Remove object from the list)
        - update:<ID>:<new name>:<new description>:<new price>:<new location>    (Update object from list)
        - move:<location>:<new location>                                         (Move objects from one place to another)
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
