# import choice function to randomly choose from list  
from random import choice  
# randomly assigns computers choice  
computer = choice(["rock", "paper", "scissors"])
askUser = input("Enter a choice (rock, paper, scissors): ")

print(f"\nYou chose {askUser}, computer chose {computer}.\n")
if askUser == computer:
    print(f"Both players selected {askUser}. It's a tie!")
elif askUser == "rock":
    if askUser == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose!")
elif askUser == "paper":
    if askUser == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose!")
elif askUser == "scissors":
    if askUser == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose!")
