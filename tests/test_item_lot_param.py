import item_lot_param
import unittest

class init_test(unittest.TestCase):
    def runTest(self):
        self.assertRaises(ValueError, item_lot_param(9,9,9,9,9,9,9))

if __name__ == "__main__":
    unittest.main()