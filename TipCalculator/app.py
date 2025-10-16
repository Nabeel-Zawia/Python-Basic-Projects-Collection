print("welcome to the bill tip calculator")
Full_price=float(input("Enter the full bill price: "))
Amount_of_tip=int(input("Enter the amount of tip you are going to give: "))
Share_amoung_persons=int(input("how many persons are there in this table: "))
Bill_with_tip= Amount_of_tip/100 * Full_price + Full_price
Bill_person = round(Bill_with_tip / Share_amoung_persons,2)
print(f"Each person should pay: {Bill_person} ")