import key_items_setup
import unittest

class key_placed_unit_tests(unittest.TestCase):
    def setUp(self):
        self.key_placed_instance = key_items_setup.key_placed
    def tearDown(self):
        return super().tearDown()

class empty_list(key_placed_unit_tests):
    def runTest(self):
        self.assertFalse(self.key_placed_instance("lordvessel",{}))

class list_of_one(key_placed_unit_tests):
    def runTest(self):
        self.assertFalse(self.key_placed_instance("lordvessel",{"blighttown_key" : "blighttown"}))

class list_of_five(key_placed_unit_tests):
    def runTest(self):
        self.assertFalse(self.k)

if __name__ == "__main__":
    unittest.main()