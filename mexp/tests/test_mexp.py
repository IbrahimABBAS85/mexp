import unittest

from structure.car_class import Car
from mexp import *

class Test_test_mexp(unittest.TestCase):

    def test_find_str(self):
        listTesti = []
        listTesti.append(Car('Jack', 'benlalla', True, 1))
        listTesti.append(Car('Jack2', 'elarrs', False, 5))
        listTesti.append(Car('Marc', 'roro', False, 2))
        result = find(listTesti, lname = 'roro')
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, 'Marc')

    def test_find_str_no_result(self):
        listTesti = []
        listTesti.append(Car('Jack', 'benlalla', True, 1))
        listTesti.append(Car('Jack2', 'elarrs', False, 5))
        listTesti.append(Car('Marc', 'roro', False, 2))
        result = find(listTesti, lname = 'toto')
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 0)        

    def test_find_bool(self):
        listTesti = []
        listTesti.append(Car('Jack', 'benlalla', True, 1))
        listTesti.append(Car('Jack2', 'elarrs', False, 5))
        listTesti.append(Car('Marc', 'roro', False, 2))
        result = find(listTesti, active = True)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].lname, 'benlalla')

        result = find(listTesti, active = False)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)

    def test_find_int(self):
        listTesti = []
        listTesti.append(Car('Jack', 'benlalla', True, 1))
        listTesti.append(Car('Jack2', 'elarrs', False, 1))
        listTesti.append(Car('Marc', 'roro', False, 2))
        result = find(listTesti, rank = 2)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].lname, 'roro')

        result = find(listTesti, rank = 1)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)

    def test_find_one_argument_many_results(self):
        listTesti = []
        listTesti.append(Car('Jack', 'benlalla', True, 1))
        listTesti.append(Car('Jack', 'elarrs', False, 5))
        listTesti.append(Car('Marc', 'roro', False, 2))
        result = find(listTesti, name = 'Jack')
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)

    def test_find_two_arguments_one_result(self):
        listTesti = []
        listTesti.append(Car('Jack', 'benlalla', True, 1))
        listTesti.append(Car('Jack', 'elarrs', False, 5))
        listTesti.append(Car('Marc', 'roro', False, 2))
        result = find(listTesti, name = 'Jack', lname='elarrs')
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].lname, 'elarrs')

    def test_find_four_arguments(self):
        listTesti = []
        listTesti.append(Car('Jack', 'benlalla', True, 1))
        listTesti.append(Car('Jack', 'elarrs', False, 5))
        listTesti.append(Car('Marc', 'roro', False, 2))
        result = find(listTesti, name = 'Jack', lname='elarrs', active = False, rank = 5)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].lname, 'elarrs')
        result = find(listTesti, name = 'Jack', lname='elarrs', active = False, rank = 1)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 0)

    def test_find_any_str(self):
        listTesti = []
        listTesti.append(Car('Jack', 'benlalla', True, 1))
        listTesti.append(Car('Jack2', 'elarrs', False, 5))
        listTesti.append(Car('Marc', 'roro', False, 2))
        result = find_any(listTesti, name = 'Jack')
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)

    def test_find_any_two_str(self):
        listTesti = []
        listTesti.append(Car('Jack', 'benlalla', True, 1))
        listTesti.append(Car('Jack2', 'elarrs', False, 5))
        listTesti.append(Car('Marc', 'roro', False, 2))
        result = find_any(listTesti, name = 'Jack', lname = 'elarrs')
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)
        result = find_any(listTesti, name = 'Jack', lname = 'x')
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)

    def test_find_any_str_no_results(self):
        listTesti = []
        listTesti.append(Car('Jack', 'benlalla', True, 1))
        listTesti.append(Car('Jack2', 'elarrs', False, 5))
        listTesti.append(Car('Marc', 'roro', False, 2))
        result = find_any(listTesti, name = 'toto')
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 0)

def suite():
    suite = unittest.TestSuite()    
    suite.addTest(Test_test_mexp('test_find_str'))
    suite.addTest(Test_test_mexp('test_find_str_no_result'))
    suite.addTest(Test_test_mexp('test_find_bool'))
    suite.addTest(Test_test_mexp('test_find_int'))
    suite.addTest(Test_test_mexp('test_find_one_argument_many_results'))
    suite.addTest(Test_test_mexp('test_find_two_arguments_one_result'))
    suite.addTest(Test_test_mexp('test_find_four_arguments'))
    suite.addTest(Test_test_mexp('test_find_any_str'))
    suite.addTest(Test_test_mexp('test_find_any_two_str'))
    suite.addTest(Test_test_mexp('test_find_any_str_no_results'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())