from aptdaemon import console

"""
def create_object_dictionary(ID, name, description, price, location):
    
    Description: create an object
    :param ID: int
    :param name: string
    :param description: string
    :param price: float
    :param location: string
    :return: an dictionary

    dictionary = {"ID": ID,
                  "name": name,
                  "description": description,
                  "price": price,
                  "location": location}
    return dictionary


def get_ID_dictionary(one_object):
    
    Description: get the ID of an object
    :param one_object: dictionary
    :return: ID of the object
    
    return one_object["ID"]


def add_object_dictionary(list_of_objects, one_object):
    
    Description: Add an object to inventory
    :param list_of_objects: list
    :param one_object: list
    :return: A list of objects
    
    list_of_objects.append(one_object)

def remove_object_dictionary(list_of_objects, ID):
    
    Description: remove an object from inventory
    :param list_of_objects:  list
    :param ID:  int
    :return: a list of objects
    
    for i in range(len(list_of_objects)):
        if get_ID_dictionary(list_of_objects[i]) == ID:
            list_of_objects.pop(i)
            break




def command_line_interface(line_input):
    '''
    command
    :param line_input: un string care e practic o linie de instructiuni
    :return:
    '''
    str_input = line_input.split('/')
    return str_input


def run():
    line_input = input('Instructions: ')
    #if lineInput=="help":

    str_input = command_line_interface(line_input)
    list_of_objects = []
    while True:
        for line in str_input:
            if "add" in line:
                str_parameters = line.split(" ")
                ID = int(str_parameters[1])
                name = str_parameters[2]
                if str_parameters[3] == "economy" and str_parameters[4] == "plus":
                    classReserved = str_parameters[3] + " " + str_parameters[4]
                    price = int(str_parameters[5])
                    checking = str_parameters[6]
                else:
                    classReserved = str_parameters[3]
                    price = int(str_parameters[4])
                    checking = str_parameters[5]

                object_one = create_object_dictionary(ID, name, description, price, location)
                add_object_dictionary(object_one, list_of_objects)
            elif "delete" in line:
                str_parameters = line.split(" ")
                ID = int(str_parameters[1])
                remove_object_dictionary(ID, list_of_objects)
        print(list_of_objects)


run()
    """

