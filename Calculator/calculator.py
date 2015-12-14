def add(fnum,snum):
  	return fnum + snum

def sub(fnum,snum):
	return fnum - snum

def mult(fnum,snum):
	return fnum * snum

def div(fnum,snum):
	return fnum / snum

def input1(input = raw_input):
	return input ('Enter number: ')

def op(input = raw_input):
	try:
  		operator=input ('Enter operator: ')
  		return operator.strip()
  	except TypeError:
  		ctr=1
  		
  		op()
  		
  
def input2(input = raw_input):
	return input ('Enter number: ')




def operator(num1,op,num2):
	# if op == '+':
	# 	return add(num1,num2)
	# elif op == '-':
	# 	return sub(num1,num2)
	# elif op == '*':
	# 	return mult(num1,num2)
	# elif op == '/':
	# 	return div(num1,num2)
	# else:
	# 	return None
	functions={'+':add,'-':sub,'*':mult,'/':div}

	func=functions.get(op,None)
	if func:
		return func(num1,num2)
	return None
   
def output(num1,op,num2,ans):
  	return '{} {} {} = {}'.format(num1,op,num2,ans)

def main():
	doneNum1=False
	doneOp=False
	doneNum2=False
	ans=0
	while not doneNum1:
		try:
			num1=int(input1())
			doneNum1=True
		except ValueError:
			print 'Must input a number.'

	while not doneOp:
		try:
			oper=op()
			doneOp=True
		except TypeError:
			print 'Enter a valid operator.'

	while not doneNum2:
		try:
			num2=int(input2())
			doneNum2=True
		except ValueError:
			print 'Must input a number.'

	try:
		ans=operator(num1,oper,num2)
		print output(num1,oper,num2,ans)
	except ZeroDivisionError:
		print 'You cannot divide zero'

	
	  
if __name__ == '__main__':
  	main()