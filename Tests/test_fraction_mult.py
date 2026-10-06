import unittest

from fraction import Fraction


class TestFractionMult(unittest.TestCase):

    def test_mult_basic(self):
        result = Fraction(1,3) * Fraction(1,5)
        self.assertEquals("1/15",str(result))
    
    def test_mul_fraction_by_fraction_reduces_result(self):
        result = Fraction(2, 3) * Fraction(3, 4)
        self.assertEqual("1/2", str(result))

    def test_mul_fraction_by_integer(self):
        result = Fraction(3, 5) * 10
        self.assertEqual("6", str(result))

    def test_mul_with_zero(self):
        result = Fraction(0, 7) * Fraction(5, 9)
        self.assertEqual("0", str(result))

    def test_mul_with_neg(self):
        result = Fraction(1,3) * Fraction(-1,3)
        self.assertEquals("-1/9",str(result))

    def test_mul_raises_type_error_for_invalid_type(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) * "invalid"


if __name__ == "__main__":
    unittest.main()
