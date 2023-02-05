import random

j = open("joke.txt", "r")
jokes = j.read().split("\n")

def display():
  y = str(input("Would you like to hear a joke? (y/n): "))

  if y == "y":
    print(random.choice(jokes))
    display()
  else:
    print("Good Bye!")

display()


