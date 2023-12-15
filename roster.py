# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": ["High", "Ryan", "Davis", "Cadeau", "Bacot", "Trimble", "Wojcik", "Washington", "Lebo", "Landry"],
          "First Name": ["Zayden", "Cormac", "RJ", "Elliot", "Armando", "Seth", "Paxson", "Jalen", "Creighton", "Rob"],
          "height": [81, 77, 72, 73, 83, 75, 77, 82, 73, 76],
          "weight": [225, 195, 180, 180, 240, 195, 195, 230, 180, 190]}

data = pd.DataFrame(player)

# bmi = weight in kg/height in meters squared 
data["bmi"] = round((data["weight"]/2.205)/((data["height"]/39.37)**2),2)

print(data)

data.to_csv("bmi.csv")

