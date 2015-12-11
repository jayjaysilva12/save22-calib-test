import calculator
import unittest

class TestCalculator(unittest.TestCase):
  
    def test_Add(self):
      self.assertEqual(
            calculator.add(1,1),
            2)
            

if __name__=='__main__':
  unittest.main()