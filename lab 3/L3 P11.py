def two_base(a):
    m = 0
    p = 1
    while a > 0:
        r = a % 2
        m = m + (r * p)
        p = p * 10
        a = a // 2
    return m


def bits(number):
    a = two_base(number)
    number_of_one = 0
    while a > 0:
        ld = a % 10
        if ld == 1:
            number_of_one += 1
        a = a // 10
    return number_of_one


def read_list():
    n = int(input("Number of elements=  "))
    list = []

    for index in range(n):
        aux = int(input("\t x = "))
        list.append(aux)
    return list


def print_list(list):
    length = len(list)
    for index in range(length):
        if index == (length - 1):
            print(list[index], "\n")
        else:
            print(list[index], end=" , ")


"""
Description:
        -returneaza o lista cu cea mai lunga subsecventa de numere cu acelasi numar de biti de 1 in scriere binara
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de numere cu acelasi numar de biti de 1 in scriere binara
"""


def get_all_subsequences(list):
    length = len(list)
    list_of_subsequences = []
    for index in range(length):
        for k in range(length - index):
            list_of_subsequences.append(list[index: index + 1 + k])
    return list_of_subsequences


def get_subsequences_with_length(list_of_subsequences, k):
    subsequence_with_given_length = []
    for subsequence in list_of_subsequences:
        if len(subsequence) == k:
            subsequence_with_given_length.append([subsequence])
    return subsequence_with_given_length


def has_same_amount_of_1(sequence):
    for index in range(len(sequence) - 1):
        if bits(sequence[index]) != bits(sequence[index + 1]):
            return False
    return True


def get_subsequences_with_numbers_with_same_amount_of_1(list_of_sequences):
    same_number_of_one_in_subsequences = []
    for sequence in list_of_sequences:
        if has_same_amount_of_1(sequence):
            same_number_of_one_in_subsequences.append(sequence)

    return same_number_of_one_in_subsequences


def find_max_length(list_of_sequences):
    max_length = 0
    for sequence in list_of_sequences:
        if len(sequence) > max_length:
            max_length = len(sequence)
    return max_length


def get_indexes_of_ascending_lists_with_length(list, k):
    """
    Description: get all the indices of the ascending subsequences with maximum length
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
    all_subsequences = get_all_subsequences(list)
    one_subsequences = get_subsequences_with_numbers_with_same_amount_of_1(all_subsequences)
    max_length = find_max_length(one_subsequences)

    return get_indexes_of_ascending_lists_with_length(list, max_length)


print(all_indices_of_subsequences_from_list(read_list()))
