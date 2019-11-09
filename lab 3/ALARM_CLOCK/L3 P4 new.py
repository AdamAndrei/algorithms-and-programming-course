def read_list():
    n = int(input("Number of elements=  "))
    lista = []

    for index in range(n):
        aux = int(input("\t x = "))
        lista.append(aux)
    return lista


def print_list(list):
    length = len(list)
    for index in range(length):
        if index == (length - 1):
            print(list[index], "\n")
        else:
            print(list[index], end=" , ")


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

"""
def get_indexes_of_ascending_lists_with_length(list, k):
    list_of_list_of_indices = []
    for index in range(len(list) - k + 1):
        for p in range(index, index + k):
            if list[index] < list[p]:
                list_of_indices = [index, p]

                list_of_list_of_indices.append(list_of_indices)

    return list_of_list_of_indices
"""


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


print(all_subsequences_ascending_from_list(read_list()))
