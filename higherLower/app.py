import logo as logo_module
import data as data_module
import random

logo = logo_module.logo
vs = logo_module.vs
data = data_module.data
score = 0

print(logo)

def random_high(data):
    """a function to choose a random dictionary from the data list"""
    compareA = random.choice(data)
    compareB = random.choice(data)
    return compareA,compareB
    
def wrong_answer(wrong, correct):
    """finding a new opponent function for the losing one only """
    newA = wrong
    _ , newB = random_high(correct)   # the underscore here is used for a variable to match the function requirements without the need or care for the value the underscore has
    return newA,newB

def main_game(compareA, compareB):
    """main game function with the rules of higher or lower"""
    global score
    print(f"\nCompare A: {compareA['name']} is {compareA['description']} from {compareA['country']}")
    print(vs)
    print(f"Compare B: {compareB['name']} is {compareB['description']} from {compareB['country']}")
    
    choice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()

    if choice not in ["a", "b"]:
        print("Invalid choice! Please enter 'a' or 'b'.")
        return compareA, compareB, True  # replay the same round

    if compareA['followers'] > compareB['followers']:
        correct = 'a'
    elif compareA['followers'] < compareB['followers']:
        correct = 'b'
    else:
        print("It's a tie!")
        return compareA, compareB, True  # replay the same round

    if choice == correct:
        score += 1
        print(f"You're right! Current score: {score}")
        if correct == 'a':
            return compareA, compareB, True
        else:
            return compareB, compareA, True
    else:
        print(f"You're wrong! Final score: {score}")
        return None, None, False
    
end = True
compareA, compareB = random_high(data)

while end:
    compareA, compareB, end = main_game(compareA, compareB)
    if end:
        compareA, compareB = wrong_answer(compareA, data)