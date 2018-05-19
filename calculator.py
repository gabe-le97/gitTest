def add(num1, num2):
	return num1+num2

def subtract(num1, num2):
	return num1-num2

def multiplication(num1, num2):
	return num1*num2

def printf(format, *values):
	print(format % values )

def division(num1, num2):
	return num1/num2

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
		print('\nEnter a choice')
		choice = checkInput(num)
		if(choice == 1):
			print('Addition')
			print(add(num1, num2))
		elif(choice == 2):
			print('Subtraction')
			print(subtract(num1, num2))
		elif(choice == 3):
			print('Division')
			print(division(num1,num2))
		elif(choice == 4):
			print("multiplication")
			print(multiplication(num1, num2))
		else:
			print('Goodbye')
			exit(0)


main()
