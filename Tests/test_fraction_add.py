import unittest

from fraction import Fraction

class TestAdd(unittest.TestCase):
  def test_add_reduces(self):
    result = Fraction(1,4) + Fraction(1,4)
    self.assertEqual("1/2",str(result))

  def test_add_mixed(self):
    result = Fraction(2,3) + Fraction(1,4)
    self.assertEqual("11/12",str(result))

  def test_add_mixed_reduces(self):
    result = Fraction(2,45) + Fraction(2,5)
    self.assertEqual("4/9",str(result))

  def test_add_to_int(self):
    result = Fraction(2,3) + Fraction(1,3)
    self.assertEqual("1",str(result))

  def test_add_int(self):
    result = Fraction(2,3) + 1
    self.assertEqual("5/3",str(result))

  def test_add_neg(self):
    result = Fraction(2,3) + Fraction(-1,3)
    self.assertEqual("1/3",str(result))

  def test_add_to_zero(self):
    result = Fraction(2,3) + Fraction(-2,3)
    self.assertEqual("0",str(result))

  def test_add_invalid_type(self):
    with self.assertRaises(TypeError):
            Fraction(1, 2) + "invalid"


if __name__ == "__main__":
  unittest.main()
