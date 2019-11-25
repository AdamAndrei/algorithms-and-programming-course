import unittest

from lab7.domain.Item import Item


class ItemTest(unittest.TestCase):
    def test_items_with_same_data_different_id_not_equal(self):
        item_one = Item(1, "chair", "made of wood", 23, "room")
        item_two = Item(2, "chair", "made of wood", 23, "room")
        self.assertNotEqual(item_one, item_two)

    def test_equal(self):
        item_one = Item(1, "chair", "made of wood", 23, "room")
        item_two = Item(1, "chair", "made of wood", 23, "room")
        self.assertEqual(item_one, item_two)
