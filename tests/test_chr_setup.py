import chr_setup
import unittest
import random

class can_be_used_unit_tests(unittest.TestCase):
    def setUp(self):
        self.can_be_used_instance = chr_setup.can_be_used
    def tearDown(self):
        return super().tearDown()
class cannot_be_used():
    def runTest(self):
        seed = bool(random.getrandbits(1))
        assert self.can_be_used_instance(0,0,0,0,seed,seed,seed) == False, \
            "a character with stats of 0 across the board should not be able to wield anything"


if __name__ == "__main__":
    unittest.main()