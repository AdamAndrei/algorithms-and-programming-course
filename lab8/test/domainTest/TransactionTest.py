import unittest

from lab8.domain.Transaction import Transaction


class TransactionTest(unittest.TestCase):
    def test_equal(self):
        transaction_one = Transaction(1, 2, 3, 12, "11/11/1111", 12.12)
        transaction_two = Transaction(1, 2, 3, 12, "11/11/1111", 12.12)
        self.assertEqual(transaction_one, transaction_two)

    def test_not_equal(self):
        transaction_one = Transaction(1, 2, 3, 12, "11/11/1111", 12.12)
        transaction_two = Transaction(1, 2, 3, 12, "12/11/1111", 12.12)
        self.assertNotEqual(transaction_one, transaction_two)

    def test_getter(self):
        transaction_one = Transaction(1, 2, 3, 12, "11/11/1111", 12.12)
        self.assertEqual(transaction_one.get_transaction_id(), 1)
        self.assertEqual(transaction_one.get_medicine_transacted_id(), 2)
        self.assertEqual(transaction_one.get_customer_card_transaction_id(), 3)
        self.assertEqual(transaction_one.get_pieces_number(), 12)
        self.assertEqual(transaction_one.get_date(), '11/11/1111')
        self.assertEqual(transaction_one.get_time(), 12.12)

    def test_setter(self):
        transaction_one = Transaction(1, 2, 3, 12, "11/11/1111", 12.12)
        transaction_one.set_pieces_number(13)
        transaction_one.set_date('12/11/1111')
        transaction_one.set_time(12.11)
        transaction_two = Transaction(1, 2, 3, 13, "12/11/1111", 12.11)
        self.assertEqual(transaction_one, transaction_two)
