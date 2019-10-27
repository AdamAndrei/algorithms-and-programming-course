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


def signature(n):
    if abs(n) == n:
        return True
    else:
        return False


def subsequence_three(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0
    for index in range(len(list) - 1):
        if signature(list[index]) != signature(list[index + 1]):
            curentcount += 1
            if curentcount == 1:
                curentstart = index
            if curentcount > bestcount:
                bestcount = curentcount
                beststart = curentstart
        else:
            curentcount = 0
    return list[beststart: beststart + bestcount + 1]


def test_subsequence_three():
    assert (subsequence_three([1, -2, 3, -4, 5, 6, 7, -4, 3, 2]) == [1, -2, 3, -4, 5])


test_subsequence_three()
