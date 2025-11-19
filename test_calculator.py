#https://github.com/FluxFish3/lab11-TR-MG
#Partner 1: Michael Galiani
#Partner 2: Tomas Ramirez

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(-5, 20), 15)# 3 assertions
        self.assertEqual(add(4, 1),5)

    def test_subtract(self):
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(4, 1), 3)
        self.assertEqual(subtract(-5, -10), 5)
# 3 assertions


    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-5, 6), -30)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 0), 0)
        self.assertEqual(div(-1, -5), 5)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0,5)
        # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self):# 3 assertions
        self.assertEqual(logarithm(10,100),2)
        self.assertEqual(logarithm(3,27),3)
        self.assertEqual(logarithm(2,16),4)

    def test_log_invalid_base(self):# 1 assertion
        with self.assertRaises(ValueError):
            log(0,100)
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(1, 1), math.sqrt(2))
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 5), math.sqrt(50))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(100), 10)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()