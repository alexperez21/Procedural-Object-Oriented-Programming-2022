askUser = (input("Enter a message: ")).lower()
frequency = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
alphabet = "abcdefghijklmnopqrstuvwyxz"

for i in range(len(alphabet)):
  if alphabet[i] in askUser:
    frequency[i] = askUser.count(alphabet[i])

length = len(askUser)

for j in range(len(frequency)):
  frequency[j] = (frequency[j] / length)
  frequency[j] = (frequency[j] * 100)
  if frequency[j] != 0.0:
    print(f"{alphabet[j]}: {round(frequency[j],2)}%")
  
  
