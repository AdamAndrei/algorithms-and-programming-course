"""
Features:
F1. Adding an object to inventory
F2. Removing an object from inventory
F3. Updating an object from inventory
F4. Move objects from one place to another
F5. Add string to description

Features:
F1. Adding an expense
F2. Removing an expense
F3. Modifying an expense

Running scenario for F1:
# | User          | Program                           | Comment
-----------------------------------------------------------------------------------------------------------------------------------------------------------
1 |               | <main>                            | The program displays the menu
2 | 1             |                                   | The user chooses the addition
3 |               | Give the object ID:               | The program asks for the object ID
4 | 1             | Give the name of the object:      | The user gives the number 1 and the program asks for the name
5 | chair         | Give the description of the object| The user gives the name 'chair' and the program requests the description
6 | made of wood  | Give the price of object          | The user gives description 'made of wood' and the program asks for the price
7 | 23            | Give the location                 | The user gives the price 23 and the program asks for location
8 | room          | Add and print object              | The program displays the menu


Activities for F1:
1. Representation of object as a dictionary
2. Read the data for an object
3. Adding the object to the inventory
4. Completion of the user interface

____________________________________________________________________________________________________________________________________________________________________________________________________________

Running scenario for F2:
# | User          | Program                                                | Comment
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1 |               | <main>                                                 | The program displays the menu
2 |2              | Give the id                                            | We choose to remove an object and the program asks for the id of the object wanted to be removed
3 |1              | The program remove object and print the inventory      | The program delete the object with ID = 1 from the list
4 |               | <main>                                                 | The list has been modified, by deleting the desired object, the menu being displayed again
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Activities for F2:
1. Read a list of dictionaries
2. Delete one object from list
3. Completion of the user interface

____________________________________________________________________________________________________________________________________________________________________________________________________________

Running scenario for F3:
# | User                                | Program                                                                                 | Comment
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1 |                                     | <main>                                                                                  | The program displays the menu
2 | 3                                   |  Give the id                                                                            | The user choose to updare and the program asks for for the id
3 |                                     |  Update object and print list                                                           | The program print the list with the updated object
4 |                                     |  What option do you want:                                                               | The program display the menu and asks for another command
8 |                                     | <main>                                                                                  |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Activities for F3:
1. Read the number for the object which need to updated
2. Read the data for the new expense
3. Modifying an object from the inventory
4. Completion of the user interface


____________________________________________________________________________________________________________________________________________________________________________________________________________

Running scenario for F4:
# | User                                | Program                                           | Comment
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1 |                                     | <main>                                            | The program displays the menu
2 |4                                    |  Give location                                    | The user chooses to move the
3 |room                                 |  Give new location                                | The program asks for the new location
4 |roof                                 |  What option do you want:                         | The program print the list with the object moved into the new location and print menu
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Activities for F4:
1. Read the location for the objects which need to be moved
2. Read the data for the new location
3. Modifying objects from the inventory
4. Completion of the user interface


____________________________________________________________________________________________________________________________________________________________________________________________________________

Running scenario for F5:
# | User                     | Program                                           | Comment
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1 |                          | <main>                                            | The program displays the menu
2 |5                         |                                                   | The user chooses to add string to the object descriptions
3 |                          |  Give string                                      | The program asks for the string
4 |ANDREI                    |  Give number                                      | The program  asks for the number to compare
5 |                          |  Print list modified and menu                     | The program prints the modified repository
8 |                          | <main>                                            |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Activities for F5:
1. Read the string you want to add and the minim value of price
2. Modifying object descriptions from the inventory
3. Completion of the user interface

"""
from lab6_cc.exceptions import *
from lab6_cc.logic import *


def uiControlExpenses(list_of_expenses):
    """
    Description: The user interface for control expenses
    :param list_of_expenses: the list of expenses - dict
    :return: -
    """
    nrMax = nrApMax(list_of_expenses)
    listM = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    for m in listM:
        for i in range(1, nrMax+1):
            # listMount = []
            listMount = expensesMount(list_of_expenses, m, i)
            if listMount:
                print('The cost fot the apartment {} in mount {} is: '.format(i, m), listMount)
            # listMount = []


def uiSort(list_of_expenses):
    """
    Description: The user interface for sort
    :param list_of_expenses: the list of expenses - dict
    :return: list of expenses
    """

    # list_of_expenses = orderDesc(list_of_expenses)
    return orderDesc(list_of_expenses)


def uiRemoveAp(list_of_expenses):
    """
    Description: The user interface for remove by apartment number
    :param list_of_expenses: the list of expenses - dict
    :return: the new list
    """
    nrAp = -1
    while nrAp == -1:
        try:
            nrAp = int(input('Write the apartment number:'))
        except ValueError:
            print('Insert a number!')
        else:
            if nrAp <= 0:
                nrAp = -1
                print('The apartment number must positive!')
    return removeExpenses(list_of_expenses, nrAp)


def uiRemoveExpenses(list_of_expenses):
    """
    Description: The user interface for remove by apartment id
    :param list_of_expenses: the list of expenses - dict
    :return: the new list
    """
    ID = -1
    while ID == -1:
        try:
            ID = int(input('Write the id of the expense:'))
        except ValueError:
            print('Insert a number!')
        else:
            if ID <= 0:
                ID = -1
                print('The id must be a positive number!')
    return removeExpense(list_of_expenses, ID)


def UIAddSum(list_of_expenses):
    """
    Description: The user interface for adding sum
    :param list_of_expenses: the list of expenses - dict
    :return: -
    """
    date = input('Write the date:')
    date = try_date(date)
    value = -1
    while value == -1:
        try:
            value = int(input('Write the value for add:'))
        except ValueError:
            print('Insert a number!')
        else:
            if value <= 0:
                value = -1
                print('The value must be a positive number!')
    list_of_expenses = additionCost(list_of_expenses, date, value)
    return list_of_expenses


def uiAdd(list_of_expenses):
    """
    Description: The user interface for add
    :param list_of_expenses: list of expenses - list
    :return: new list
    """
    try:
        ID = -1
        while ID == -1:
            try:
                ID = int(input('Write the id of the expense:'))
            except ValueError:
                print('Insert a number!')
            else:
                if ID <= 0:
                    ID = -1
                    print('The id must be a positive number!')
        nrAp = -1
        while nrAp == -1:
            try:
                nrAp = int(input('Write the apartment number:'))
            except ValueError:
                print('Insert a number!')
            else:
                if nrAp <= 0:
                    nrAp = -1
                    print('The apartment number must positive!')
        sumE = -1
        while sumE == -1:
            try:
                sumE = int(input('Write the cost of the expense:'))
            except ValueError:
                print('Insert a number!')
            else:
                if sumE < 0:
                    sumE = -1
                    print('The cost must positive or 0!')
        date = input('Write the date:')
        date = try_date(date)
        typeE = input('Write the type of the expense:')
        typeE = try_expense_type(typeE)
        new_expense = Add(list_of_expenses, ID, nrAp, sumE, date, typeE)
        return new_expense
    except KeyError as ke:
        print('Error!', ke)
        return list_of_expenses


def uiUpdate(list_of_expenses):
    """
    Description: The user interface for update
    :param list_of_expenses: the list of expenses - dict
    :return: new list
    """
    ID = -1
    while ID == -1:
        try:
            ID = int(input('Write the id of the expense:'))
        except ValueError:
            print('Insert a number!')
        else:
            if ID <= 0:
                ID = -1
                print('The id must be a positive number!')
    nrAp = -1
    while nrAp == -1:
        try:
            nrAp = int(input('Write the apartment number:'))
        except ValueError:
            print('Insert a number!')
        else:
            if nrAp <= 0:
                nrAp = -1
                print('The apartment number must positive!')
    sumE = -1
    while sumE == -1:
        try:
            sumE = int(input('Write the cost of the expense:'))
        except ValueError:
            print('Insert a number!')
        else:
            if sumE < 0:
                sumE = -1
                print('The cost must positive or 0!')
    date = input('Write the date:')
    date = try_date(date)
    typeE = input('Write the type of the expense:')
    typeE = try_expense_type(typeE)

    list_of_expenses = update(
        list_of_expenses,
        ID,
        nrAp,
        sumE,
        date,
        typeE
    )
    print("Updated finished!")
    return list_of_expenses


def uiMaxType(list_of_expenses):
    """
    Description: The user interface for max type
    :param list_of_expenses: the list of expenses - dict
    :return: -
    """
    listMax = detMaxPerType(list_of_expenses)
    print(listMax)


def main():
    """
    The user interface
    """
    list_of_expenses = read_to_file()
    listUndo = [read_to_file()]
    countUndo = 0
    # okUndo = 0
    listRedo = [read_to_file()]
    while True:
        print('1. Add expense.')
        print('2. Delete the expense.')
        print('3. Update the expense.')
        print('4. Delete all expenses for a given apartment.')
        print('5. Adding a value to all the expenses at once read.')
        print('6. Determining the largest expenditure for each type of expenditure.')
        print('7. Order descending expenses by amount.')
        print('8. Display of monthly amounts for each apartment.')
        print('9. Undo')
        print('10. Redo.')
        print('X. EXIT!')
        option = input('Chose the option: ')
        if option == '1':
            list_of_expenses = uiAdd(list_of_expenses)
            listUndo.append(list_of_expenses)
            countUndo = 0
            # okUndo += 1
        elif option == '2':
            list_of_expenses = uiRemoveExpenses(list_of_expenses)
            listUndo.append(list_of_expenses)
            countUndo = 0
            # okUndo += 1
        elif option == '3':
            list_of_expenses = uiUpdate(list_of_expenses)
            listUndo.append(list_of_expenses)
            countUndo = 0
            # okUndo += 1
        elif option == '4':
            list_of_expenses = uiRemoveAp(list_of_expenses)
            listUndo.append(list_of_expenses)
            countUndo = 0
            # okUndo += 1
        elif option == '5':
            list_of_expenses = UIAddSum(list_of_expenses)
            listUndo.append(list_of_expenses)
            countUndo = 0
            # okUndo += 1
        elif option == '6':
            uiMaxType(list_of_expenses)
        elif option == '7':
            list_of_expenses = uiSort(list_of_expenses)
            listUndo.append(list_of_expenses)
            countUndo = 0
            # okUndo += 1
        elif option == '8':
            uiControlExpenses(list_of_expenses)
        elif option == '9':
            # if okUndo >= 0:
            countUndo += 1
            listRedo.append(listUndo[-1])
            del listUndo[-1]
            new_expenses_list = listUndo[-1]
            save_to_file(new_expenses_list)
            # okUndo += -1
        elif option == '10':
            if countUndo != 0:
                new_expenses_list = listRedo[-1]
                listUndo.append(listRedo[-1])
                del listRedo[-1]
                save_to_file(new_expenses_list)
                countUndo += -1
        elif option == 'a':
            list_of_expenses = read_to_file()
            print(list_of_expenses)
        elif option == 'x' or option == 'X':
            return False


main()
