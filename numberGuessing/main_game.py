def main_game():
    """Main game function for user inputs and returs difficulty"""
    print("welcome to the number guessing game".title())
    print("i'm thinking of a number between 1 and 100.".title())
    difficulty = input("choose a difficulty. type 'easy' or 'hard': ").title().lower()
    return difficulty