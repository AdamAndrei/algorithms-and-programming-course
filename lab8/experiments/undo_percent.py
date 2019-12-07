import math
import random


def expense(price, percent):
    expensive_price = price * (1 + percent / 100)
    discounted_price = expensive_price * (1 - ((percent / 100) / ((percent / 100) + 1)))
    # if discounted_price > price:
    #     discounted_price = math.floor(discounted_price)
    # elif discounted_price < price:
    #     discounted_price = math.floor(discounted_price) + 1
    # else:
    #     discounted_price = discounted_price
    return discounted_price


print(expense(100.34, 10))
print(expense(100.23, 11))
print(expense(100.56, 12))
print(expense(99.12, 100))
print(expense(100, 102))
print(expense(100, 99))
print(expense(100, 98))
list = [1, 2, 3, 4, 5]
medicine_transacted_id = random.choice(list)
print(medicine_transacted_id + 1)
