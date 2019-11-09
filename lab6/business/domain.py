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

    dictionary = {"ID": ID,
                  "name": name,
                  "description": description,
                  "price": price,
                  "location": location}
    x = '{}, {}, {}, {}, {}'.format(ID, name, description, price, location)
    return dictionary
    # return x

def get_ID_dictionary(one_object):
    """
    Description: get the ID of an object
    :param one_object: dictionary
    :return: ID of the object
    """
    # a = one_object.split(sep=",")
    # return int(a[0])
    return one_object["ID"]

def get_name_dictionary(one_object):
    """
    Description: get the name of an object
    :param one_object: dictionary
    :return: name of the object
    """
    # a = one_object.split(sep=",")
    # return input(a[1])
    return one_object["name"]


def get_description_dictionary(one_object):
    """
    Description: get the description of an object
    :param one_object: dictionary
    :return: description of the object
    """
    # a = one_object.split(sep=",")
    # return input(a[2])
    return one_object["description"]


def get_price_dictionary(one_object):
    """
    Description: get the price of an object
    :param one_object: dictionary
    :return: price of the object
    """
    # a = one_object.split(sep=",")
    # return float(a[3])
    return one_object["price"]


def get_location_dictionary(one_object):
    """
    Description: get the location of an object
    :param one_object: dictionary
    :return: location of the object
    """
    # a = one_object.split(sep=",")
    # return str(a[4])
    return one_object["location"]


def set_ID_dictionary(one_object, new_ID):
    """
    Description: set the new ID of an object
    :param one_object: dictionary
    :return: new ID of the object
    """
    one_object["ID"] = new_ID


def set_name_dictionary(one_object, new_name):
    """
    Description: set the new name of an object
    :param one_object: dictionary
    :return: new name of the object
    """
    one_object["name"] = new_name


def set_description_dictionary(one_object, new_description):
    """
    Description: set the new description of an object
    :param one_object: dictionary
    :return: new description of the object
    """
    one_object["description"] = new_description


def set_price_dictionary(one_object, new_price):
    """
    Description: set the new price of an object
    :param one_object: dictionary
    :return: new price of the object
    """
    one_object["price"] = new_price


def set_location_dictionary(one_object, new_location):
    """
    Description: set the new location of an object
    :param one_object: dictionary
    :return: new location of the object
    """
    one_object["location"] = new_location


