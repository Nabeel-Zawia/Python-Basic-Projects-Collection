from logo import logo
import data as data_module

resources = data_module.resources
menu = data_module.menu

print(logo)

# TODO : 1. Prompt user by asking what type of coffe they want.

def report(resources):
     """a function to generate a report of the resources in the machine"""
     print(f"water remaining : {resources["water"]} ml")
     print(f"coffee remaining : {resources["coffee"]} g")
     print(f"milk remaining : {resources["milk"]} ml")
     print(f"money collected : ${resources["money"]}")

def machine_resources(water,coffee,milk,price,resources):
    """a function to calculate the whole functionality of the program and svaes new values"""
    QUARTERS = 0.25
    DIMES = 0.10
    NICKLES = 0.05
    PENNIES = 0.01
    
    machine_water,machine_coffee,machine_milk,money = resources.values()
    report(resources)
    if machine_water > water and machine_coffee > coffee and machine_milk > milk:
        resources["water"] -= water
        resources["coffee"] -= coffee
        resources["milk"] -= milk
        print(f"total order price is : ${price}")
        
       
        total_coins_inserted = 0
        max_total_coins_inserted = 0
        while max_total_coins_inserted < price :
            try:
                quarters = int(input("how many quarters do you have: $".title()))
                dimes = int(input("how many dimes do you have: $".title()))
                nickles = int(input("how many nickles do you have: $".title()))
                pennies = int(input("how many pennies do you have: $".title()))
                quarters *= QUARTERS
                dimes *= DIMES
                nickles *= NICKLES
                pennies *= PENNIES
                exchange = 0
                total_coins_inserted = quarters + dimes + nickles + pennies
                resources["money"] += total_coins_inserted
                max_total_coins_inserted += total_coins_inserted
                print(f"insert more money please! coffee price is : ${price} you inserted : ${max_total_coins_inserted}")
            except ValueError:
                print("please enter a number ")
                return
            
            
            
        if total_coins_inserted > price :
            exchange = total_coins_inserted - price
            report(resources)
            print(f"thank you your coffee is ready total price : ${price} , paid : ${total_coins_inserted} , exchange : ${exchange}")
                    
        else:
            report(resources)
            print(f"thank you your coffee is ready total price : ${price} , paid : ${total_coins_inserted} , exchange : ${exchange}")
    else:
         print("no enough ingredints in the machine refill me up , money refunded".title())
    return 

def machine(order,menu):
    """a function to retrive the data of the menu from the data.py file and asssign them to variables to calculate"""
    ingredeints = menu[order]
    water = ingredeints.get("water",0)    
    coffee = ingredeints.get("coffee",0)    
    milk = ingredeints.get("milk",0)    
    price = ingredeints.get("price",0)    
    
    return water , coffee , milk , price
    
        

def main():
    """the main program function that takes the user input and returns it """
    order = ""
    order = input("What whould you like to order ? ( espresso / latte / cappucino ) : ").lower()
    if order == "report":
          print(resources)
          return main()
    elif order == "off" :
          exit()
    else:
        return order

order = main()

water , coffee , milk , price = machine(order,menu)



machine_resources(water,coffee,milk,price,resources)