
words=[('pedro',22),('juan',23),('pepe',24)]

def byName(key):
    return key[0]

def byAge(value):
    return value[1]

def turtle():
	print 'turtle'
	pass

def calc():
	print 'calc'
	pass

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
			turtle()
		elif ch == 3:
			calc()
		else:
			exit()


if __name__ == '__main__':
  main()