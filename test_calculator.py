import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add2(self):
        self.assertEqual(self.calc.add(-1, 2), 1)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 1), 4)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 1), 5)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(-5, -1), 5)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 1), 2)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(-5, 1), -5)
    def test_divide3(self):
        self.assertEqual(self.calc.divide(4, -2), -2)
    def test_divide4(self):
        self.assertEqual(self.calc.divide(-5, -1), 5)
    def test_divide5(self):
        self.assertEqual(self.calc.divide(5, 0), "undefined")
    def test_divide6(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(-3, 2), -1)
    def test_modulo3(self):
        self.assertEqual(self.calc.modulo(-5, 3), -2) 
    def test_modulo4(self):
        self.assertEqual(self.calc.modulo(5, -2), 1)
    def test_modulo5(self):
        self.assertEqual(self.calc.modulo(0, 1), 0)
    def test_modulo6(self):
        self.assertEqual(self.calc.modulo(2,0),"undefined")
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()