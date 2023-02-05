import random
import array

maxLength = 16
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']
upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']

combined = numbers + upperCase + lowerCase + symbols

randDigit = random.choice(numbers)
randUpper = random.choice(upperCase)
randLower = random.choice(lowerCase)
randSymbol = random.choice(symbols)

tempPass = randDigit + randUpper + randLower + randSymbol

for x in range(maxLength - 4):
	tempPass = tempPass + random.choice(combined)

	tempPassList = array.array('u', tempPass)
	random.shuffle(tempPassList)
  
password = ""
for x in tempPassList:
		password = password + x
print(password)
