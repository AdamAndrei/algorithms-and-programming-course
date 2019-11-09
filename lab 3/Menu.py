def all_tests():
    test_get_all_subsequences()
    test_get_subsequence_with_length()
    test_is_ascending()
    test_get_ascending_subsequences()
    test_find_max_length()
    test_two_base()
    test_bits()
    test_has_same_amount_of_1()
    test_get_subsequences_with_numbers_with_same_amount_of_1()


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
    length = len(list)
    for index in range(length):
        if index == (length - 1):
            print(list[index], "\n")
        else:
            print(list[index], end=" , ")


def test_get_all_subsequences():
    assert len(get_all_subsequences([1, 2, 3])) == 6


def get_all_subsequences(list):
    """
    Description: get all subsequences of list
    :param list: list
    :return: a list of lists
    """
    lenght = len(list)
    list_of_subsenquences = []
    for index in range(lenght):
        for k in range(lenght - index):
            list_of_subsenquences.append(list[index: index + 1 + k])
    return list_of_subsenquences


def test_get_subsequence_with_length():
    assert len(get_subsequences_with_length([[1, 2], [1], [1, 3]], 2)) == 2


def get_subsequences_with_length(list_of_subsequences, k):
    """
    Description: get am subsequences with a given length
    :param list_of_subsequences: list
    :param k: int
    :return: a list of subsequences with a given length
    """
    subsequence_with_given_length = []
    for subsequnce in list_of_subsequences:
        if len(subsequnce) == k:
            subsequence_with_given_length.append([subsequnce])
    return subsequence_with_given_length


def test_is_ascending():
    assert is_ascending([1, 2, 3])
    assert is_ascending([])


def is_ascending(sequence):
    """
    Description: decide if a subsequence is in ascending order
    :param sequence: list
    :return: True if is in ascending order, False otherwise
    """
    for index in range(len(sequence) - 1):
        if sequence[index] > sequence[index + 1]:
            return False
    return True


def test_get_ascending_subsequences():
    assert (len(get_ascending_subsequences([[1, 2, 3], [1, 3, 2], [1, 2]])) == 2)


def get_ascending_subsequences(list_of_sequences):
    """
    Description: get all ascending subsequences
    :param list_of_sequences: list
    :return: a list of lists
    """
    ascending_subsequences = []
    for sequence in list_of_sequences:
        if is_ascending(sequence):
            ascending_subsequences.append(sequence)

    return ascending_subsequences


def test_find_max_length():
    assert (find_max_length([[1, 2, 3], [1, 2], [1, 2, 3, 4]]) == 4)


def find_max_length(list_of_sequences):
    """
    Description: find the length of the longest list in list
    :param list_of_sequences:  list
    :return: The maximum length of ascending subsequences
    """
    max_length = 0
    for sequence in list_of_sequences:
        if len(sequence) > max_length:
            max_length = len(sequence)
    return max_length


def test_get_indexes_of_ascending_lists_with_length():
    assert (get_indexes_of_ascending_lists_with_length([1, 2, 3, 4, 2], 4)[0] == 0)


def get_indexes_of_ascending_lists_with_length(list, k):
    """
    Description: get all the indices of the ascending subsequences with maximum length
    :param list: list
    :param k: int
    :return: a list of list of indices
    """
    list_of_list_of_indices = []
    for index in range(len(list) - k + 1):
        if is_ascending(list[index:index + k]):
            list_of_indices = [index, index + k - 1]
            list_of_list_of_indices.append(list_of_indices)
    return list_of_list_of_indices


def all_subsequences_ascending_from_list(list):
    all_subsequences = get_all_subsequences(list)
    ascending_subsequences = get_ascending_subsequences(all_subsequences)
    max_length = find_max_length(ascending_subsequences)

    return get_indexes_of_ascending_lists_with_length(list, max_length)


"""
Description:
        -transforma un numar din baza 10 in baza 2
In:
        -un numar intreg 
Out:
        -un numar in baza 2
"""


def test_two_base():
    assert two_base(2) == 10


def two_base(a):
    m = 0
    p = 1
    while a > 0:
        r = a % 2
        m = m + (r * p)
        p = p * 10
        a = a // 2
    return m


"""
Description:
        -numara de cate ori apar biti de 1 in scrierea in baza 2
In:
        -un numar in baza 2
Out:
        -un numar intreg
"""


def test_bits():
    assert (bits(2) == 1)


def bits(number):
    a = two_base(number)
    number_of_one = 0
    while a > 0:
        ld = a % 10
        if ld == 1:
            number_of_one += 1
        a = a // 10
    return number_of_one


def test_has_same_amount_of_1():
    assert (has_same_amount_of_1([2, 4, 8]))


def has_same_amount_of_1(sequence):
    """
    Description: decide if one subsequence has all numbers whit the same amount of 1 in 2 base writing
    :param sequence: list
    :return: True if all numbers verify the condition, False otherwise
    """
    for index in range(len(sequence) - 1):
        if bits(sequence[index]) != bits(sequence[index + 1]):
            return False
    return True


def test_get_subsequences_with_numbers_with_same_amount_of_1():
    assert (len(get_subsequences_with_numbers_with_same_amount_of_1([[2, 4], [1, 3]])) == 1)


def get_subsequences_with_numbers_with_same_amount_of_1(list_of_sequences):
    """
    Description: Get subsequences with numbers with same amount of 1
    :param list_of_sequences:list
    :return: list os lists
    """
    same_number_of_one_in_subsequences = []
    for sequence in list_of_sequences:
        if has_same_amount_of_1(sequence):
            same_number_of_one_in_subsequences.append(sequence)

    return same_number_of_one_in_subsequences


def get_indexes_of_lists_with_length(list, k):
    """
    Description: get all the indices of the subsequences with maximum length
    :param list: list
    :param k: int
    :return: a list of list of indices
    """
    list_of_list_of_indices = []
    for index in range(len(list) - k + 1):
        if has_same_amount_of_1(list[index:index + k]):
            list_of_indices = [index, index + k - 1]
            list_of_list_of_indices.append(list_of_indices)
    return list_of_list_of_indices


def all_indices_of_subsequences_from_list(list):
    """
    Description: get the indices od each ascending subsequence with max length
    :param list: list
    :return: list of lists
    """
    all_subsequences = get_all_subsequences(list)
    ascending_subsequences = get_subsequences_with_numbers_with_same_amount_of_1(all_subsequences)
    max_length = find_max_length(ascending_subsequences)

    return get_indexes_of_ascending_lists_with_length(list, max_length)


"""
Description:
        -creeaza un meniu
"""


def print_menu():
    print("1 - Citire date")
    print("2 - Determina indicii de la cele mai lungi subsecvente de numere ordonate crescator:")
    print("3 - Determina indicii de la cele mai lungi subsecventa de numere cu acelasi numar de biti de 1:")
    print("4 - Iesire")


"""
Description:
        -functia principala
"""


def main():
    print_menu()
    chosennumber = int(input("What option do you want: "))
    list = []
    while chosennumber != 4:
        if chosennumber == 1:
            list = read_list()
        elif chosennumber == 2:
            print(all_subsequences_ascending_from_list(list))
        elif chosennumber == 3:
            print(all_indices_of_subsequences_from_list(list))
        elif chosennumber == 4:
            break
        print("")
        print_menu()
        print(" ")
        chosennumber = int(input("what option do you want: "))


all_tests()

main()
