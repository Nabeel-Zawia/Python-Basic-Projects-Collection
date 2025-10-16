import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.',
    '?', '/', '`', '~'
]

print("Welcome to PYpassword generator!")

letters_input = int(input("How many letters would you like? "))
symbols_input = int(input("How many symbols would you like? "))
numbers_input = int(input("How many numbers would you like? "))

password_letters = []
password_symbols = []
password_numbers = []

for _ in range(letters_input):
    password_letters.append(random.choice(letters))

for _ in range(symbols_input):
    password_symbols.append(random.choice(symbols))

for _ in range(numbers_input):
    password_numbers.append(str(random.choice(numbers)))  

password_list = password_letters + password_symbols + password_numbers
random.shuffle(password_list)  

password = "".join(password_list)
print(f"Your password is: {password}")
