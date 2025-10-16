#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open('Input/Names/invited_names.txt', mode='r') as invited:
    Names = invited.readlines()
    Names = [name.strip("\n") for name in Names]
    print(Names)

with open('Input/Letters/starting_letter.txt', mode="r") as template:
    letter = template.read()
    

for name in Names:
    with open(f'Output/ReadyToSend/{name}', mode="w") as ready:
        person_letter = letter.replace("[name]",name)
        messeage = ready.write(person_letter)
        
