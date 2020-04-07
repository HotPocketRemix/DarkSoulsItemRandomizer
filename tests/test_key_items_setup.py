import key_items_setup
import unittest
import randomizer_options as rng_opt

class key_placed_unit_tests(unittest.TestCase):
    def setUp(self):
        self.key_placed_instance = key_items_setup.key_placed
    def tearDown(self):
        return super().tearDown()

class empty_list(key_placed_unit_tests):
    def runTest(self):
        self.assertFalse(self.key_placed_instance("lordvessel",{}))

class list_of_one_false_first_branch(key_placed_unit_tests):
    def runTest(self):
        self.assertFalse(self.key_placed_instance("lordvessel",{"blighttown_key" : "blighttown"}))

class list_of_five_false_first_branch(key_placed_unit_tests):
    def runTest(self):
        self.assertFalse(self.key_placed_instance("lordvessel",{"blighttown_key":"blighttown","large_ember":"blighttown","mystery_key":"new_londo_ruins","large_ember":"firelink_shrine","orange_charred_ring":"lost_izalith"}))

class list_of_one_true(key_placed_unit_tests):
    def runTest(self):
        self.assertTrue(self.key_placed_instance("lordvessel",{"lordvessel" : "blighttown"}))

class list_of_five_true(key_placed_unit_tests):
    def runTest(self):
        self.assertTrue(self.key_placed_instance("lordvessel",{"blighttown_key":"blighttown","lordvessel":"blighttown","mystery_key":"new_londo_ruins","large_ember":"firelink_shrine","orange_charred_ring":"lost_izalith"}))

class list_of_one_to_place(key_placed_unit_tests):
    def runTest(self):
        self.assertFalse(self.key_placed_instance("lordvessel",{"lordvessel" : "to_place"}))

class list_of_five_to_place(key_placed_unit_tests):
    def runTest(self):
        self.assertFalse(self.key_placed_instance("lordvessel",{"blighttown_key":"blighttown","lordvessel":"to_place","mystery_key":"new_londo_ruins","large_ember":"firelink_shrine","orange_charred_ring":"lost_izalith"}))

class list_of_one_cannot_place(key_placed_unit_tests):
    def runTest(self):
        self.assertFalse(self.key_placed_instance("lordvessel",{"lordvessel" : "cannot_place"}))

class list_of_five_cannot_place(key_placed_unit_tests):
    def runTest(self):
        self.assertFalse(self.key_placed_instance("lordvessel",{"blighttown_key":"blighttown","lordvessel":"cannot_place","mystery_key":"new_londo_ruins","large_ember":"firelink_shrine","orange_charred_ring":"lost_izalith"}))

class get_key_restrictions_unit_tests(unittest.TestCase):
    def setup(self):
        self.get_key_restrictions_instance = key_items_setup.get_key_restrictions
    def tearDown(self):
        return super().tearDown()

class get_key_restrictions_error(get_key_restrictions_unit_tests):
    def runTest(self):
        self.assertRaises(KeyError, self.get_key_restrictions_instance("lordvessel",rng_opt() ))

if __name__ == "__main__":
    unittest.main()