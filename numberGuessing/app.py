from logo import logo
import main_game
import number_guess
import rules
print(logo)


random_number = number_guess.number_guess()
difficulty = main_game.main_game()
rules.rules(difficulty,random_number)
