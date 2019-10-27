def test_find_longest_palindrome():
    assert(find_longest_palindrome(['123', '111121111', '121', 'abcdcba']) == '111121111')


def get_all_subsequences(list):
    lenght = len(list)
    list_of_subsenquences = []
    for index in range(lenght):
            list_of_subsenquences.append(list[index: index + 1])
    return list_of_subsenquences


def reverse(s):
    return s[::-1]


def is_palindrome(s):
    # Calling reverse function
    rev = reverse(s)

    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False


def get_palindrome_subsequences(list_of_subsequences):
    list_of_palindrome_subsequences = []
    for palindrome_subsequence in list_of_subsequences:
        if is_palindrome(palindrome_subsequence):
            list_of_palindrome_subsequences.append(palindrome_subsequence)
    return list_of_palindrome_subsequences


def find_longest_palindrome(list):
    list_version = list[0]
    for index in range(len(list) - 1):
        if len(list[index]) < len(list[index + 1]):
            list_version = list[index + 1]
    return list_version

def first_caracter(n):
    if (n[0]) in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False

def string_start_cipher(list):
    for index in range (len(list)):
        if first_caracter(list[index]):
            return True
    return False


def start_cipher_subsequence(list):
    list_of_cipher_subsequences = []
    for subsequence in list:
        if string_start_cipher(subsequence):
            list_of_cipher_subsequences.append(subsequence)
    return list_of_cipher_subsequences


def find_shortest_string(list):
    shortest = list[0]
    for index in range(len(list) - 1):
        if len(list[index]) > len(list[index + 1]):
            shortest = list[index + 1]
    return shortest





"""
Description:
        -citeste o lista de string-uri
Out:
        -o lista de string-uri

"""


def read_list():
    n = int(input("Number of elements=  "))
    lista = []

    for index in range(n):
        aux = (input("\t x = "))
        lista.append(aux)
    return lista

print(find_shortest_string(start_cipher_subsequence(read_list())))


"""
Description:
        -creeaza un meniu
"""


def print_menu():
    print("1 - Citire date:")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - Iesire")


"""
Description:
        -functia principala



def main():
    print_menu()
    chosennumber = int(input("Numarul citit= "))
    list = []
    while chosennumber != 6:
        if chosennumber == 1:
            list = read_list()
        elif chosennumber == 2:
            print(find_longest_palindrome(get_all_subsequences(read_list())))
        elif chosennumber == 3:

        elif chosennumber == 4:

        elif chosennumber == 5:

        elif chosennumber == 6:
            break
        print_menu()
        chosennumber = int(input("Numarul este: "))
"""

