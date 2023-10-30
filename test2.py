#unittest is used to test our code
#very important toavoid all types of errors and handle them
import unittest
import main 

class TestMain(unittest.TestCase):
    def setUp(self):        #runs before every test function 
        print("About to test a function")

    def test_do_stuff(self):
        """This is a test"""            #you can also use docstrings
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'savfhab'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertTrue(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertTrue(result, 'please enter number')

    def test_do_stuff5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertTrue(result, 'please enter number other than 0')

    def tearDown(self):     #also runs after every test
        print("cleaning up some code")

if __name__ == '__main__':
    unittest.main()
