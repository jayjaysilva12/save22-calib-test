import calculator
import unittest

class TestCalculator(unittest.TestCase):
  
    def test_add(self):
    	self.assertEqual(calculator.add(1,1),2)
    	with self.assertRaises(TypeError):
    		calculator.add('1',1)
    
    def test_sub(self):
    	self.assertEqual(calculator.sub(1,1),0)
    
    def test_mult(self):
    	self.assertEqual(calculator.mult(1,2),2)

    def test_div(self):
    	with self.assertRaises(ZeroDivisionError):
    		self.assertEqual(calculator.div(10,0))

    def test_None(self):
    	self.assertEqual(calculator.operator(13,'ab',11),None)

    def test_operator(self):
    	self.assertEqual(calculator.add(13,11),24)
    	self.assertEqual(calculator.sub(15,-10),25)
    	self.assertEqual(calculator.div(16,2),8)
    	self.assertEqual(calculator.mult(7,-3),-21)

    def test_output(self):
    	self.assertEqual(calculator.output(13,'+',11,24),'13 + 11 = 24')

    def test_op(self):
    	self.assertEqual(calculator.op(self.mock_input),1)

    def mock_input(self,prompt):
    	return 1

if __name__=='__main__':
	unittest.main()