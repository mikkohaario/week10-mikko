import unittest
from ..calculator import calculator as calculator

class TestCalculator(unittest.TestCase):
    def test_sum_numbers_returns_sum_of_integers(self):
        result = calculator.plus(2, 3)
        self.assertEqual(result, 5)

    def test_sum_numbers_works_with_negative_numbers(self):
        result = calculator.plus(-2, -3)
        self.assertEqual(result, -5)

    def test_sum_numbers_returns_sum_of_floats(self):
        result = calculator.plus(2.4, 3.2)
        self.assertAlmostEqual(result, 5.6)

    def test_sum_numbers_returns_sum_of_integer_and_float(self):
        result = calculator.plus(2, 3.2)
        self.assertEqual(result, 5.2)

    def test_sum_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.plus(1, "a")

    ############################

    def test_minus_numbers_returns_sum_of_integers(self):
        result = calculator.minus(2, 3)
        self.assertEqual(result, -1)

    def test_minus_numbers_works_with_negative_numbers(self):
        result = calculator.minus(-2, -3)
        self.assertEqual(result, 1)

    def test_minus_numbers_returns_sum_of_floats(self):
        result = calculator.minus(2.4, 3.2)
        self.assertAlmostEqual(result, -0.8)

    def test_minus_numbers_returns_sum_of_integer_and_float(self):
        result = calculator.minus(2, 3.2)
        self.assertAlmostEqual(result, -1.2)

    def test_minus_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.minus(1, "a")
    
    ############################

    def test_tulo_numbers_returns_sum_of_integers(self):
        result = calculator.tulo(2, 3)
        self.assertEqual(result, 6)

    def test_tulo_numbers_works_with_negative_numbers(self):
        result = calculator.tulo(-2, -3)
        self.assertEqual(result, 6)

    def test_tulo_numbers_returns_sum_of_floats(self):
        result = calculator.tulo(2.4, 3.2)
        self.assertAlmostEqual(result, 7.68)

    def test_tulo_numbers_returns_sum_of_integer_and_float(self):
        result = calculator.tulo(2, 3.2)
        self.assertAlmostEqual(result, 6.4)

    def test_tulo_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.minus(1, "a")

    #################

    def test_jako_numbers_returns_sum_of_integers(self):
        result = calculator.jako(2, 3)
        self.assertGreaterEqual(result, 0.66)

    def test_jako_numbers_works_with_negative_numbers(self):
        result = calculator.jako(-2, -3)
        self.assertGreaterEqual(result, 0.6666666666666666)

    def test_jako_numbers_returns_sum_of_floats(self):
        result = calculator.jako(2.4, 3.2)
        self.assertAlmostEqual(result, 0.75)

    def test_jako_numbers_returns_sum_of_integer_and_float(self):
        result = calculator.jako(2, 3.2)
        self.assertGreaterEqual(result, 0.625)

    def test_jako_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.jako(1, "a")
if __name__ == '__main__':
    unittest.main()
    