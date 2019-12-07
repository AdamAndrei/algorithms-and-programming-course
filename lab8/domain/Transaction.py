from domain.Entity import Entity


class Transaction(Entity):
    def __init__(self, transaction_id, medicine_transacted_id, customer_card_transaction_id, pieces_number, date, time):
        super(Transaction, self).__init__(transaction_id)
        self.__medicine_transacted_id = medicine_transacted_id
        self.__customer_card_transaction_id = customer_card_transaction_id
        self.__pieces_number = pieces_number
        self.__date = date
        self.__time = time

    def __eq__(self, other):
        if not isinstance(other, Transaction):
            return False
        return self.get_id_entity() == other.get_id_entity() and \
            self.__medicine_transacted_id == other.__medicine_transacted_id and \
            self.__customer_card_transaction_id == other.__customer_card_transaction_id and \
            self.__pieces_number == other.__pieces_number and \
            self.__date == other.__date and \
            self.__time == other.__time

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "transaction_id = {} medicine_transacted_id = {} customer_card_transacted_id = {}" \
               " pieces_number = {} " \
               "date = {} time ={}".format(self.get_id_entity(),
                                           self.__medicine_transacted_id,
                                           self.__customer_card_transaction_id,
                                           self.__pieces_number,
                                           self.__date,
                                           self.__time)

    def get_medicine_transacted_id(self):
        return self.__medicine_transacted_id

    def get_customer_card_transaction_id(self):
        return self.__customer_card_transaction_id

    def get_pieces_number(self):
        return self.__pieces_number

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def set_pieces_number(self, new_pieces_number):
        self.__pieces_number = new_pieces_number

    def set_date(self, new_date):
        self.__date = new_date

    def set_time(self, new_time):
        self.__time = new_time

    def get_text_format(self):
        return "{},{},{},{},{},{}".format(self.get_id_entity(),
                                          self.get_medicine_transacted_id(),
                                          self.get_customer_card_transaction_id(),
                                          self.get_pieces_number(),
                                          self.get_date(),
                                          self.get_time())
