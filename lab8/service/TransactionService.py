import datetime

from lab8.domain.Transaction import Transaction
from lab8.domain.TransactionValidator import TransactionValidator
from lab8.repository.CustomerCardRepository import CustomerCardRepository
from lab8.repository.MedicineRepository import MedicineRepository
from lab8.repository.TransactionRepository import TransactionRepository


class TransactionService:
    def __init__(self,
                 transaction_repository: TransactionRepository,
                 transaction_validator: TransactionValidator,
                 customer_card_repository: CustomerCardRepository,
                 medicine_repository: MedicineRepository):
        self.__transaction_repository = transaction_repository
        self.__transaction_validator = transaction_validator
        self.__customer_card_repository = customer_card_repository
        self.__medicine_repository = medicine_repository

    def add_transaction(self,
                        transaction_id,
                        medicine_transacted_id,
                        customer_card_transaction_id,
                        pieces_number,
                        date,
                        time):
        transaction = Transaction(transaction_id,
                                  medicine_transacted_id,
                                  customer_card_transaction_id,
                                  pieces_number,
                                  date,
                                  time)
        self.__transaction_validator.validate_transaction(transaction)
        self.__transaction_repository.create(transaction)

    def get_all_transactions(self):
        found_transactions = []
        for transaction in self.__transaction_repository.read_all():
            found_transactions.append(transaction)
        return found_transactions

    def get_transaction(self, transaction_id):
        return self.__transaction_repository.read_by_id(transaction_id)

    def update_transaction(self,
                           new_transaction_id,
                           new_medicine_transacted_id,
                           new_customer_card_transaction_id,
                           new_pieces_number,
                           new_date,
                           new_time):
        transaction = Transaction(new_transaction_id,
                                  new_medicine_transacted_id,
                                  new_customer_card_transaction_id,
                                  new_pieces_number,
                                  new_date,
                                  new_time)
        self.__transaction_validator.validate_transaction(transaction)
        self.__transaction_repository.update(transaction)

    def remove_transaction(self, transaction_id):
        self.__transaction_repository.delete(transaction_id)

    def get_discount(self, medicine_transacted_id, customer_card_transacted_id, pieces_number):
        medicine_price = self.__medicine_repository.read_by_id(medicine_transacted_id).get_medicine_price()
        medicine_recipe = self.__medicine_repository.read_by_id(medicine_transacted_id).get_recipe_need()
        customer_card_id = customer_card_transacted_id
        customers_card_id = []
        found_discount = []
        for customer_card in self.__customer_card_repository.read_all():
            found_id = customer_card.get_customer_card_id()
            customers_card_id.append(found_id)
        for i in range(len(customers_card_id)):
            if customer_card_id == int(customers_card_id[i]):
                if medicine_recipe:
                    found_discount.append("15% discount")
                    medicine_price_one = medicine_price - (medicine_price * (15 / 100))
                    the_amount_paid = medicine_price_one * pieces_number
                    found_discount.append(the_amount_paid)
                else:
                    found_discount.append("10% discount")
                    medicine_price_one = medicine_price - (medicine_price * (10 / 100))
                    the_amount_paid = medicine_price_one * pieces_number
                    found_discount.append(the_amount_paid)
        return found_discount

    @staticmethod
    def __get_date_in_format(date):
        date_list = date.split(sep="/")
        year = int(date_list[2])
        month = int(date_list[1])
        day = int(date_list[0])
        date_in_date_format = datetime.datetime(year, month, day)
        return date_in_date_format

    def get_transactions_between_two_dates(self, date_one, date_two):
        list_of_transactions = []
        date_one_obj = self.__get_date_in_format(date_one)
        date_two_obj = self.__get_date_in_format(date_two)
        difference = date_two_obj - date_one_obj
        for transaction in self.__transaction_repository.read_all():
            checked_date = self.__get_date_in_format(transaction.get_date())
            zero_days = datetime.timedelta(0)
            if difference > zero_days:
                if (checked_date - date_one_obj) > zero_days and \
                        (date_two_obj - checked_date) > zero_days:
                    list_of_transactions.append(transaction.get_transaction_id())
            elif difference < zero_days:
                if (date_one_obj - checked_date) > zero_days and \
                        (checked_date - date_two_obj) > zero_days:
                    list_of_transactions.append(transaction.get_transaction_id())
            elif difference == zero_days:
                list_of_transactions = []
        return list_of_transactions

    def remove_transactions_between_two_dates(self, date_one, date_two):
        date_one_obj = self.__get_date_in_format(date_one)
        date_two_obj = self.__get_date_in_format(date_two)
        difference = date_two_obj - date_one_obj
        list_of_transaction_to_remove = []
        for transaction in self.__transaction_repository.read_all():
            checked_date = self.__get_date_in_format(transaction.get_date())
            zero_days = datetime.timedelta(0)
            if difference > zero_days:
                if (checked_date - date_one_obj) > zero_days and \
                        (date_two_obj - checked_date) > zero_days:
                    list_of_transaction_to_remove.append(transaction.get_transaction_id())
            elif difference < zero_days:
                if (date_one_obj - checked_date) > zero_days and \
                        (checked_date - date_two_obj) > zero_days:
                    list_of_transaction_to_remove.append(transaction.get_transaction_id())
            elif difference == zero_days:
                list_of_transaction_to_remove.append(transaction.get_transaction_id())
        for i in range(len(list_of_transaction_to_remove)):
            self.remove_transaction(list_of_transaction_to_remove[i])