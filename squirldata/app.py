import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

Fur_Color = data["Primary Fur Color"]

gray = 0
cinnamon = 0
red = 0

for _ in data["Primary Fur Color"]:
    if _ == "Gray":
        gray+=1
    elif _ == "Cinnamon":
        cinnamon +=1
    elif _ == "Red":
        red =+1

new_data = {
    "Fur Color" : ["Gray" , "Cinnamon" , "Red"],
    "Count" : [gray,cinnamon,red]
}

csv_data = pandas.DataFrame(new_data)

csv_data.to_csv("new_squirl_data.csv")