import random

rock = 0
paper = 1
scissors = 2

user_choice = int(input("What do you choose? 0 = rock, 1 = paper, or 2 = scissors: "))
print(f"Your choice was: {user_choice}")
computer_choice = random.randint(0, 2)
print(f"Computer choice was: {computer_choice}")

# Determine winner
if user_choice == rock and computer_choice == scissors or \
   user_choice == paper and computer_choice == rock or \
   user_choice == scissors and computer_choice == paper:
    print("You won")
elif user_choice == computer_choice:
    print("It's a tie")
else:
    print("You lose")
