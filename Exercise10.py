import turtle
t=turtle
words=[('pedro',22),('juan',23),('pepe',24)]

def byName(key):
    return key[0]

def byAge(value):
    return value[1]

def turtle(val):
	t.pensize(3)
	t.color('red')
	for i in range(0,val):
		t.left(135)
		t.forward(150)
		t.right(90)
		t.forward(45)
		t.right(90)
		t.forward(150)
		t.left(90)
		t.forward(150)
		t.right(90)
		t.forward(45)
		t.right(90)
		t.forward(150)
		t.left(90)
		t.forward(150)
		t.right(90)
		t.forward(45)
		t.right(90)
		t.forward(150)
		t.left(90)
		t.forward(150)
		t.right(90)
		t.forward(45)
		t.right(90)
		t.forward(150)

	t.exitonclick()
	exit()

def add(fnum,snum):
	return fnum + snum

def sub(fnum,snum):
	return fnum - snum

def mult(fnum,snum):
	return fnum * snum

def div(fnum,snum):
	return fnum / snum

def enterNum():
	firstNumber = input('Enter Number: ')
	secondNumber = input('Enter Number: ')
	return (firstNumber,secondNumber)

def calc():
	(firstNumber,secondNumber)=enterNum()
	op = raw_input('Enter operand: ')
	if op == '+':
		toPrint=add(firstNumber,secondNumber)
	elif op == '-':
		toPrint=sub(firstNumber,secondNumber)
	elif op == '*':
		toPrint=mult(firstNumber,secondNumber)
	elif op == '/':
		toPrint=div(firstNumber,secondNumber)
	print 'The answer is: ', toPrint

def main():
	while 1:
		print
		print '[1]Sorting'
		print '[2]Turtle'
		print '[3]Calculator'
		print '[ELSE EXIT]'
		ch = input('Enter Choice: ')
		if ch == 1:
			while 1:
				print 
				print '[1]lambda by name'
				print '[2]lambda by age'
				print '[3]function by name'
				print '[4]function by age'
				print '[5]back'
				print '[ELSE EXIT]'
				choice = input('Enter Choice: ')
				if choice == 1:
					print 
					toPrint=sorted(words, key=lambda x:x[0])
				elif choice == 2:
					print 
					toPrint=sorted(words, key=lambda x:x[1])
				elif choice == 3:
					print
					toPrint=sorted(words, key = byName,reverse = True)
				elif choice == 4:
					print
					toPrint=sorted(words, key = byAge,reverse = True)
				elif choice == 5:
					main()
				else:
					exit()
				print toPrint
		elif ch == 2:
			print 
			print '[1]Letter X'
			print '[2]Windmill'
			print '[3]Back'
			print '[ELSE EXIT]'
			cho = input('Enter Choice: ')
			if cho == 1:
				turtle(1)
			elif cho == 2:
				turtle(8)
			elif cho == 3:
				main()
			else:
				exit()
		elif ch == 3:
			calc()
		else:
			exit()


if __name__ == '__main__':
  main()