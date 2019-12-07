from domain.Transaction import Transaction
from exception.InvalidIdException import InvalidIdException
from exception.InvalidTransactionException import InvalidTransactionException


class TransactionValidator:
    @staticmethod
    def validate_transaction(transaction: Transaction):
        """
        Function verify if an object respects some conditions and if it finds an irregularity raise an exception
        :param transaction: an Transaction object
        :return: exceptions
        """
        if not isinstance(transaction.get_id_entity(), int):
            raise InvalidIdException("Transaction id = {} is not int".format(transaction.get_id_entity()))
        if not isinstance(transaction.get_medicine_transacted_id(), int):
            raise InvalidIdException("Medicine id = {} is not "
                                     "int".format(transaction.get_medicine_transacted_id()))
        if transaction.get_customer_card_transaction_id() != '':
            if not isinstance(transaction.get_customer_card_transaction_id(), int):
                raise InvalidIdException("Customer id = {} is not "
                                         "int".format(transaction.get_customer_card_transaction_id()))
        if not isinstance(transaction.get_pieces_number(), int):
            raise InvalidTransactionException("Pieces number of drugs = {} is not"
                                              " int".format(transaction.get_pieces_number()))
        if not isinstance(transaction.get_time(), float):
            raise InvalidTransactionException("Time = {} is not float".format(transaction.get_time()))
        if "/" not in transaction.get_date():
            raise InvalidTransactionException("Please use / for writing date")
        if len("{}".format(transaction.get_date())) < 5:
            raise InvalidTransactionException("This is not a valid date")
        date = transaction.get_date().split(sep="/")
        if len(date) != 3:
            raise InvalidTransactionException("Use only 2 /")
        if int(date[0]) < 1 or int(date[0]) > 31:
            raise InvalidTransactionException("Day {} must be between 1 and 31".format(int(date[0])))
        if int(date[1]) < 1 or int(date[1]) > 12:
            raise InvalidTransactionException("Month {} must be between 1 and 12".format(int(date[1])))
        if int(date[2]) > 2019:
            raise InvalidTransactionException("Year {} cannot be in the future".format(int(date[2])))

    @staticmethod
    def validate_date(date):
        """
        Function verify if a date id valid
        :param date: string
        :return: raise exceptions if date doesn't respects some conditions
        """
        date = date.split(sep="/")
        if len(date) != 3:
            raise InvalidTransactionException("Use only 2 /")
        if int(date[0]) < 1 or int(date[0]) > 31:
            raise InvalidTransactionException("Day {} must be between 1 and 31".format(int(date[0])))
        if int(date[1]) < 1 or int(date[1]) > 12:
            raise InvalidTransactionException("Month {} must be between 1 and 12".format(int(date[1])))
        if int(date[2]) > 2019:
            raise InvalidTransactionException("Year {} cannot be in the future".format(int(date[2])))
