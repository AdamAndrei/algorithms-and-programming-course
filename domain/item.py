def test_Item():
    item_one = Item(1, "chair", "made of wood", 23, "room")
    item_two = Item(2, "table", "made of steel", 34, "bath")
    assert item_one.ID == 1
    assert item_one.name == "chair"
    assert item_one.description == "made of wood"
    assert item_one.price == 23
    assert item_one.location == "room"



class Item():
    def __init__(self, ID, name, description, price, location):
        self.ID = ID
        self.name = name
        self.description = description
        self.price = price
        self.location = location

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.ID == other.ID and self.name == other.name and self.description == other.description and self.price == other.price and self.location == other.location

    def __ne__(self, other):
        return not(self == other)

