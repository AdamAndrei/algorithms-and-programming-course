from lab8.domain.Transaction import Transaction


class TransactionValidator:
    def validate_transaction(self, transaction: Transaction):
        if not isinstance(transaction.get_transaction_id(), int):
            raise ValueError("Transaction id = {} is not int".format(transaction.get_transaction_id()))
        if not isinstance(transaction.get_medicine_transacted_id(), int):
            raise ValueError("Medicine id = {} is not "
                             "int".format(transaction.get_medicine_transacted_id()))
        if transaction.get_customer_card_transaction_id() != '':
            if not isinstance(transaction.get_customer_card_transaction_id(), int):
                raise ValueError("Customer id = {} is not "
                                 "int".format(transaction.get_customer_card_transaction_id()))
        if not isinstance(transaction.get_pieces_number(), int):
            raise ValueError("Pieces number of drugs = {} is not"
                             " int".format(transaction.get_pieces_number()))
        if not isinstance(transaction.get_time(), float):
            raise ValueError("Time = {} is not float".format(transaction.get_time()))
        if "/" not in transaction.get_date():
            raise ValueError("Please use / for writing date")
        if len("{}".format(transaction.get_date())) < 5:
            raise ValueError("This is not a valid date")
        date = transaction.get_date().split(sep="/")
        if len(date) != 3:
            raise ValueError("Use only 2 /")
        if int(date[0]) < 1 or int(date[0]) > 31:
            raise ValueError("Day {} must be between 1 and 31".format(int(date[0])))
        if int(date[1]) < 1 or int(date[1]) > 12:
            raise ValueError("Month {} must be between 1 and 12".format(int(date[1])))
        if int(date[2]) > 2019:
            raise ValueError("Year {} cannot be in the future".format(int(date[2])))
