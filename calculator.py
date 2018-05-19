def add(num1, num2):
	return num1+num2

def printf(format, *values):
    print(format % values )

def checkInput(num):
	while(True):
		try:
			num = int(input('Enter a number: '))
			break
		except ValueError:
			print('Valid number please')
	return num

def main():
	num = 0
	num1 = checkInput(num)
	num2 = checkInput(num)
	
	while(True):
		print('Enter a choice')
		choice = checkInput(num)
		if(choice == 1):
			print('Addition')
			print(add(num1,num2))
		else:
			print('Please enter a valid choice')


main()