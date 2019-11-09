from lab6.business.logic import *

EPSILON = 0.000001


def test_create_object_dictionary():
    import math
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert len(one_object) == 5
    assert get_ID_dictionary(one_object) == 1
    assert math.fabs(one_object["price"] - 23) < EPSILON
    assert get_name_dictionary(one_object) == "chair"


def test_get_ID_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_ID_dictionary(one_object) == 1


def test_get_name_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "masa")
    assert get_name_dictionary(one_object) == "chair"


def test_get_description_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_description_dictionary(one_object) == "made of wood"
    assert get_description_dictionary(one_object) != ""


def test_get_price_dictionary():
    object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_price_dictionary(object) == 23


def test_get_location():
    object_one = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_location_dictionary(object_one) == "table"


def test_set_ID_dictionary():
    object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_ID_dictionary(object) == 1
    set_ID_dictionary(object, 2)
    assert get_ID_dictionary(object) == 2


def test_set_name_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "masa")
    assert get_name_dictionary(one_object) == "chair"
    set_name_dictionary(one_object, "table")
    assert get_name_dictionary(one_object) == "table"


def test_set_description_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_description_dictionary(one_object) == "made of wood"
    set_description_dictionary(one_object, "made of steel")
    assert get_description_dictionary(one_object) == "made of steel"


def test_set_price_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_price_dictionary(one_object) == 23
    set_price_dictionary(one_object, 12)
    assert get_price_dictionary(one_object) == 12


def test_set_location_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    assert get_location_dictionary(one_object) == "table"
    set_location_dictionary(one_object, "roof")
    assert get_location_dictionary(one_object) == "roof"


def test_add_object_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    list_of_objects = []
    add_object_dictionary(list_of_objects, one_object)
    assert len(list_of_objects) == 1
    assert get_ID_dictionary(list_of_objects[0]) == 1
    assert get_location_dictionary(list_of_objects[0]) == "table"


def test_remove_object_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    list = [one_object]
    remove_object_dictionary(list, get_ID_dictionary(one_object))
    assert len(list) == 0


def test_update_object_dictionary():
    one_object = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    list = [one_object]
    update_object_dictionary(1, list, "table", "made of glass", 34, "room")
    assert get_description_dictionary(list[0]) == "made of glass"
    assert get_price_dictionary(list[0]) == 34


def test_move_object_dictionary():
    object_one = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    object_two = create_object_dictionary(2, "table", "made of steel", 42, "room")
    list = [object_one, object_two]
    move_object_dictionary(list, "table", "room")
    assert get_location_dictionary(list[0]) == "room"


def test_add_string_dictionary():
    object_one = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    object_two = create_object_dictionary(2, "table", "made of steel", 42, "room")
    list = [object_one, object_two]
    add_string_dictionary(list, " blue", 24)
    assert get_description_dictionary(list[1]) == "made of steel blue"


def test_max_per_location_dictionary():
    object_one = create_object_dictionary(1, "chair", "made of wood", 23, "table")
    object_two = create_object_dictionary(2, "table", "made of steel", 42, "room")
    object_three = create_object_dictionary(3, "table", "made of steel", 44, "room")
    list = [object_one, object_two, object_three]
    dictionary = max_per_location_dictionary(list)
    assert len(dictionary) == 2
    assert ((dictionary["room"]) == 44)


def assert_equals(expected, actual):
    if expected == actual:
        return
    raise AssertionError("Failed asserting that actual {0} equals expected {1}".format(actual, expected))


def test_sum_by_location_dictionary():
    obj = create_object_dictionary(1, "chair", "made of wood", 23, "room")
    obj_one = create_object_dictionary(2, "table", "made of steel", 7, "room")
    obj_two = create_object_dictionary(3, "mirror", "made of glass", 20, "bath")
    list_of_objects = [obj, obj_one, obj_two]
    assert_equals(30, sum_by_location_dictionary(list_of_objects)["room"])


def all_tests():
    test_get_location()
    test_get_description_dictionary()
    test_get_ID_dictionary()
    test_get_name_dictionary()
    test_get_price_dictionary()
    test_set_ID_dictionary()
    test_set_name_dictionary()
    test_set_description_dictionary()
    test_set_price_dictionary()
    test_set_location_dictionary()
    test_add_object_dictionary()
    test_remove_object_dictionary()
    test_update_object_dictionary()
    test_move_object_dictionary()
    test_add_string_dictionary()
    test_max_per_location_dictionary()
    test_sum_by_location_dictionary()


all_tests()

