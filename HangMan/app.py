random_word = ""
display = ""
guess = ""
words = ["programmer", "designer", "juicewrld", "keyboard", "mouse", "monitor"]

import random

random_word = random.choice(words)
display = "_ " * len(random_word)
print(display.strip())

while "_ " in display:
    guess = input("\nEnter a letter: ").lower()

    new_display = ""
    for i in range(len(random_word)):
        if random_word[i] == guess:
            new_display += guess + " "
        else:
            new_display += display.split()[i] + " "

    display = new_display.strip()
    print(display)

print("\nCongratulations, you've guessed the word:", random_word)
