import randomize_item_table
import unittest

class find_key_item_by_name_error_test(unittest.TestCase):
    def runTest(self):
        self.assertRaises(ValueError,randomize_item_table.find_key_item_by_name("lordvessel", {}))

if __name__ == "__main__":
    unittest.main()