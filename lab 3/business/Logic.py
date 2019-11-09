from .Domain import *


def add_object_dictionary(list_of_objects, one_object):
    """
    Description: Add an object to inventory
    :param list_of_objects: list
    :param one_object: list
    :return: A list of objects
    """
    list_of_objects.append(one_object)


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


def add_string_dictionary(list_of_objects, string, price):
    for object_one in list_of_objects:
        if get_price_dictionary(object_one) > price:
            new_description = get_description_dictionary(object_one) + string
            set_description_dictionary(object_one, new_description)


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
