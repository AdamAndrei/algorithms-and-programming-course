import unittest

from lab8.test.domainTest.CustomerCardTest import CustomerCardTest
from lab8.test.domainTest.MedcineTest import MedicineTest
from lab8.test.domainTest.TransactionTest import TransactionTest
from lab8.test.repositoryTest.MedicineRepositoryTest import MedicineRepositoryTest


def run_tests():
    loader = unittest.defaultTestLoader
    all_suites = \
        [
            loader.loadTestsFromTestCase(MedicineTest),
            loader.loadTestsFromTestCase(CustomerCardTest),
            loader.loadTestsFromTestCase(TransactionTest),
            loader.loadTestsFromTestCase(MedicineRepositoryTest)
        ]
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(unittest.TestSuite(all_suites))


if __name__ == '__main__':
    run_tests()
