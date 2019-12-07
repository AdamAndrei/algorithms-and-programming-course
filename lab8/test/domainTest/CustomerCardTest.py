import unittest

from domain.CustomerCard import CustomerCard


class CustomerCardTest(unittest.TestCase):
    def test_equal(self):
        card_one = CustomerCard(1, 'Adam', 'Andrei', 5010306015562, '06/03/2001', '01/10/2019', False)
        card_two = CustomerCard(1, 'Adam', 'Andrei', 5010306015562, '06/03/2001', '01/10/2019', False)
        self.assertEqual(card_one, card_two)

    def test_not_equal(self):
        card_one = CustomerCard(1, 'Adam', 'Andrei', 5010306015562, '06/03/2001', '01/10/2019', False)
        card_two = CustomerCard(1, 'Adam', 'Andrei', 5010306015561, '06/03/2001', '01/10/2019', False)
        self.assertNotEqual(card_one, card_two)

    def test_getter(self):
        card_one = CustomerCard(1, 'Adam', 'Andrei', 5010306015562, '06/03/2001', '01/10/2019', False)
        self.assertEqual(card_one.get_id_entity(), 1)
        self.assertEqual(card_one.get_customer_name(), 'Adam')
        self.assertEqual(card_one.get_customer_first_name(), 'Andrei')
        self.assertEqual(card_one.get_customer_cnp(), 5010306015562)
        self.assertEqual(card_one.get_birth_date(), '06/03/2001')
        self.assertEqual(card_one.get_registration_date(), '01/10/2019')

    def test_get_text_format(self):
        card_one = CustomerCard(1, 'Adam', 'Andrei', 5010306015562, '06/03/2001', '01/10/2019', False)
        card_string = card_one.get_text_format()
        self.assertEqual(card_string, "1,Adam,Andrei,5010306015562,06/03/2001,01/10/2019")
