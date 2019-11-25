from lab7.domain.Item import Item
from lab7.exeption.DublicatedIdException import DuplicatedIdException


class ItemRepository:
    def __init__(self):
        self.__items = {}

    def add(self, item: Item):
        if not self.exists(item.get_id()):
            self.__items[item.get_id()] = item

    def exists(self, item_id: int):
        return item_id in self.__items

    def find_by_id(self, item_id) -> Item:
        if self.exists(item_id):
            return self.__items[item_id]






