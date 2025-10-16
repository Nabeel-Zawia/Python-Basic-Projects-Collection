print("Welcome to arden pizza delivery shop!")
size = input("what size do you want? s,m,l: ")
pepperoni = input("Do you want pepperooni on you pizza? y or n")
extra_cheese = input("do you want extra chesse? y or n")
bill = 0
print(f"size you choosen is {size}")


if size =="s":
    bill += 15
    if pepperoni == "y":
        print("pepperoni added to your order")
        bill +=2
elif size =="m":
    bill += 20
    if pepperoni == "y":
        print("pepperoni added to your order")
        bill +=3
elif size == "l":
    bill += 25
    if pepperoni == "y":
        print("pepperoni added to your order")
        bill +=3
else:
    print("enter a proper size please")

if extra_cheese == "y":
    print("extra cheese added to your order")
    bill +=1

print (f"Your order bill wil be : {bill}")