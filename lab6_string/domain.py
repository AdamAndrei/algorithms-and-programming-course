PROPIERTIES_SEPARATOR = ","


def create_object_dictionary(ID, name, description, price, location):
    """
    Description: create an object
    :param ID: int
    :param name: string
    :param description: string
    :param price: float
    :param location: string
    :return: a string
    """
    return "{},{},{},{},{}".format(ID, name, description, price, location)


def get_ID_dictionary(one_object):
    """
    Description: get the ID of an object
    :param one_object: dictionary
    :return: ID of the object
    """
    return int(one_object.split(sep=PROPIERTIES_SEPARATOR)[0])


def get_name_dictionary(one_object):
    """
    Description: get the name of an object
    :param one_object: dictionary
    :return: name of the object
    """
    return one_object.split(sep=PROPIERTIES_SEPARATOR)[1]


def get_description_dictionary(one_object):
    """
    Description: get the description of an object
    :param one_object: dictionary
    :return: description of the object
    """
    return one_object.split(sep=PROPIERTIES_SEPARATOR)[2]


def get_price_dictionary(one_object):
    """
    Description: get the price of an object
    :param one_object: dictionary
    :return: price of the object
    """
    return float(one_object.split(sep=PROPIERTIES_SEPARATOR)[3])


def get_location_dictionary(one_object):
    """
    Description: get the location of an object
    :param one_object: dictionary
    :return: location of the object
    """
    return one_object.split(sep=PROPIERTIES_SEPARATOR)[4]


def __set_position(obj, position: int, value):
    """
    Description: modify the object
    :param obj: string
    :param position: int
    :param value: int/input
    :return: modified objects
    """
    obj_properties = obj.split(sep=PROPIERTIES_SEPARATOR)
    obj_properties[position] = value
    return create_object_dictionary(
        obj_properties[0],
        obj_properties[1],
        obj_properties[2],
        obj_properties[3],
        obj_properties[4]
    )


def set_ID_dictionary(one_object, new_ID):
    """
    Description: set the new ID of an object
    :param new_ID:
    :param one_object: dictionary
    :return: new ID of the object
    """
    return __set_position(one_object, 0, new_ID)


def set_name_dictionary(one_object, new_name):
    """
    Description: set the new name of an object
    :param new_name:
    :param one_object: dictionary
    :return: new name of the object
    """
    return __set_position(one_object, 1, new_name)


def set_description_dictionary(one_object, new_description):
    """
    Description: set the new description of an object
    :param one_object: dictionary
    :return: new description of the object
    """
    return __set_position(one_object, 2, new_description)


def set_price_dictionary(one_object, new_price):
    """
    Description: set the new price of an object
    :param one_object: dictionary
    :return: new price of the object
    """
    return __set_position(one_object, 3, new_price)


def set_location_dictionary(one_object, new_location):
    """
    Description: set the new location of an object
    :param one_object: dictionary
    :return: new location of the object
    """
    return __set_position(one_object, 4, new_location)



