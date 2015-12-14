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

    def test_success(self):
		num1=calculator.input1(self.mock_input1)
		oper=calculator.op(self.mock_op)
		num2=calculator.input2(self.mock_input2)
		ans=calculator.operator(num1,oper,num2)
		final=calculator.output(num1,oper,num2,ans)
		self.assertEqual(final,'1 + 3 = 4')

    def test_input1(self):
    	self.assertEqual(calculator.input1(self.mock_input1),1)

    def mock_input1(self,prompt):
    	return 1

    def test_op(self):
    	self.assertEqual(calculator.operator(1,self.mock_op(''),3),4)

    def mock_op(self,prompt):
    	return '+'

    def test_input2(self):
    	self.assertEqual(calculator.input2(self.mock_input2),3)

    def mock_input2(self,prompt):
    	return 3

    def test_DivideByZero(self):
        self.assertEqual(calculator.input1(self.mock_num1),1)
        self.assertEqual(calculator.op(self.mock_div),'/')
        self.assertEqual(calculator.input2(self.mock_num2),0)

    def mock_num1(self,prompt):
        return 1
    def mock_div(self,prompt):
        return '/'
    def mock_num2(self,prompt):
        return 0

    def test_StringInputs(self):
        self.assertEqual(calculator.input1(self.mock_strNum1),'A')
        self.assertEqual(calculator.op(self.mock_add),'+')
        self.assertEqual(calculator.input2(self.mock_strNum2),'C')

    def mock_strNum1(self,prompt):
        return 'A'
    def mock_add(self,prompt):
        return '+'
    def mock_strNum2(self,prompt):
        return 'C'

    def testIntAndString(self):
        self.assertEqual(calculator.input1(self.mock_intStrNum1),1)
        self.assertEqual(calculator.op(self.mock_intStrAdd),'+')
        self.assertEqual(calculator.input2(self.mock_intStrNum2),'A')

    def mock_intStrNum1(self,prompt):
        return 1
    def mock_intStrAdd(self,prompt):
        return '+'
    def mock_intStrNum2(self,prompt):
        return 'A'


if __name__=='__main__':
	unittest.main()