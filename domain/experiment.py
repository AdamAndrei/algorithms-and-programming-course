# x = input("x = ")
# y = input("y =")
# if y in x:
#     print("da")
# else:
#     print("nu")
#
#
# def to_string(a, b, c, d, e):
#     return "{},{},{},{},{}".format(a, b, c, d, e)
#
# def a():
#     if 'asd' in to_string(1, "asd", "d", "1", 2):
#         return "da"
#     else:
#         return None
#
#
# print(to_string(1, "a", "s", "d", 2))
# print(a())
#
#
# if '1a' in to_string(1, "a", "s", "d", 2):
#     print("oooo")
# else:
#     print("ppp")


# def get_date_int(date):
#     list_of_date = date.split(sep="/")
#     int_date = int(list_of_date[1]) * (10 ** 6) + int(list_of_date[0]) * (10 ** 4) + int(list_of_date[2])
#     return int_date
#
#
# print(get_date_int("01/01/2001"))
# print(get_date_int("01/11/2001"))
# print(get_date_int("02/01/2001"))
# print(get_date_int("03/01/2001"))
# print(get_date_int("04/01/2001"))
# print(get_date_int("01/02/2001"))
# print(get_date_int("01/03/2001"))
# print(get_date_int("01/04/2001"))
# print(get_date_int("01/05/2001"))
# print(get_date_int("01/06/2001"))
# print(get_date_int("01/07/2001"))
# print(get_date_int("01/08/2001"))
# print(get_date_int("01/09/2001"))
# print(get_date_int("01/10/2001"))
# print(get_date_int("01/11/2001"))
# print(get_date_int("01/12/2001"))
# print(get_date_int("01/12/2001"))
#        medicine_recipe = self.__medicine_repository.read_medicine(medicine_transacted_id).get_recipe_need()

# if not medicine.get_recipe():
#     medicine_name = medicine.get_medicine_name()
#     medicine_producer_name = medicine.get_name_medicine_producer()
#     medicine_price = medicine.get_medicine_price() - medicine.get_medicine_price() / 10
#     medicine_recipe_need = medicine.get_recipe_need()
#     self.__medicine_service.update_medicine(medicine_id, medicine_name, medicine_producer_name,
#                                             medicine_price,
#                                             medicine_recipe_need)
# else:
#     medicine_name = medicine.get_medicine_name()
#     medicine_producer_name = medicine.get_name_medicine_producer()
#     medicine_price = medicine.get_medicine_price() - medicine.get_medicine_price() / 15
#     medicine_recipe_need = medicine.get_recipe_need()
#     self.__medicine_service.update_medicine(medicine_id, medicine_name, medicine_producer_name,
#                                             medicine_price,
#                                             medicine_recipe_need)
#
# def __add_transaction(self):
#     try:
#         transaction_id = int(input("transaction id = "))
#         medicine_transacted_id = int(input("medicine transacted id = "))
#         customer_card_transacted_id = int(input("customer card transacted id ="))
#         pieces_number = int(input("pieces number = "))
#         date = input("date = ")
#         time = int(input("time ="))
#         self.__transaction_service.add_transaction(transaction_id, medicine_transacted_id,
#                                                    customer_card_transacted_id, pieces_number, date, time)
#         medicine_price = self.__medicine_repository.read_medicine(medicine_transacted_id).get_medicine_price()
#         medicine_recipe = self.__medicine_repository.read_medicine(medicine_transacted_id).get_recipe_need()
#         if medicine_recipe:
#             print("Reducere de 15%")
#             medicine_price_one = medicine_price - (medicine_price / 15)
#             the_amount_paid = medicine_price_one * pieces_number
#             print(the_amount_paid)
#         else:
#             print("Reducere de 10%")
#             medicine_price_one = medicine_price - (medicine_price / 10)
#             the_amount_paid = medicine_price_one * pieces_number
#             print(the_amount_paid)
#         print("Transaction added!")
#     except ValueError as ve:
#         print("Error", ve)
#     except KeyError:
#         print("ID already exists")


# list_of_drugs = self.__medicine_repository.read_all()
# max_per_id = {}
# for transaction in self.__transaction_repository.read_all():
#     medicine_id_in_transaction = transaction.get_medicine_transacted_id()
#     pieces_number_for_medicine = transaction.get_pieces_number()
#     if medicine_id_in_transaction not in max_per_id:
#         max_per_id[medicine_id_in_transaction] = 0
#     max_per_id[medicine_id_in_transaction] = pieces_number_for_medicine
# list_of_filtered_drugs = []
# for drug in list_of_drugs:
#     if drug.get_medicine_id() in max_per_id:
#         list_of_filtered_drugs.append(drug)
# over_filtered_drugs = []
# for filtered_drug in list_of_filtered_drugs:
#     id_drug_one = filtered_drug.get_medicine_id()
#     filtered_dictionary = {}
#     for key in max_per_id:
#         if key != id_drug_one:
#             filtered_dictionary[key] = max_per_id[key]
#     for key in filtered_dictionary:
#         id_drug = filtered_drug.get_medicine_id()
#         copy_max_per_id = copy.deepcopy(max_per_id)
#         if copy_max_per_id[id_drug] >= filtered_dictionary[key]:
#             over_filtered_drugs.append(self.__medicine_repository.read_medicine(id_drug))
#             del (copy_max_per_id, id_drug)
# return over_filtered_drugs

#
# def get_date_int(self, date):
#     list_of_date = date.split(sep="/")
#     int_date = list_of_date[0] * (10 ** 6) + list_of_date[1] * (10 ** 4) + list_of_date[2]
#     return int_date
# import datetime
#
#
# def get_dates(date_one, date_two):
#     date_one_list = date_one.split(sep="/")
#     date_two_list = date_two.split(sep="/")
#     year = int(date_one_list[2])
#     month = int(date_one_list[1])
#     day = int(date_one_list[0])
#     date_one_date = datetime.datetime(year, month, day)
#     year_2 = int(date_two_list[2])
#     month_2 = int(date_two_list[1])
#     day_2 = int(date_two_list[0])
#     date_two_date = datetime.datetime(year_2, month_2, day_2)
#     date_interval = date_two_date - date_one_date
#     if date_interval > datetime.timedelta(0):
#         return date_interval
#
#
# print(get_dates("12/12/2010", "15/12/2011"))
#
#
# def get_transactions_between_two_dates(self, date_one, date_two):
#     list_of_transactions = []
#     difference = self.__get_date_in_format(date_two) - self.__get_date_in_format(date_one)
#     for transaction in self.__transaction_repository.read_all():
#         if difference > datetime.timedelta(0):
#             if abs(self.__get_date_in_format(date_two) - self.__get_date_in_format(transaction.get_date())) < \
#                     difference:
#                 list_of_transactions.append(transaction.get_transaction_id())
#         elif difference < datetime.timedelta(0):
#             if abs(self.__get_date_in_format(date_one) - self.__get_date_in_format(transaction.get_date())) < \
#                     difference:
#                 list_of_transactions.append(transaction.get_transaction_id())
#         elif difference == datetime.timedelta(0):
#             list_of_transactions = []
#         return list_of_transactions
