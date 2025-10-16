from logo import logo
alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(encode_or_decode, sentence, shift):
    output_text = ""
    
    if encode_or_decode == "decrypt":
        shift = -shift

    for letter in sentence:
       
        if letter in alphabets:
            shifted_position = (alphabets.index(letter) + shift) % len(alphabets)
            output_text += alphabets[shifted_position]
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}ed result: {output_text}")
print(logo)

should_continue = True

while should_continue == True:

    direction = input("Hello there, do you want to encrypt or decrypt? Type 'exit' to close the program: ").lower()
    sentence = input("Enter a sentence (lowercase only): ").lower()
    shift = int(input("Enter the amount of shift: "))

    caesar(direction, sentence, shift)

    restart= input("Type yes if you want to go again , otherwise type no ").lower()
    if restart == "no":
        print("Goodbye")
        should_continue = False
        
