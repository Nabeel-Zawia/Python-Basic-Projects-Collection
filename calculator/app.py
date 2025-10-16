from logo import logo

print(logo)


def calcluation(num1,operation,num2):
    """A function to calculate the operations coming by user"""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else :
        return "invalid operation type!" 


trigger = True
end = True

while end:
    while trigger:
        num1=float(input("what's the first number?: "))
        operation=input("pick an operation")
        num2=float(input("what's the second number?: "))
        trigger = False
    evaluation = calcluation(num1,operation,num2)
    print(evaluation)
    continue_calculate = input(f"type y to contine with {evaluation} , or n to start a new calculation or e to exit : ").lower()
    if continue_calculate == "y":
        num1 = evaluation
        operation=input("pick an operation")
        num2=int(input("what's the second number?: "))
        
    elif continue_calculate == "n":
        trigger = True

    else:
        end = False