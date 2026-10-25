import unittest

from fraction import Fraction

class TestSub(unittest.TestCase):
  def test_sub_reduces(self):
    result = Fraction(3,4) - Fraction(1,4)
    self.assertEqual("1/2",str(result))

  def test_sub_mixed(self):
    result = Fraction(11,12) - Fraction(1,4)
    self.assertEqual("2/3",str(result))

  def test_sub_mixed_reduces(self):
    result = Fraction(4,9) - Fraction(2,5)
    self.assertEqual("2/45",str(result))

  def test_sub_to_int(self):
    result = Fraction(4,3) - Fraction(1,3)
    self.assertEqual("1",str(result))

  def test_sub_int(self):
    result = Fraction(4,3) - 1
    self.assertEqual("1/3",str(result))

  def test_sub_neg(self):
    result = Fraction(1,3) - Fraction(-1,3)
    self.assertEqual("2/3",str(result))

  def test_sub_to_zero(self):
    result = Fraction(2,3) - Fraction(2,3)
    self.assertEqual("0",str(result))

  def test_sub_invalid_type(self):
    with self.assertRaises(TypeError):
            Fraction(1, 2) - "invalid"


if __name__ == "__main__":
  unittest.main()
