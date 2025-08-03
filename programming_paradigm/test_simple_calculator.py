import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.Testcase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-10, -1), -11)
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), 0)
        self.assertEqual(self.calc.subtract(-10, -1), 9)

    def test_multiplication(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-10, -1), 10)

    def test_division(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.divide(2, 4), 0.5)
        self.assertEqual(self.calc.divide(0, 100), 0)
        self.assertEqual(self.calc.divide(-10, -1), 10)
 