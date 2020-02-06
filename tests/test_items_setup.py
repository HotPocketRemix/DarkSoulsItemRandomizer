import items_setup
import unittest

class boss_weapon_list_helper_unit_tests(unittest.TestCase):
    def setUp(self):
        self.boss_weapon_list_instance = items_setup.boss_weapon_list_helper
    def tearDown(self):
        return super().tearDown()

class list_of_five(boss_weapon_list_helper_unit_tests):
    def runTest(self):
        assert self.boss_weapon_list_instance(0, 400) == \
            [(0, 0), (0, 100), (0, 200), (0, 300), (0, 400)], \
                "The lists are not equivalent"

class list_of_one(boss_weapon_list_helper_unit_tests):
    def runTest(self):
        assert self.boss_weapon_list_instance(0, 0) == [(0, 0)], \
            "The lists are not equivalent"

class list_of_zero(boss_weapon_list_helper_unit_tests):
    def runTest(self):
        assert self.boss_weapon_list_instance(0, -1) == [], \
            "The lists are not equivalent"

class inverted_indices(boss_weapon_list_helper_unit_tests):
    def runTest(self):
        assert self.boss_weapon_list_instance(400, 0) == [], \
            "The lists are not equivalent"

if __name__ == "__main__":
    unittest.main()
