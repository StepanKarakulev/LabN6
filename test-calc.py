import unittest
from main import sum
from main import divide
from main import substract
from main import multiply

class TestCalc(unittest.TestCase):

    def test_Sum(self):
        self.assertEqual(sum(3,5), 8)
        self.assertEqual(sum(3, 0), 3)
        self.assertEqual(sum(-4, 1), -3)
        self.assertEqual(sum(10, 15), 25)

    def test_Devide(self):
        self.assertEqual(divide(10,2), 5)
        self.assertEqual(divide(0, 2), 0)
        self.assertEqual(divide(-4, 1), -4)
        self.assertEqual(divide(5, 2), 2.5)

    def test_Multiply(self):
        self.assertEqual(multiply(3,5), 15)
        self.equal = self.assertEqual(multiply(3, 0), 0)
        self.assertEqual(multiply(-4, 1), -4)
        self.assertEqual(multiply(10, 15), 150)

    def test_substract(self):
        self.assertEqual(substract(3,5), -2)
        self.assertEqual(substract(3, 0), 3)
        self.assertEqual(substract(-4, 1), -5)
        self.assertEqual(substract(10, 15), -5)