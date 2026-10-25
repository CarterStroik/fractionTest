from fraction import Fraction
import unittest

class test_fraction_float(unittest.TestCase):
  def test_display_float(self):
    a = Fraction(1,2)
    self.assertEqual("0.5",a.__float__().__str__())
  def test_displayInt(self):
    a = Fraction(5,1)
    self.assertEqual("5.0",a.__float__().__str__())
  def test_displayNeg(self):
    a = Fraction(-1,2)
    b = Fraction(1,-2)
    self.assertEqual("-0.5",a.__float__().__str__())
    self.assertEqual("-0.5",a.__float__().__str__())
