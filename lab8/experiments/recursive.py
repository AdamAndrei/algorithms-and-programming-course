def sum_iterative(list):
    k = 0
    for i in range(len(list)):
        k += list[i]
    return k


print(sum_iterative([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def sum_recursive(list):
    if not list:
        return 0
    return list[0] + sum_iterative(list[1:])


def print_recursive(list):
    if not list:
        return
    print_recursive(list[1:])
    print(list[0])


print(sum_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9])
