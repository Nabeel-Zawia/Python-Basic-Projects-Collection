import random

a = input("flip the coin head or tail!: head = 0 tail =1: ")

if a ==0:
    a="head"
else:
    a="tail"
print(f"your choice was {a}")
b=random.randint(0,1)

if b == 0 :
    b="head"
else:
    b="tail"

print(f"computer choice was {b}")

