from lab6_cc.domain import *
import json


def save_to_file(list_of_expenses):
    """
    Description: Save the list to the file
    :param list_of_expenses: the list of expenses - dict
    :return: -
    """
    with open('expenses.txt', 'w') as f_out:
        f_out.write(json.dumps(list_of_expenses))


def read_to_file():
    """
    Description: Read the list to the file
    :return: the list of expenses from file
    """
    try:
        with open('expenses.txt', 'r') as f_in:
            return json.loads(f_in.read())
    except FileNotFoundError:
        return []


def Add(list_of_expenses, ID, nrAp, sumE, date, typeE):
    """
    Description: Add an expense in list of expenses
    :param list_of_expenses: the list of expenses
    :param ID: the id of the apartment
    :param nrAp: the number of the apartment
    :param sumE: the cost for an expense
    :param date: the date for an expense
    :param typeE: the type of an expense
    :return: new expense list
    """
    read_to_file()
    new_expense = CreateExpenses(ID, nrAp, sumE, date, typeE)
    list_of_expenses.append(new_expense)
    save_to_file(list_of_expenses)
    return list_of_expenses


def removeExpenses(list_of_expenses, nrAp):
    """
    Description: Remove an expense by number
    :param list_of_expenses: the list of expenses - dict
    :param nrAp: the number of the apartment who need to be removed
    :return: new list
    """
    list_of_expenses = read_to_file()
    new_list = []
    for i in range(len(list_of_expenses)):
        if get_nrAp(list_of_expenses[i]) != nrAp:
            new_list.append(list_of_expenses[i])
    save_to_file(new_list)
    return new_list


def removeExpense(list_of_expenses, ID):
    """
    Description: Remove an expense by ID
    :param list_of_expenses: the list of expenses - dict
    :param ID: the id of the apartment who need to be removed
    :return: new list
    """
    list_of_expenses = read_to_file()
    new_list = []
    for i in range(len(list_of_expenses)):
        if get_ID(list_of_expenses[i]) != ID:
            new_list.append(list_of_expenses[i])
    save_to_file(new_list)
    return new_list


def update(list_of_expenses, ID, nrAp, sumE, date, typeE):
    """
    Description: Update an expense by id
    :param list_of_expenses: the list of expenses -dict
    :param ID: the given id
    :param nrAp: new number
    :param sumE: new cost
    :param date: new date
    :param typeE: new type
    :return: new list
    """
    new_list = []
    list_of_expenses = read_to_file()
    for i in range(len(list_of_expenses)):
        if get_ID(list_of_expenses[i]) != ID:
            new_list.append(list_of_expenses[i])
        else:
            new_expense = CreateExpenses(
                get_ID(list_of_expenses[i]),
                int(nrAp) if nrAp != '' else get_nrAp(list_of_expenses[i]),
                int(sumE) if sumE != '' else get_sumE(list_of_expenses[i]),
                date if date != '' else get_date(list_of_expenses[i]),
                typeE if typeE != '' else get_typeE(list_of_expenses[i])
            )
            new_list.append(new_expense)
    save_to_file(new_list)
    return new_list


def additionCost(list_of_expenses, date, value):
    """
    Description: Adding a value to all the expenses at once read
    :param list_of_expenses: the list of expenses - dict
    :param date: the date when add a value to the cost
    :param value: the value for add
    :return: the modify list
    """
    list_of_expenses = read_to_file()
    new_list = []
    for i in range(len(list_of_expenses)):
        if get_date(list_of_expenses[i]) == date:
            new_cost = get_sumE(list_of_expenses[i]) + value
            new_list.append(CreateExpenses(get_ID(list_of_expenses[i]), get_nrAp(list_of_expenses[i]), new_cost, date,
                                           get_typeE(list_of_expenses[i])))
        else:
            new_list.append(list_of_expenses[i])
    save_to_file(new_list)
    return new_list


def detMaxPerType(list_of_expenses):
    """
    Description: Determining the largest expenditure for each type of expenditure
    :param list_of_expenses: the list of expenses - dict
    :return: list of max
    """

    listMax = []
    sumCanal = 0
    sumMaintenance = 0
    sumOther = 0
    costCanalMax = []
    costMaintenanceMax = []
    costOtherMax = []
    list_of_expenses = read_to_file()
    for i in range(len(list_of_expenses)):
        if get_typeE(list_of_expenses[i]) == 'canal' and get_sumE(list_of_expenses[i]) > sumCanal:
            costCanalMax = list_of_expenses[i]
            sumCanal = get_sumE(list_of_expenses[i])
        elif get_typeE(list_of_expenses[i]) == 'maintenance' and get_sumE(list_of_expenses[i]) > sumMaintenance:
            costMaintenanceMax = list_of_expenses[i]
            sumMaintenance = get_sumE(list_of_expenses[i])
        elif get_typeE(list_of_expenses[i]) == 'other' and get_sumE(list_of_expenses[i]) > sumOther:
            costOtherMax = list_of_expenses[i]
            sumOther = get_sumE(list_of_expenses[i])
    listMax.append(costCanalMax)
    listMax.append(costMaintenanceMax)
    listMax.append(costOtherMax)
    return listMax


def orderDesc(list_of_expenses):
    """
    Description: Order descending expenses by amount
    :param list_of_expenses: the list of expenses
    :return: sorted list
    """
    list_of_expenses = read_to_file()
    list_of_expenses = sorted(list_of_expenses, key=lambda expense: get_sumE(expense), reverse=True)
    save_to_file(list_of_expenses)
    return list_of_expenses


def orderApartment(list_of_expenses):
    """
    Description: Sorted the list by number of apartment
    :param list_of_expenses: list of expenses - dict
    :return: sorted list
    """
    list_of_expenses = read_to_file()
    list_of_expenses = sorted(list_of_expenses, key=lambda expense: get_nrAp(expense), reverse=False)
    return list_of_expenses


def nrApMax(list_of_expenses):
    """
    Description: The maximum number of apartments
    :param list_of_expenses: list of expenses - dict
    :return: number maxim
    """
    listAp = orderApartment(list_of_expenses)
    nrMax = get_nrAp(listAp[len(listAp) - 1])
    return nrMax


def expensesMount(list_of_expenses, mount, nrCrt):
    """
    Description: Display of monthly amounts for each apartment
    :param list_of_expenses: list of expenses -dict
    :param mount: the mount
    :param nrCrt: current number
    :return: the list of cost per mount
    """
    listMount = []
    listApartments = orderApartment(list_of_expenses)
    for expense in listApartments:
        if nrCrt == get_nrAp(expense) and mount[0] == get_date(expense)[3] and mount[1] == get_date(expense)[4]:
            listMount.append(get_sumE(expense))
    return listMount


def selectID(list_of_expenses, ID):
    """
    Description: Found an expense with a given ID
    :param list_of_expenses: the list of expenses -dict
    :param ID: the id of an apartment
    :return: an expense
    """
    for expense in list_of_expenses:
        if get_ID(expense) == ID:
            return expense