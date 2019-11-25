import unittest

from lab7.domain.Item import Item
from lab7.domain.ItemValidator import ItemValidator
from lab7.repository.ItemRepository import ItemRepository
from lab7.service.ItemRemover import ItemRemover


class ItemRemoverTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = ItemRepository()
        self.remover = ItemRemover(self.repository, ItemValidator(self.repository))
        item = Item(1, "chair", "made of wood", 23, "room")
        self.repository.add(item)
        item_one = Item(2, "chair", "made of wood", 23, "room")
        self.repository.add(item_one)

    def test_remove(self):
        self.remover.remove(1)
        self.assertEqual(self.repository.find_by_id(1), None)


