def add(fnum,snum):
	return fnum + snum

def sub(fnum,snum):
	return fnum - snum

def mult(fnum,snum):
	return fnum * snum

def div(fnum,snum):
	return fnum / snum

def input1():
  return int(raw_input('Enter number: '))

def op():
  return raw_input('Enter operator: ')
  
def input2():
  return int(raw_input('Enter number: '))

def operator(num1,op,num2):
	if op == '+':
		return add(num1,num2)
	elif op == '-':
		return sub(num1,num2)
	elif op == '*':
		return mult(num1,num2)
	elif op == '/':
		return div(num1,num2)
	else:
		return None
   
def output(num1,op,num2,ans):
  return '{} {} {} = {}'.format(num1,op,num2,ans)

def main():
  num1=input1()
  oper=op()
  num2=input2()
  ans=operator(num1,oper,num2)
  print output(num1,oper,num2,ans)
  
main()