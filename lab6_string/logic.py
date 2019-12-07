import copy
import json

from lab6_string.domain import *


def add_object_dictionary(list_of_objects, one_object, filename):
    """
    Description: Add an object to inventory
    :param filename:
    :param list_of_objects: list
    :param one_object: list
    :return: A list of objects
    """
    read_from_file(filename)
    list_of_objects.append(one_object)
    save_to_file(list_of_objects, filename)


def remove_object_dictionary(list_of_objects, ID, filename):
    """
    Description: remove an object from inventory
    :param list_of_objects:  list
    :param ID:  int
    :return: a list of objects
    """
    read_from_file(filename)
    for i in range(len(list_of_objects)):
        if get_ID_dictionary(list_of_objects[i]) == ID:
            list_of_objects.pop(i)
            break
    save_to_file(list_of_objects, filename)


def update_object_dictionary(ID, list_of_objects, new_name, new_description, new_price, new_location, filename):
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
    read_from_file(filename)
    for index in range(len(list_of_objects)):
        one_object = list_of_objects[index]
        if get_ID_dictionary(one_object) == ID:
            modified_obj = set_name_dictionary(one_object, new_name)
            modified_obj = set_description_dictionary(modified_obj, new_description)
            modified_obj = set_price_dictionary(modified_obj, new_price)
            modified_obj = set_location_dictionary(modified_obj, new_location)
            validate_item(modified_obj)
            list_of_objects[index] = modified_obj
            break
    save_to_file(list_of_objects, filename)


def move_object_dictionary(list_of_objects, location, new_location, filename):
    """
    Description: Move all the object from one location ta a new location
    :param list_of_objects: list
    :param location: string
    :param new_location: string
    :return: list
    """
    read_from_file(filename)
    for index in range(len(list_of_objects)):
        obj = list_of_objects[index]
        if get_location_dictionary(obj) == location:
            modified_obj = set_location_dictionary(obj, new_location)
            list_of_objects[index] = modified_obj
    save_to_file(list_of_objects, filename)


def add_string_dictionary(list_of_objects, string, price, filename):
    """
    Description: add a string to every description of each object with price higher than a given number
    :param list_of_objects: list
    :param string: string
    :param price: int
    :return: modified list of objects
    """
    read_from_file(filename)
    for index in range(len(list_of_objects)):
        object_one = list_of_objects[index]
        if get_price_dictionary(object_one) > price:
            new_description = get_description_dictionary(object_one) + string
            modified_obj = set_description_dictionary(object_one, new_description)
            list_of_objects[index] = modified_obj
    save_to_file(list_of_objects, filename)


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


def ascending_order_by_price_dictionary(list_of_objects, filename):
    """
    Description: put objects in ascending order by price
    :param list_of_objects: list
    :return:list in ascending order by price
    """
    read_from_file(filename)
    for i in range(len(list_of_objects) - 1):
        for k in range(i, len(list_of_objects)):
            object_i = list_of_objects[i]
            object_k = list_of_objects[k]
            if get_price_dictionary(object_i) > get_price_dictionary(object_k):
                list_of_objects[i] = object_k
                list_of_objects[k] = object_i
    save_to_file(list_of_objects, filename)


def sum_by_location_dictionary(list_of_objects):
    """
    Description: make the sum of all prices for each location
    :param list_of_objects: list
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


def save_to_file(obj, filename):
    """
    Description: save save to file
    :param obj: list
    :param filename: string
    """
    with open(filename, "w") as opened_file:
        json.dump(obj, opened_file)


def read_from_file(filename):
    """
    Description: read from file
    :param filename: string
    :return: string
    """
    try:
        with open(filename, "r") as opened_file:
            return json.load(opened_file)
    except FileNotFoundError:
        return []


def make_copy(list):
    return copy.deepcopy(list)


def validate_item(item):
    """
    Description: validate an item
    :param item: string
    """
    if get_location_dictionary(item) == "":
        raise ValueError("Location cannot be empty")
    if len(get_location_dictionary(item)) > 4:
        raise ValueError("Location can have up to 4 characters")


def validate_unique_id(item, list):
    for object_t in list:
        object_a = object_t[0]
        if get_ID_dictionary(object_a) == get_ID_dictionary(item):
            raise ValueError("Id must be unique")


def get_obj_by_id(id, list_of_objects):
    for object in list_of_objects:
        if get_ID_dictionary(object) == id:
            return object
