import unittest

from lab8.domain.CustomerCard import CustomerCard


class CustomerCardTest(unittest.TestCase):
    def test_equal(self):
        card_one = CustomerCard(1, 'Adam', 'Andrei', 5010306015562, '06/03/2001', '01/10/2019')
        card_two = CustomerCard(1, 'Adam', 'Andrei', 5010306015562, '06/03/2001', '01/10/2019')
        self.assertEqual(card_one, card_two)

    def test_not_equal(self):
        card_one = CustomerCard(1, 'Adam', 'Andrei', 5010306015562, '06/03/2001', '01/10/2019')
        card_two = CustomerCard(1, 'Adam', 'Andrei', 5010306015561, '06/03/2001', '01/10/2019')
        self.assertNotEqual(card_one, card_two)

    def test_getter(self):
        card_one = CustomerCard(1, 'Adam', 'Andrei', 5010306015562, '06/03/2001', '01/10/2019')
        self.assertEqual(card_one.get_customer_card_id(), 1)
        self.assertEqual(card_one.get_customer_name(), 'Adam')
        self.assertEqual(card_one.get_customer_first_name(), 'Andrei')
        self.assertEqual(card_one.get_customer_cnp(), 5010306015562)
        self.assertEqual(card_one.get_birth_date(), '06/03/2001')
        self.assertEqual(card_one.get_registration_date(), '01/10/2019')

    def test_setter(self):
        card_one = CustomerCard(1, 'Adam', 'Andrei', 5010306015562, '06/03/2001', '01/10/2019')
        card_one.set_customer_name('Toma')
        card_one.set_customer_first_name('Newton')
        card_one.set_birth_date('25/12/1665')
        card_one.set_registration_date('26/03/2000')
        card_two = CustomerCard(1, 'Toma', 'Newton', 5010306015562, '25/12/1665', '26/03/2000')
        self.assertEqual(card_one, card_two)

    def test_get_text_format(self):
        card_one = CustomerCard(1, 'Adam', 'Andrei', 5010306015562, '06/03/2001', '01/10/2019')
        card_string = card_one.get_text_format()
        self.assertEqual(card_string, "1,Adam,Andrei,5010306015562,06/03/2001,01/10/2019")
