import unittest
import random_guessing_game_test as main

class TestMain(unittest.TestCase):
    def test_stuff1(self):
        answer = 5
        test_param = 5
        result = main.input_guess(test_param, answer)
        self.assertTrue(result)

    def test_stuff2(self):
        answer = 5
        test_param = 0
        result = main.input_guess(test_param, answer)
        self.assertFalse(result)

    def test_stuff3(self):
        answer = 5
        test_param = 'ajfajnfk'
        result = main.input_guess(test_param, answer)
        self.assertFalse(result)


unittest.main()