import unittest

class TestAdd(unittest.TestCase):
  def test_add_reduces(self):
    result = Fraction(1,4) + Fraction(1,4)
    assertEquals("1/2",result)

  def test_add_mixed(self):
    result = Fraction(2,3) + Fraction(1,4)
    assertEquals("11/12",result)

  def test_add_mixed_reduces(self):
    result = Fraction(2,45) + Fraction(2,5)
    assertEquals("4/9",result)

  def test_add_to_int(self):
    result = Fraction(2,3) + Fraction(1,3)
    assertEquals("1",result)

  def test_add_int(self):
    result = Fraction(2,3) + 1
    assertEquals("5/3",result)

  def test_add_neg(self):
    result = Fraction(2,3) + Fraction(-1,3)
    assertEquals("1/3",result)

  def test_add_to_zero(self):
    result = Fraction(2,3) + Fraction(-2,3)
    assertEquals("0",result)

  def test_add_invalid_type(self):
    with self.assertRaises(TypeError):
            Fraction(1, 2) + "invalid"


if __name__ == "__main__":
  unittest.main()
