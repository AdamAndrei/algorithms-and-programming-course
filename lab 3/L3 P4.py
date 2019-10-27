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
    lenght = len(list)
    list_of_subsenquences = []
    for index in range(lenght):
        for k in range(lenght - index):
            list_of_subsenquences.append(list[index: index + 1 + k])
    return list_of_subsenquences


def get_subsequences_with_length(list_of_subsequences, k):
    subsequence_with_given_length = []
    for subsequnce in list_of_subsequences:
        if len(subsequnce) == k:
            subsequence_with_given_length.append(subsequnce)
    return subsequence_with_given_length


def all_subsequences_ascending_from_list(list):
    all_subsequences = get_all_subsequences(list)
    ascending_subsequences = get_ascending_subsequences(all_subsequences)
    max_length = find_max_length(ascending_subsequences)

    return get_subsequences_with_length(ascending_subsequences, max_length)


def test_all_subsequences_ascending_from_list():
    assert (all_subsequences_ascending_from_list([3, 2, 1]) == [[3], [2], [1]])
    assert (all_subsequences_ascending_from_list([1, 2, 3, 1, 2, 7]) == [[1, 2, 3], [1, 2, 7]])
    assert (all_subsequences_ascending_from_list([2, 3]) == [[2, 3]])
    assert (all_subsequences_ascending_from_list([2]) == [[2]])
    assert (all_subsequences_ascending_from_list([]) == [])


def is_ascending(sequence):
    for index in range(len(sequence) - 1):
        if sequence[index] > sequence[index + 1]:
            return False
    return True


def get_ascending_subsequences(list_of_sequences):
    ascending_subsequences = []
    for sequence in list_of_sequences:
        if is_ascending(sequence):
            ascending_subsequences.append(sequence)

    return ascending_subsequences


# test_subsequence_four()


def test_all_subsequences():
    assert (get_all_subsequences([1]) == [[1]])
    assert (get_all_subsequences([1, 2]) == [[1], [1, 2], [2]])
    assert (get_all_subsequences([1, 2, 3]) == [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]])


# print(get_ascending_subsequences(all_subsequence([1, 2, 3, 1, 5])))


# test_all_subsequences()


def find_max_length(list_of_sequences):
    max_length = 0
    for sequence in list_of_sequences:
        if len(sequence) > max_length:
            max_length = len(sequence)
    return max_length


def test_find_max_length():
    assert (find_max_length([[1], [1, 2], [3, 5]]) == 2)


def test_get_subsequence_with_length():
    assert (get_subsequences_with_length([[1], [1, 2], [3, 5]], 2) == [[1, 2], [3, 5]])
    assert (get_subsequences_with_length([[1], [1, 2], [3, 5]], 1) == [[1]])
    assert (get_subsequences_with_length([[1], [1, 2], [3, 5]], 0) == [])


def test_all():
    test_get_subsequence_with_length()
    test_find_max_length()
    test_all_subsequences()
    test_all_subsequences_ascending_from_list()


print(all_subsequences_ascending_from_list(read_list()))
