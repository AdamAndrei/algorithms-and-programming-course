EPSILON = 0.0001


def test_create_object():
    import math
    object = create_object(1, "chair", "made of wood", 23, "table")
    assert len(object) == 5
    assert object[0] == 1
    assert math.fabs(object[3] - 23) < EPSILON
    assert object[1] == "chair"


def create_object(ID, name, description, price, location):
    """
    Description: creates an object
    :param ID: int
    :param name: string
    :param description: string
    :param price: float
    :param location: string
    :return: a list
    """
    object_list = [ID, name, description, price, location]
    return object_list


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
    dictionary = {"ID" : ID,
                  "name" : name,
                  "description": description,
                  "price": price,
                  "location": location}
    return dictionary


def test_get_ID():
    object = create_object(1, "chair", "made of wood", 23, "table")
    assert get_ID(object) == 1


def get_ID(object):
    """
    Description: get the ID of an object
    :param object: list
    :return: ID of the object
    """
    return object[0]
    # return object["ID"]


def test_get_name():
    object = create_object(1, "chair", "made of wood", 23, "masa")
    assert get_name(object) == "chair"


def get_name(object):
    """
    Description: get the name of an object
    :param object: list
    :return: name of the object
    """
    return object[1]
    # return object["name"]


def test_get_description():
    object = create_object(1, "chair", "made of wood", 23, "table")
    assert get_description(object) == "made of wood"
    assert get_description(object) != ""


def get_description(object):
    """
    Description: get the description of an object
    :param object: list
    :return: description of the object
    """
    return object[2]
    # return object["description"]


def test_get_price():
    object = create_object(1, "chair", "made of wood", 23, "table")
    assert get_price(object) == 23


def get_price(object):
    """
    Description: get the price of an object
    :param object: list
    :return: price of the object
    """
    return object[3]
    # return object["price"]


def test_get_location():
    object = create_object(1, "chair", "made of wood", 23, "table")
    assert get_location(object) == "table"


def get_location(object):
    """
    Description: get the location of an object
    :param object: list
    :return: location of the object
    """
    return object[4]
    # return object["location"]


def test_set_ID():
    object = create_object(1, "chair", "made of wood", 23, "table")
    assert get_ID(object) == 1
    set_ID(object, 2)
    assert get_ID(object) == 2


def set_ID(object, new_ID):
    """
    Description: set the new ID of an object
    :param object: list
    :return: new ID of the object
    """
    object[0] = new_ID
    # return object["ID"]


def test_set_name():
    object = create_object(1, "chair", "made of wood", 23, "masa")
    assert get_name(object) == "chair"
    set_name(object, "table")
    assert get_name(object) == "table"


def set_name(object, new_name):
    """
    Description: set the new name of an object
    :param object: list
    :return: new name of the object
    """
    object[1] = new_name
    # object["name"] == new_name


def test_set_description():
    object = create_object(1, "chair", "made of wood", 23, "table")
    assert get_description(object) == "made of wood"
    set_description(object, "made of steel")
    assert get_description(object) == "made of steel"


def set_description(object, new_description):
    """
    Description: set the new description of an object
    :param object: list
    :return: new description of the object
    """
    object[2] = new_description
    # object["description"] == new_description


def test_set_price():
    object = create_object(1, "chair", "made of wood", 23, "table")
    assert get_price(object) == 23
    set_price(object, 12)
    assert get_location(object) == 12

def set_price(object, new_price):
    """
    Description: set the new price of an object
    :param object: list
    :return: new price of the object
    """
    object[3] = new_price
    # object["price"] == new_price


def test_set_location():
    object = create_object(1, "chair", "made of wood", 23, "table")
    assert get_location(object) == "table"
    set_location(object, "roof")
    assert get_location(object) == "roof"


def set_location(object, new_location):
    """
    Description: set the new location of an object
    :param object: list
    :return: new location of the object
    """
    object[4] = new_location
    # object["location"] == new_location


def test_add_object():
    object = create_object(1, "chair", "made of wood", 23, "table")
    list_of_objects = []
    add_objects(list_of_objects, object)
    assert len(list_of_objects) == 1
    assert get_ID(list_of_objects[0]) == 1
    assert get_location(list_of_objects[0]) == "table"


def add_objects(list_of_objects, object):
    """
    Description: Add an object to inventory
    :param list_of_objects: list
    :param object: list
    :return: A list of objects
    """
    list_of_objects.append(object)


def test_remove_object():
    object = create_object(1, "chair", "made of wood", 23, "table")
    list = [object]
    remove_object(list, get_ID(object))
    assert len(list) == 0


def remove_object(list_of_objects, ID):
    """
    Description: remove an object from inventory
    :param list_of_objects:  list
    :param ID:  int
    :return: a list of objects
    """
    for i in range(len(list_of_objects)):
        if get_ID(list_of_objects[i]) == ID:
            list_of_objects.pop(i)
            break


def test_update_object():
    object = create_object(1, "chair", "made of wood", 23, "table")
    list = [object]
    update_object(1, list, "table", "made of glass", 34, "room")
    assert get_description(list[0]) == "made of glass"
    assert get_price(list[0]) == 34


def update_object(ID, list_of_objects, new_name, new_description, new_price, new_location):
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
    for object in list_of_objects:
        if get_ID(object) == ID:
            set_name(object, new_name)
            set_description(object, new_description)
            set_price(object, new_price)
            set_location(object, new_location)


def test_move_object():
    object_one = create_object(1, "chair", "made of wood", 23, "table")
    object_two = create_object(2, "table", "made of steel", 42, "room")
    list = [object_one, object_two]
    move_object(list, "table", "room")
    assert get_location(list[0]) == "room"


def move_object(list_of_objects, location, new_location):
    """
    Description: Move all the object from one location ta a new location
    :param list_of_objects: list
    :param location: string
    :param new_location: string
    :return: list
    """
    for obj in list_of_objects:
        if get_location(obj) == location:
            set_location(obj, new_location)
            break


def test_add_string():
    object_one = create_object(1, "chair", "made of wood", 23, "table")
    object_two = create_object(2, "table", "made of steel", 42, "room")
    list = [object_one, object_two]
    add_string(list, " blue", 24)
    assert get_description(list[1]) == "made of steel blue"


def add_string(list_of_objects, string, price):
    for object_one in list_of_objects:
        if get_price(object_one) > price:
            new_description = get_description(object_one) + string
            set_description(object_one, new_description)


def test_max_per_location():
    object_one = create_object(1, "chair", "made of wood", 23, "table")
    object_two = create_object(2, "table", "made of steel", 42, "room")
    object_three = create_object(3, "table", "made of steel", 44, "room")
    list = [object_one, object_two, object_three]
    dictionary = max_per_location(list)
    assert len(dictionary) == 2
    assert get_ID(dictionary["room"]) == 3


def max_per_location(list_of_objects):
    """
    Description: Function returns a dictionary that contains the maximum price per location
    :param list_of_objects: list
    :return: dictionary
    """
    max_price_by_location = {}
    for object_one in list_of_objects:
        location = get_location(object_one)
        current_price = get_price(object_one)
        if location not in max_price_by_location:
            max_price_by_location[location] = get_price(object_one)

        previous_price = max_price_by_location[location]
        if previous_price < current_price:
            max_price_by_location[location] = current_price

    return max_price_by_location


def test_ascending_order_by_price():
    object_one = create_object(1, "chair", "made of wood", 56, "table")
    object_two = create_object(2, "table", "made of steel", 42, "room")
    object_three = create_object(3, "mirror", "made of glass", 44, "bath")
    list = [object_one, object_two, object_three]
    ascending_order_by_price(list)
    assert get_ID(list[0]) == 2
    assert get_ID(list[1]) == 3
    assert get_ID(list[2]) == 1
    assert get_price(list[2]) == 56


def ascending_order_by_price(list_of_objects):
    """

    :param list_of_objects:
    :return:
    """
    for i in range(len(list_of_objects) - 1):
        for k in range(i, len(list_of_objects)):
            object_i = list_of_objects[i]
            object_k = list_of_objects[k]
            if get_price(object_i) > get_price(object_k):
                list_of_objects[i] = object_k
                list_of_objects[k] = object_i


def sum_by_location(list_of_objects):
    """

    :param list_of_objects:
    :return:
    """
    price_sum_by_location = {}
    for obj in list_of_objects:
        location = get_location(obj)
        price = get_location(obj)
        if location not in obj:
            price_sum_by_location[location] = 0

        price_sum_by_location[location] += price
    return price_sum_by_location
























