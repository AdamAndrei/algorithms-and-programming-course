def read_list():
    n = int(input("Number of elements=  "))
    lista = []

    for index in range(n):
        aux = int(input("\t x = "))
        lista.append(aux)
    return lista


def get_all_subsequences(list):
    list_of_subsequences = []
    length = len(list)
    for index in range(length):
        for k in range(length - index):
            list_of_subsequences.append(list[index: index + 1 + k])
    return list_of_subsequences


def give_number():
    n = int(input("Give me number:"))
    return n


def subsequences_with_arithmetic_mean_lower_than_k(list_of_subsequences, k):
    import math
    list_of_good_list = []
    for subsequence in list_of_subsequences:
        if (math.fsum(subsequence) / len(subsequence)) <= k:
            list_of_good_list.append(subsequence)
    return list_of_good_list


# print(subsequences_with_arithmetic_mean_lower_than_k(get_all_subsequences(read_list()), give_number()))


"""
Description:
        -creeaza un meniu
"""


def print_menu():
    print("1 - Citire date")
    print("2 - Subsecventele care au media elementelor mai mica decat un numar dat:")
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
            print(subsequences_with_arithmetic_mean_lower_than_k(get_all_subsequences(list), give_number()))
        elif chosennumber == 3:
            break
        print_menu()
        chosennumber = int(input("Numarul este: "))


main()
