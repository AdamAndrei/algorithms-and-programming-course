

def CreateExpenses(ID, nrAp, sumE, date, typeE):
    """
    Description: Create an expense
    :param ID: the id of an apartment
    :param nrAp: the number of an apartment
    :param sumE: the cost of an expense
    :param date: the date of an expense
    :param typeE: the type of an expense
    :return: the new expense
    """

    return '{},{},{},{},{}'.format(ID, nrAp, sumE, date, typeE)


def get_ID(expense):
    """
    Description: Gets the id of an apartment
    :param expense: the expense.
    :return: the apartment number.
    """
    args = expense.split(sep=',')
    return int(args[0])


def get_nrAp(expense):
    """
    Description: Gets the id of an apartment
    :param expense: the expense.
    :return: the apartment id.
    """
    args = expense.split(sep=',')
    return int(args[1])


def get_sumE(expense):
    """
    Description: Gets the sum of an expense
    :param expense: the expense.
    :return: the sum of an expense.
    """
    args = expense.split(',')
    return int(args[2])


def get_date(expense):
    """
    Description: Gets the date of an expense
    :param expense: the expense.
    :return: the date of an expense.
    """
    args = expense.split(sep=',')
    return args[3]


def get_typeE(expense):
    """
    Description: Gets the type of an expense
    :param expense: the expense.
    :return: the type of an expense.
    """
    args = expense.split(sep=',')
    return args[4]


def Create(expense):
    """
    Description: Format the list of expenses for display
    :param expense: an expense
    :return: the expense
    """
    return 'ID: {}. Nr: {}. Cost: {}. Date: {}. Type: {}'.format(
        get_ID(expense),
        get_nrAp(expense),
        get_sumE(expense),
        get_date(expense),
        get_typeE(expense)
    )


def __set_position(obj, position: int, value):
    """
    Description: modify the object
    :param obj: string
    :param position: int
    :param value: int/input
    :return: modified objects
    """
    obj_properties = obj.split(sep=',')
    obj_properties[position] = value
    return CreateExpenses(
        obj_properties[0],
        obj_properties[1],
        obj_properties[2],
        obj_properties[3],
        obj_properties[4]
    )


def set_cost(one_object, new_cost):
    """
    Description: set the new ID of an object
    :param new_cost:
    :param one_object: dictionary
    :return: new ID of the object
    """
    return __set_position(one_object, 2, new_cost)


def get_object_by_id(list_of_expenses, ID):
    """
    Description:
    :param list_of_expenses:
    :param ID:
    :return:
    """
    for i in list_of_expenses:
        if get_ID(i) == ID:
            return i
    return None
