import unittest

from lab7.test.domain.ItemTest import ItemTest
from lab7.test.domain.ItemValidatorTest import ItemValidatorTest
from lab7.test.repository.ItemRepositoryTest import ItemRepositoryTest


def run_tests():
    loader = unittest.defaultTestLoader
    all_suites = \
    [
        loader.loadTestsFromTestCase(ItemTest),
        loader.loadTestsFromTestCase(ItemValidatorTest),
        loader.loadTestsFromTestCase(ItemRepositoryTest)
    ]
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(unittest.TestSuite(all_suites))


if __name__ == '__main__':
    run_tests()
