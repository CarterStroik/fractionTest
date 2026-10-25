from fraction import Fraction
import unittest

class test_fraction_str(unittest.TestCase):
  def test_displayfraction(self):
    a = Fraction(1,2)
    self.assertEqual(" 1/2 ",a.__str__())
  def test_displayInt(self):
    a = Fraction(5,1)
    self.assertEqual("5",a.__str__())
  def test_displayNeg(self):
    a = Fraction(-1,2)
    b = Fraction(1,-2)
    self.assertEqual("-1/2",a.__str__())
    self.assertEqual("-1/2",a.__str__())
    
