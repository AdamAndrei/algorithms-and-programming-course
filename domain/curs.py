from copy import deepcopy


def bubblesort(list):
    list = deepcopy(list)
    swapped = True
    count = 1
    while swapped:
        swapped = False
        for i in range (len(list) - 1):
            if list[i] < list[i+1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True
        if swapped:
            count += 1
    return list

print(bubblesort([23, 2, 100, 234, 24]))


def insertion_sort(list):
    list = deepcopy(list)
    for i in range (1, len(list)):
        # lista[0] > lista[1] > lista[2] > ...
        for j in range(i):
            if list[i] > list[j]:
                list.insert(j, list[i])
                del list[i + 1]
                break
    return list

print(insertion_sort([1, 4, 89, 54, 67, 23, 100]))


#quick sort
# foloseste functia de partitie
#

def pseudo_quick_sort(list, key=lambda x: x, reverse=False):

    if list == []:
        return []
    pivot = key(list[0])
    less_than_pivot = [nr for nr in list if key(nr) < pivot]
    equals_than_pivot = [nr for nr in list if key(nr) == pivot]
    greater_than_pivot = [nr for nr in list if key(nr) > pivot]

    return pseudo_quick_sort(less_than_pivot, key=key) + equals_than_pivot + pseudo_quick_sort(greater_than_pivot, key=key)


print(pseudo_quick_sort([1, 5, 2, 67, 45, 100, 34], key=lambda x: -x))



def merge_sort(list, cmp=lambda x, y: x < y):
    def merge(list, st, m, dr):
        merged_list = []
        i, j = st, m + 1
        while i <= m and j <= dr:
            if cmp(list[i], list[j]):
                merged_list.append(list[i])
                i += 1
            else:
                merged_list.append(list[j])
                j += 1
        merged_list += list[i:m + 1]
        merged_list += list[j:dr + 1]
        list[st:dr + 1] = merged_list

    def inner(list, st, dr):
        if st == dr:
            return
        m = (st + dr) // 2
        inner(list, st, m)
        inner(list, m + 1, dr)
        merge(list, st, m, dr)

    inner(list, 0, len(list) - 1)
    return list


print(merge_sort([1, 89, 34, 23, 67], cmp=lambda x, y: x > y))


list = [1, 5, 3, 89, 23, 45, 12, 100]
sorted(list, key=lambda x: -x)
print(list)

def benchmark(algoritm):
    from random import randint
    from time import time
    lst =[]
    for i in range(10000):
        lst.append(randint(10, 100000000))
    start = time()
    result = algoritm(lst)
    end = time()
    assert result == sorted(lst)
    print(end - start)

benchmark(bubblesort)