import unittest

from lab7.domain.Item import Item
from lab7.exeption.DublicatedIdException import DuplicatedIdException
from lab7.repository.ItemRepository import ItemRepository


class ItemRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = ItemRepository()

    def test_add_raises_duplicated_id_exception(self):
        item = Item(1, "chair", "made of wood", 23, "room")
        self.repository.add(item)
        self.assertTrue(self.repository.exists(1))
        item_one = Item(1, "table", "made of steel", 34, "roof")
        self.repository.add(item_one)
        self.assertEqual(item, self.repository.find_by_id(1))

    def test_find_by_id_returns_None(self):
        self.assertIsNone(self.repository.find_by_id(1))
