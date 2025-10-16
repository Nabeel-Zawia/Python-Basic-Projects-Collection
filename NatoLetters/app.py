import pandas as pd


nato_df = pd.read_csv('nato_phonetic_alphabet.csv')


nato_dict = {row.letter: row.code for _, row in nato_df.iterrows()}




def main_function():
    try:
        user_input = input("enter a word: ").upper()
        result = {letter:nato_dict[letter] for letter in user_input}
        output_list = list(result.values())
        print(output_list)
    except KeyError as error:
        print("sorry you should only enter letters!")
        main_function()


main_function()