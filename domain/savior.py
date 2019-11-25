# import datetime
#
# from lab8.domain.Transaction import Transaction
# from lab8.domain.TransactionValidator import TransactionValidator
# from lab8.repository.CustomerCardRepository import CustomerCardRepository
# from lab8.repository.MedicineRepository import MedicineRepository
# from lab8.repository.TransactionRepository import TransactionRepository
#
#
# class TransactionService:
#     def __init__(self,
#                  transaction_repository: TransactionRepository,
#                  transaction_validator: TransactionValidator,
#                  customer_card_repository: CustomerCardRepository,
#                  medicine_repository: MedicineRepository):
#         self.__transaction_repository = transaction_repository
#         self.__transaction_validator = transaction_validator
#         self.__customer_card_repository = customer_card_repository
#         self.__medicine_repository = medicine_repository
#
#     def add_transaction(self,
#                         transaction_id,
#                         medicine_transacted_id,
#                         customer_card_transaction_id,
#                         pieces_number,
#                         date,
#                         time):
#         transaction = Transaction(transaction_id,
#                                   medicine_transacted_id,
#                                   customer_card_transaction_id,
#                                   pieces_number,
#                                   date,
#                                   time)
#         self.__transaction_validator.validate_transaction(transaction)
#         self.__transaction_repository.add_transaction(transaction)
#
#     def get_all_transactions(self):
#         found_transactions = []
#         for transaction in self.__transaction_repository.read_all():
#             found_transactions.append(transaction)
#         return found_transactions
#
#     def get_transaction(self, transaction_id):
#         return self.__transaction_repository.read_transaction(transaction_id)
#
#     def update_transaction(self,
#                            new_transaction_id,
#                            new_medicine_transacted_id,
#                            new_customer_card_transaction_id,
#                            new_pieces_number,
#                            new_date,
#                            new_time):
#         transaction = Transaction(new_transaction_id,
#                                   new_medicine_transacted_id,
#                                   new_customer_card_transaction_id,
#                                   new_pieces_number,
#                                   new_date,
#                                   new_time)
#         self.__transaction_validator.validate_transaction(transaction)
#         self.__transaction_repository.update_transaction(transaction)
#
#     def remove_transaction(self, transaction_id):
#         self.__transaction_repository.delete_transaction(transaction_id)
#
#     def get_discount(self, medicine_transacted_id, customer_card_transacted_id, pieces_number):
#         medicine_price = self.__medicine_repository.read_medicine(medicine_transacted_id).get_medicine_price()
#         medicine_recipe = self.__medicine_repository.read_medicine(medicine_transacted_id).get_recipe_need()
#         customer_card_id = customer_card_transacted_id
#         customers_card_id = []
#         found_discount = []
#         for customer_card in self.__customer_card_repository.read_all():
#             found_id = customer_card.get_customer_card_id()
#             customers_card_id.append(found_id)
#         for i in range(len(customers_card_id)):
#             if customer_card_id == int(customers_card_id[i]):
#                 if medicine_recipe:
#                     found_discount.append("15% discount")
#                     medicine_price_one = medicine_price - (medicine_price * (15 / 100))
#                     the_amount_paid = medicine_price_one * pieces_number
#                     found_discount.append(the_amount_paid)
#                 else:
#                     found_discount.append("10% discount")
#                     medicine_price_one = medicine_price - (medicine_price * (10 / 100))
#                     the_amount_paid = medicine_price_one * pieces_number
#                     found_discount.append(the_amount_paid)
#         return found_discount
#
#     @staticmethod
#     def __get_date_in_format(date):
#         date_list = date.split(sep="/")
#         year = int(date_list[2])
#         month = int(date_list[1])
#         day = int(date_list[0])
#         date_in_date_format = datetime.datetime(year, month, day)
#         return date_in_date_format
#
#     def get_transactions_between_two_dates(self, date_one, date_two):
#         list_of_transactions = []
#         date_one_obj = self.__get_date_in_format(date_one)
#         date_two_obj = self.__get_date_in_format(date_two)
#         difference = date_two_obj - date_one_obj
#         for transaction in self.__transaction_repository.read_all():
#             checked_date = self.__get_date_in_format(transaction.get_date())
#             zero_days = datetime.timedelta(0)
#             if difference > zero_days:
#                 if (checked_date - date_one_obj) > zero_days and \
#                         (date_two_obj - checked_date) > zero_days:
#                     list_of_transactions.append(transaction.get_transaction_id())
#             elif difference < zero_days:
#                 if (date_one_obj - checked_date) > zero_days and \
#                         (checked_date - date_two_obj) > zero_days:
#                     list_of_transactions.append(transaction.get_transaction_id())
#             elif difference == zero_days:
#                 list_of_transactions = []
#         return list_of_transactions
#
#     def remove_transactions_between_two_dates(self, date_one, date_two):
#         date_one_obj = self.__get_date_in_format(date_one)
#         date_two_obj = self.__get_date_in_format(date_two)
#         difference = date_two_obj - date_one_obj
#         list_of_transaction_to_remove = []
#         for transaction in self.__transaction_repository.read_all():
#             checked_date = self.__get_date_in_format(transaction.get_date())
#             zero_days = datetime.timedelta(0)
#             if difference > zero_days:
#                 if (checked_date - date_one_obj) > zero_days and \
#                         (date_two_obj - checked_date) > zero_days:
#                     list_of_transaction_to_remove.append(transaction.get_transaction_id())
#             elif difference < zero_days:
#                 if (date_one_obj - checked_date) > zero_days and \
#                         (checked_date - date_two_obj) > zero_days:
#                     list_of_transaction_to_remove.append(transaction.get_transaction_id())
#             elif difference == zero_days:
#                 list_of_transaction_to_remove.append(transaction.get_transaction_id())
#         for i in range(len(list_of_transaction_to_remove)):
#             self.remove_transaction(list_of_transaction_to_remove[i])



# import copy
# import random
# import string
#
# from lab8.domain.Medicine import Medicine
# from lab8.domain.MedicineValidator import MedicineValidator
# from lab8.repository.MedicineRepository import MedicineRepository
# from lab8.repository.TransactionRepository import TransactionRepository
#
#
# class MedicineService:
#     def __init__(self,
#                  medicine_repository: MedicineRepository,
#                  medicine_validator: MedicineValidator,
#                  transaction_repository:TransactionRepository):
#         self.__medicine_repository = medicine_repository
#         self.__medicine_validator = medicine_validator
#         self.__transaction_repository = transaction_repository
#
#     def add_medicine(self,
#                      medicine_id,
#                      medicine_name,
#                      name_medicine_producer,
#                      medicine_price,
#                      recipe_need):
#         medicine = Medicine(medicine_id, medicine_name, name_medicine_producer, medicine_price, recipe_need)
#         self.__medicine_validator.validate_medicine(medicine)
#         self.__medicine_repository.add_medicine(medicine)
#
#     def update_medicine(self,
#                         new_medicine_id,
#                         new_medicine_name,
#                         new_name_medicine_producer,
#                         new_medicine_price,
#                         new_recipe_need):
#         medicine = Medicine(new_medicine_id, new_medicine_name, new_name_medicine_producer, new_medicine_price,
#                             new_recipe_need)
#         self.__medicine_validator.validate_medicine(medicine)
#         self.__medicine_repository.update_medicine(medicine)
#
#     def get_list_of_drugs_that_match(self, the_string):
#         found_medicine = []
#         for medicine in self.__medicine_repository.read_all():
#             if the_string in medicine.get_text_format():
#                 found_medicine.append(medicine)
#         return found_medicine
#
#     def get_all_drugs(self):
#         found_drugs = []
#         for medicine in self.__medicine_repository.read_all():
#             found_drugs.append(medicine)
#         return found_drugs
#
#     def get_medicines_id_in_descending_order_by_pieces_number(self):
#         list_of_drugs = self.__medicine_repository.read_all()
#         max_per_id = {}
#         for transaction in self.__transaction_repository.read_all():
#             medicine_id_in_transaction = transaction.get_medicine_transacted_id()
#             pieces_number_for_medicine = transaction.get_pieces_number()
#             if medicine_id_in_transaction not in max_per_id:
#                 max_per_id[medicine_id_in_transaction] = 0
#             max_per_id[medicine_id_in_transaction] += pieces_number_for_medicine
#         list_of_filtered_drugs = []
#         for drug in list_of_drugs:
#             if drug.get_medicine_id() in max_per_id:
#                 list_of_filtered_drugs.append(drug)
#         for index in range(len(list_of_filtered_drugs) - 1):
#             for k in range(index, len(list_of_filtered_drugs)):
#                 drug_index = list_of_filtered_drugs[index]
#                 drug_k = list_of_filtered_drugs[k]
#                 if max_per_id[drug_index.get_medicine_id()] < max_per_id[drug_k.get_medicine_id()]:
#                     list_of_filtered_drugs[index] = drug_k
#                     list_of_filtered_drugs[k] = drug_index
#         return list_of_filtered_drugs
#
#     def expensive_medicine(self, percentage, maximum_price):
#         list_of_medicines = self.__medicine_repository.read_all()
#         for drug in list_of_medicines:
#             if drug.get_medicine_price() < maximum_price:
#                 expense_price = drug.get_medicine_price() * (1 + percentage / 100)
#                 new_id = drug.get_medicine_id()
#                 new_name = drug.get_medicine_name()
#                 new_producer_name = drug.get_name_medicine_producer()
#                 new_recipe_need = drug.get_recipe_need()
#                 self.update_medicine(new_id, new_name, new_producer_name, expense_price, new_recipe_need)
#
#     def populate(self, n):
#         list_of_id = []
#         for medicine in self.__medicine_repository.read_all():
#             medicine_id = medicine.get_medicine_id()
#             list_of_id.append(medicine_id)
#         sorted_list = sorted(list_of_id)
#         start_id = sorted_list[-1] + 1
#         letters = string.ascii_letters
#         for index in range(n):
#             medicine_name = ''.join(random.choice(letters) for i in range(15))
#             medicine_producer_name = ''.join(random.choice(letters) for i in range(25))
#             medicine_price = float(random.randint(0, 1000))
#             recipe_need = random.choice([True, False])
#             medicine = Medicine(start_id, medicine_name, medicine_producer_name, medicine_price, recipe_need)
#             self.__medicine_validator.validate_medicine(medicine)
#             self.add_medicine(start_id, medicine_name, medicine_producer_name, medicine_price, recipe_need)
#             start_id += 1
#         return self.__medicine_repository.read_all()
#
#

# from datetime import datetime
#
# from lab8.domain.CustomerCard import CustomerCard
# from lab8.domain.CustomerCardValidator import CustomerCardValidator
# from lab8.repository.CustomerCardRepository import CustomerCardRepository
# from lab8.repository.MedicineRepository import MedicineRepository
# from lab8.repository.TransactionRepository import TransactionRepository
#
#
# class CustomerCardService:
#     def __init__(self,
#                  customer_card_repository: CustomerCardRepository,
#                  customer_card_validator: CustomerCardValidator,
#                  transaction_repository: TransactionRepository,
#                  medicine_repository: MedicineRepository):
#         self.__customer_card_repository = customer_card_repository
#         self.__customer_card_validator = customer_card_validator
#         self.__transaction_repository = transaction_repository
#         self.__medicine_repository = medicine_repository
#
#     def add_customer_card(self,
#                           customer_card_id,
#                           customer_name,
#                           customer_first_name,
#                           customer_cnp,
#                           birth_date,
#                           registration_date):
#         customer_card = CustomerCard(customer_card_id,
#                                      customer_name,
#                                      customer_first_name,
#                                      customer_cnp,
#                                      birth_date,
#                                      registration_date)
#         self.__customer_card_validator.validate_customer_card(customer_card)
#         self.__customer_card_repository.add_customer_card(customer_card)
#
#     def get_list_of_customer_cards_that_match(self, string):
#         found_customer_cards = []
#         for customer_card in self.__customer_card_repository.read_all():
#             if string in customer_card.get_text_format():
#                 found_customer_cards.append(customer_card)
#         return found_customer_cards
#
#     def get_all_cards(self):
#         found_cards = []
#         for card in self.__customer_card_repository.read_all():
#             found_cards.append(card)
#         return found_cards
#
#     def get_customer_cards_in_descending_order_by_discount(self):
#         list_of_customer_cards = self.__customer_card_repository.read_all()
#         max_per_id = {}
#         list_of_card_id = []
#         for card in self.__customer_card_repository.read_all():
#             list_of_card_id.append(card.get_customer_card_id())
#         for transaction in self.__transaction_repository.read_all():
#             if transaction.get_customer_card_transaction_id() in list_of_card_id:
#                 medicine = self.__medicine_repository.read_medicine(transaction.get_medicine_transacted_id())
#                 if medicine.get_recipe_need():
#                     amount_of_discount = transaction.get_pieces_number() * ((15 * medicine.get_medicine_price()) / 100)
#                     if transaction.get_customer_card_transaction_id() not in max_per_id:
#                         max_per_id[transaction.get_customer_card_transaction_id()] = 0
#                     max_per_id[transaction.get_customer_card_transaction_id()] += amount_of_discount
#                 else:
#                     amount_of_discount = transaction.get_pieces_number() * ((10 * medicine.get_medicine_price()) / 100)
#                     if transaction.get_customer_card_transaction_id() not in max_per_id:
#                         max_per_id[transaction.get_customer_card_transaction_id()] = 0
#                     max_per_id[transaction.get_customer_card_transaction_id()] += amount_of_discount
#         list_of_filtered_customer_cards = []
#         for card in list_of_customer_cards:
#             if card.get_customer_card_id() in max_per_id:
#                 list_of_filtered_customer_cards.append(card)
#         for index in range(len(list_of_filtered_customer_cards) - 1):
#             for k in range(index, len(list_of_filtered_customer_cards)):
#                 card_index = list_of_filtered_customer_cards[index]
#                 card_k = list_of_filtered_customer_cards[k]
#                 if max_per_id[card_index.get_customer_card_id()] < max_per_id[card_k.get_customer_card_id()]:
#                     list_of_filtered_customer_cards[index] = card_k
#                     list_of_filtered_customer_cards[k] = card_index
#         return list_of_filtered_customer_cards
#
#
#
# #
# from lab8.domain.CustomerCardValidator import CustomerCardValidator
# from lab8.domain.MedicineValidator import MedicineValidator
# from lab8.domain.TransactionValidator import TransactionValidator
# from lab8.repository.CustomerCardRepository import CustomerCardRepository
# from lab8.repository.MedicineRepository import MedicineRepository
# from lab8.repository.TransactionRepository import TransactionRepository
# from lab8.service.CustomerCardService import CustomerCardService
# from lab8.service.MedicineService import MedicineService
# from lab8.service.TransactionService import TransactionService
# from lab8.user_interface.Console import Console
#
#
# def main():
#     medicine_repository = MedicineRepository("drugs.txt")
#     medicine_validator = MedicineValidator()
#     customer_card_repository = CustomerCardRepository("cards.txt")
#     customer_card_validator = CustomerCardValidator()
#     transaction_repository = TransactionRepository("transactions.txt")
#     transaction_validator = TransactionValidator()
#     medicine_service = MedicineService(medicine_repository,
#                                        medicine_validator,
#                                        transaction_repository)
#     customer_card_service = CustomerCardService(customer_card_repository,
#                                                 customer_card_validator,
#                                                 transaction_repository,
#                                                 medicine_repository)
#     transaction_service = TransactionService(transaction_repository,
#                                              transaction_validator,
#                                              customer_card_repository,
#                                              medicine_repository)
#     ui = Console(medicine_service,
#                  customer_card_service,
#                  transaction_service)
#     ui.run_console()
#
#
# main()

#
# class Medicine:
#     def __init__(self, medicine_id, medicine_name, name_medicine_producer, medicine_price, recipe_need):
#         self.__medicine_id = medicine_id
#         self.__medicine_name = medicine_name
#         self.__name_medicine_producer = name_medicine_producer
#         self.__medicine_price = medicine_price
#         self.__recipe_need = recipe_need
#
#     def __eq__(self, other):
#         if not isinstance(other, Medicine):
#             return False
#         return self.__medicine_id == other.__medicine_id and \
#                self.__medicine_name == other.__medicine_name and \
#                self.__name_medicine_producer == other.__name_medicine_producer and \
#                self.__medicine_price == other.__medicine_price and \
#                self.__recipe_need == other.__recipe_need
#
#     def __ne__(self, other):
#         return not (self == other)
#
#     def __str__(self):
#         return "id_medicine = {}, medicine_name = {}, name_medicine_producer = {}, medicine_price = {}," \
#                "recipe_need = {}".format(self.__medicine_id,
#                                          self.__medicine_name,
#                                          self.__name_medicine_producer,
#                                          self.__medicine_price,
#                                          self.__recipe_need)
#
#     def get_medicine_id(self):
#         return self.__medicine_id
#
#     def get_medicine_name(self):
#         return self.__medicine_name
#
#     def get_name_medicine_producer(self):
#         return self.__name_medicine_producer
#
#     def get_medicine_price(self):
#         return self.__medicine_price
#
#     def get_recipe_need(self):
#         return self.__recipe_need
#
#     def set_medicine_name(self, new_medicine_name):
#         self.__medicine_name = new_medicine_name
#
#     def set_name_medicine_producer(self, new_name_medicine_producer):
#         self.__name_medicine_producer = new_name_medicine_producer
#
#     def set_medicine_price(self, new_medicine_price):
#         self.__medicine_price = new_medicine_price
#
#     def set_recipe_need(self, new_recipe_need):
#         self.__recipe_need = new_recipe_need
#
#     def get_text_format(self):
#         return "{},{},{},{},{}".format(self.get_medicine_id(),
#                                        self.get_medicine_name(),
#                                        self.get_name_medicine_producer(),
#                                        self.get_medicine_price(),
#                                        self.get_recipe_need())

#
# class Transaction:
#     def __init__(self, transaction_id, medicine_transacted_id, customer_card_transaction_id, pieces_number, date, time):
#         self.__transaction_id = transaction_id
#         self.__medicine_transacted_id = medicine_transacted_id
#         self.__customer_card_transaction_id = customer_card_transaction_id
#         self.__pieces_number = pieces_number
#         self.__date = date
#         self.__time = time
#
#     def __eq__(self, other):
#         if not isinstance(other, Transaction):
#             return False
#         return self.__transaction_id == other.__transaction_id and \
#                self.__medicine_transacted_id == other.__medicine_transacted_id and \
#                self.__customer_card_transaction_id == other.__customer_card_transaction_id and\
#                self.__pieces_number == other.__pieces_number and \
#                self.__date == other.__date and\
#                self.__time == other.__time
#
#     def __ne__(self, other):
#         return not(self == other)
#
#     def __str__(self):
#         return"transaction_id = {}, medicine_transacted_id = {}, customer_card_transacted_id = {}, pieces_number = {}" \
#               "date = {}, time ={}".format(self.__transaction_id,
#                                            self.__medicine_transacted_id,
#                                            self.__customer_card_transaction_id,
#                                            self.__pieces_number,
#                                            self.__date,
#                                            self.__time)
#
#     def get_transaction_id(self):
#         return self.__transaction_id
#
#     def get_medicine_transacted_id(self):
#         return self.__medicine_transacted_id
#
#     def get_customer_card_transaction_id(self):
#         return self.__customer_card_transaction_id
#
#     def get_pieces_number(self):
#         return self.__pieces_number
#
#     def get_date(self):
#         return self.__date
#
#     def get_time(self):
#         return self.__time
#
#     def set_pieces_number(self, new_pieces_number):
#         self.__pieces_number = new_pieces_number
#
#     def set_date(self, new_date):
#         self.__date = new_date
#
#     def set_time(self, new_time):
#         self.__time = new_time