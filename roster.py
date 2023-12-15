# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": ["High", "Ryan", "Davis"],
          "First Name": ["Zayden", "Cormac", "RJ"],
          "height": [81, 77, 72],
          "weight": [225, 195, 180]}
data = pd.DataFrame(player)
print(data)

