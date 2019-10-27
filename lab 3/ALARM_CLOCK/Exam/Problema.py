def test_is_palindrome():
    assert (is_palindrome(121))
    assert (not is_palindrome(123))
    assert (is_palindrome(323))


def test_find_list_of_palindrome():
    assert (find_list_of_palindrome([11, 134, 121, 131, 676]) == [11, 121, 131, 676])
    assert (find_list_of_palindrome([11, 134, 121, 131, 54, 564]) == [11, 121, 131])


"""
Description:
        -citeste o lista de numere intregi
Out:
        -o lista de numere intregi

"""


def read_list():
    n = int(input("Number of elements=  "))
    lista = []

    for index in range(n):
        aux = int(input("\t x = "))
        lista.append(aux)
    return lista


"""
Description:
        -afiseaza o lista de numere intregi
Out:
        -o lista de numere intregi

"""


def print_list(list):
    lista = []
    length = len(list)
    for index in range(length):
        if index == (length - 1):
            print(list[index], "\n")
        else:
            print(list[index], end=" , ")


def is_palindrome(x):
    ogl = 0
    n = x
    while n > 0:
        ld = n % 10
        ogl = ogl * 10 + ld
        n = n // 10
    if x == ogl:
        return True
    else:
        return False


def find_list_of_palindrome(list):
    list_of_palindrome = []
    for index in range(len(list)):
        if is_palindrome(list[index]):
            list_of_palindrome.append(list[index])
    return list_of_palindrome


def find_last_of_list_of_palindrome(list_of_palindrome):
    k = len(list_of_palindrome)
    print(list_of_palindrome[k - 1])


def find_max_of_list_of_palindrome(list_of_palindrome):
    maxim = 0
    for index in range(len(list_of_palindrome)):
        if list_of_palindrome[index] > maxim:
            maxim = list_of_palindrome[index]
    print(maxim)

"""
test_is_palindrome()
test_find_list_of_palindrome()

find_last_of_list_of_palindrome(find_list_of_palindrome(read_list()))
"""


def number_of_divisors(n):
    number_of_divisors = 0
    for d in range(1, n + 1):
        if (n % d) == 0:
            number_of_divisors += 1
    return number_of_divisors


def find_list_of_semiprime_numbers(list):
    list_of_semiprime_numbers = []
    for index in range(len(list)):
        if number_of_divisors(list[index]) == 3:
            list_of_semiprime_numbers.append(list[index])
    return list_of_semiprime_numbers


def find_minimum_of_list_of_semiprime_numbers(list_of_semiprime_numbers):
    if len(list_of_semiprime_numbers) == 0:
        return None
    minim = list_of_semiprime_numbers[0]
    for index in range(len(list_of_semiprime_numbers)):
        if list_of_semiprime_numbers[index] < minim:
            minim = list_of_semiprime_numbers[index]
    print(minim)


"""
find_minimum_of_list_of_semiprime_numbers(find_list_of_semiprime_numbers(read_list()))
"""


def odd_digits(n):
    number_of_digits = 0
    number_of_odd_digits = 0
    while n > 0:
        ld = n % 10
        if ld % 2 == 1:
            number_of_odd_digits += 1
        number_of_digits += 1
        n = n // 10
    if number_of_digits == number_of_odd_digits:
        return True
    else:
        return False


def find_all_numbers_compound_of_odd_digits(list):
    list_of_odd = []
    for index in range(len(list)):
        if odd_digits(list[index]):
            list_of_odd.append(list[index])
    print_list(list_of_odd)


def change_odd_numbers(list):
    import math
    for index in range(len(list)):
        if (list[index] % 2) == 1:
            list[index] = [math.floor(math.sqrt(list[index])), list[index] ** 2]
    print(list)

""" 
find_all_numbers_compound_of_odd_digits(read_list())
"""

"""
Description:
        -creeaza un meniu
"""


def print_menu():
    print("1 - Citire date")
    print("2 - Afiseaza ultimul numar palindrom din lista:")
    print("3 - Afiseaza cel mai mic numar semiprim:")
    print("4 - Afiseaza toate numerele formate din cifre impare:")
    print("5 - Inlocuieste numerele impare cu o lista care contine partea intreaga a radacinii numarului si patratul "
          "sau"
          )
    print("6 - Iesire")


"""
Description:
        -functia principala
"""


def main():
    print_menu()
    chosennumber = int(input("Numarul citit= "))
    list = []
    while chosennumber != 6:
        if chosennumber == 1:
            list = read_list()
        elif chosennumber == 2:
            find_last_of_list_of_palindrome(find_list_of_palindrome(list))
        elif chosennumber == 3:
            find_minimum_of_list_of_semiprime_numbers(find_list_of_semiprime_numbers(list))
        elif chosennumber == 4:
            find_all_numbers_compound_of_odd_digits(list)
        elif chosennumber == 5:
            change_odd_numbers(list)
        elif chosennumber == 6:
            break
        print_menu()
        chosennumber = int(input("Numarul este: "))


main()
