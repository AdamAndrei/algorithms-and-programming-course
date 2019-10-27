def greatest_common_factor():
    a = int(input("First number = "))
    b = int(input("Second number ="))
    while a != b:
        if a>b:
            a = a - b
        else:
            b = b - a
    print(a)


def greatest_common_factor_version2():
    a = int(input("First number = "))
    b = int(input("Second number ="))

    while b != 0:
        r = b
        b = a % b
        a = r
    print(a)


greatest_common_factor_version2()