from datetime import datetime

from lab8.domain.CustomerCard import CustomerCard
from lab8.domain.CustomerCardValidator import CustomerCardValidator
from lab8.repository.CustomerCardRepository import CustomerCardRepository
from lab8.repository.MedicineRepository import MedicineRepository
from lab8.repository.TransactionRepository import TransactionRepository


class CustomerCardService:
    def __init__(self,
                 customer_card_repository: CustomerCardRepository,
                 customer_card_validator: CustomerCardValidator,
                 transaction_repository: TransactionRepository,
                 medicine_repository: MedicineRepository):
        self.__customer_card_repository = customer_card_repository
        self.__customer_card_validator = customer_card_validator
        self.__transaction_repository = transaction_repository
        self.__medicine_repository = medicine_repository

    def add_customer_card(self,
                          customer_card_id,
                          customer_name,
                          customer_first_name,
                          customer_cnp,
                          birth_date,
                          registration_date):
        customer_card = CustomerCard(customer_card_id,
                                     customer_name,
                                     customer_first_name,
                                     customer_cnp,
                                     birth_date,
                                     registration_date)
        self.__customer_card_validator.validate_customer_card(customer_card)
        self.__customer_card_repository.add(customer_card)

    def get_list_of_customer_cards_that_match(self, string):
        found_customer_cards = []
        for customer_card in self.__customer_card_repository.read_all():
            if string in customer_card.get_text_format():
                found_customer_cards.append(customer_card)
        return found_customer_cards

    def get_all_cards(self):
        found_cards = []
        for card in self.__customer_card_repository.read_all():
            found_cards.append(card)
        return found_cards

    def get_customer_cards_in_descending_order_by_discount(self):
        list_of_customer_cards = self.__customer_card_repository.read_all()
        max_per_id = {}
        list_of_card_id = []
        for card in self.__customer_card_repository.read_all():
            list_of_card_id.append(card.get_customer_card_id())
        for transaction in self.__transaction_repository.read_all():
            if transaction.get_customer_card_transaction_id() in list_of_card_id:
                medicine = self.__medicine_repository.read_by_id(transaction.get_medicine_transacted_id())
                if medicine.get_recipe_need():
                    amount_of_discount = transaction.get_pieces_number() * ((15 * medicine.get_medicine_price()) / 100)
                    if transaction.get_customer_card_transaction_id() not in max_per_id:
                        max_per_id[transaction.get_customer_card_transaction_id()] = 0
                    max_per_id[transaction.get_customer_card_transaction_id()] += amount_of_discount
                else:
                    amount_of_discount = transaction.get_pieces_number() * ((10 * medicine.get_medicine_price()) / 100)
                    if transaction.get_customer_card_transaction_id() not in max_per_id:
                        max_per_id[transaction.get_customer_card_transaction_id()] = 0
                    max_per_id[transaction.get_customer_card_transaction_id()] += amount_of_discount
        list_of_filtered_customer_cards = []
        for card in list_of_customer_cards:
            if card.get_customer_card_id() in max_per_id:
                list_of_filtered_customer_cards.append(card)
        for index in range(len(list_of_filtered_customer_cards) - 1):
            for k in range(index, len(list_of_filtered_customer_cards)):
                card_index = list_of_filtered_customer_cards[index]
                card_k = list_of_filtered_customer_cards[k]
                if max_per_id[card_index.get_customer_card_id()] < max_per_id[card_k.get_customer_card_id()]:
                    list_of_filtered_customer_cards[index] = card_k
                    list_of_filtered_customer_cards[k] = card_index
        return list_of_filtered_customer_cards
