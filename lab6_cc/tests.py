from lab6_cc.domain import *
from lab6_cc.logic import *


def test_createExpense():
    expenses = CreateExpenses(1, 12, 250, '13.09.2017', 'canal')
    assert get_ID(expenses) == 1
    assert get_nrAp(expenses) == 12
    assert get_sumE(expenses) == 250
    assert get_date(expenses) == '13.09.2017'
    assert get_typeE(expenses) == 'canal'


def test_get_idApartment():
    expenses = CreateExpenses(1, 12, 250, '13.09.2017', 'canal')
    assert get_ID(expenses) == 1


def test_get_nrAp():
    expenses = CreateExpenses(1, 12, 250, '13.09.2017', 'canal')
    assert get_nrAp(expenses) == 12


def test_get_sumE():
    expenses = CreateExpenses(1, 12, 250, '13.09.2017', 'canal')
    assert get_sumE(expenses) == 250


def test_get_date():
    expenses = CreateExpenses(1, 12, 250, '13.09.2017', 'canal')
    assert get_date(expenses) == '13.09.2017'


def test_get_typeE():
    expenses = CreateExpenses(1, 12, 250, '13.09.2017', 'canal')
    assert get_typeE(expenses) == 'canal'


def test_addExpense():
    list_of_expenses = []
    params = [1, 12, 250, '13.09.2017', 'canal']
    list_of_expenses = Add(list_of_expenses, *params)
    assert get_ID(list_of_expenses[-1]) == params[0]
    assert get_nrAp(list_of_expenses[-1]) == params[1]
    assert get_sumE(list_of_expenses[-1]) == params[2]
    assert get_date(list_of_expenses[-1]) == params[3]
    assert get_typeE(list_of_expenses[-1]) == params[4]


def test_remove_expanses():
    e1 = CreateExpenses(1, 12, 250, '13.09.2017', 'canal')
    e2 = CreateExpenses(2, 13, 350, '16.09.2017', 'maintenance')
    e3 = CreateExpenses(3, 14, 650, '13.01.2017', 'canal')
    listE = [e1, e2, e3]
    listE = removeExpense(listE, get_ID(e1))
    assert get_object_by_id(listE, get_ID(e1)) is None


def test_update_expanses():
    e1 = CreateExpenses(1, 12, 250, '13.09.2017', 'canal')
    e2 = CreateExpenses(2, 13, 350, '16.09.2017', 'maintenance')
    e3 = CreateExpenses(3, 14, 650, '13.01.2017', 'canal')
    update_id = get_ID(e3)
    update_ap = 34
    update_sum = 12
    update_date = ''
    update_type = 'other'
    expanses = [e1, e2, e3]
    new_expanses = update(expanses, update_id, update_ap, update_sum, update_date, update_type)
    assert get_ID(e3) == 3
    assert get_nrAp(e3) == 14
    assert get_sumE(e3) == 650
    assert get_date(e3) == '13.01.2017'
    assert get_typeE(e3) == 'canal'


def test_remove_cost():
    e1 = CreateExpenses(1, 12, 250, '13.09.2017', 'canal')
    e2 = CreateExpenses(2, 13, 350, '16.09.2017', 'maintenance')
    e3 = CreateExpenses(3, 14, 650, '13.01.2017', 'canal')
    listE = [e1, e2, e3]
    listE = removeExpenses(listE, get_nrAp(e1))
    assert get_object_by_id(listE, get_ID(e1)) is None


def test_addValue():
    e1 = CreateExpenses(1, 12, 250, '13.09.2017', 'canal')
    e2 = CreateExpenses(2, 13, 350, '16.09.2017', 'maintenance')
    e3 = CreateExpenses(3, 14, 650, '13.01.2017', 'canal')
    listE = [e1, e2, e3]
    listE = additionCost(listE, get_date(e3), 12)
    new = get_object_by_id(listE, get_ID(e3))


test_createExpense()
test_get_idApartment()
test_get_sumE()
test_get_date()
test_get_typeE()
test_addExpense()
test_remove_expanses()
test_update_expanses()
test_remove_cost()
test_addValue()