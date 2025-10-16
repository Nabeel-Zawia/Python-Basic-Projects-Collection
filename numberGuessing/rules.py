def rules(difficulty,number):
    """a function that has the rules of the game to make it functional"""
    end = True
    if difficulty == "easy":
        attempts=10
    elif difficulty == "hard":
        attempts=5
    while end :
        
        print(f"You have {attempts} attempts".title())
        guess = int(input("make a guess:").title())
    
        if guess == number:
            print(f"You won the number was : {number}")
            end = False
        elif guess > number :
            print(f"you choose {guess} too high")
            attempts -=1
        elif guess < number :
            print(f"you choose {guess} too low")
            attempts -=1     
        if attempts == 0 :
            print(f"You lose the number was {number}")
            end = False