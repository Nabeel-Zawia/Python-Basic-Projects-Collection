from logo import logo
import random
from os import system
print(logo)

def hit_pass(decide,user_score,computer_score):
    """ function to calculate the sum of the cards"""
    
    for i in user_cards:
        if isinstance(i,str):
            if i in cards_deck["super_cards"]:
                i=cards_deck["super_cards"][i]
            else:
                if i == "A":
    # Pick 11 if user_score + 11 <= 21, else 1
                    if user_score + 11 <= 21:
                        i = 11
                    else:
                        i = 1

        user_score +=i
        
        
    for j in computer_cards:
        if isinstance(j,str):
            if j in cards_deck["super_cards"]:
                j=cards_deck["super_cards"][j]
            else:
                if j == "A":
    # Pick 11 if user_score + 11 <= 21, else 1
                    if user_score + 11 <= 21:
                        j = 11
                    else:
                        j = 1

        computer_score +=j
    return user_score , computer_score


cards_deck = {
    "regular_cards": [2, 3, 4, 5, 6, 7, 8, 9, 10],
    "super_cards": {
        "Q": 10,
        "K": 10,
        "J": 10
    },
    "fate_card": {
        "A": [1, 11]
    }
}
user_cards = []
computer_cards = []
computer_choice = ["hit","pass"]
user_score = 0
computer_score = 0
computer_decide = ""
user_decide = ""
end = True
# Flatten all possible card values into a list
all_cards = cards_deck["regular_cards"] + list(cards_deck["super_cards"].keys()) + list(cards_deck["fate_card"].keys()) 

# Pick a random card
user_cards = random.sample(all_cards,2)
computer_cards = random.sample(all_cards,2)

print("Welcome to blackjack21!!!!!")
name = input("Enter Your Name: ")
system("cls")
print(logo)
print(f"Welcome {name} , its you vs computer !, lets goooo")



# def calculation():


while end:
     print(f"{name} cards set are: {user_cards}")
     print(f"Computer cards set are: {computer_cards[0]}")

     decide = input("Hit or Pass: ").lower()
     user_decide = decide
     if decide == "hit":
         
         user_cards.append(random.choice(all_cards))
         print(f"{name} Hit Waiting for computer.....")
         user_score, computer_score = hit_pass(decide,user_cards,computer_cards)
     decide = random.choice(computer_choice)
     computer_decide = decide
     if decide == "hit":
        
        computer_cards.append(random.choice(all_cards))
        user_score, computer_score =  hit_pass(decide,user_cards,computer_cards)
        print(f"computer {decide}")
        print(f"{name} cards set are: {user_cards}")
        print(f"Computer cards set are: {computer_cards[0]}")
     if user_decide == "pass" and computer_decide == "pass":
        user_score, computer_score = hit_pass(decide,user_cards,computer_cards)
        continue
     
     if user_score <= 21 or computer_score <= 21 :
         
         if user_score > computer_score and user_score <= 21 or computer_score > 21 and user_score <=21:
             print(f"{name} wins the game with {user_score} , computer score : {computer_score}")
         elif computer_score > user_score and computer_score <=21 or user_score > 21 and computer_score <= 21:
             print(f"Computer wins the game with {computer_score} , {name} score : {user_score}")
         elif user_score == computer_score:
             print(f"tie {name} score : {user_score} , computer score : {computer_score}")
         else:
             print(f"both loses {name} score : {user_score} , computer score : {computer_score}")    
         end = False

