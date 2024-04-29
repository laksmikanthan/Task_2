import json

# Read the JSON file and load it into a dictionary
with open('ex5.json', 'r') as file:
    ex5 = json.load(file)

# Add a new batter named "Tea" for the donut with the name "Old Fashioned"
for donut in ex5:
    if donut["name"] == "Old Fashioned":
        donut["batters"]["batter"].append({"id": "1003", "type": "Tea"})
        break

#  updated dictionary 
with open('ex5.json', 'w') as file:
    json.dump(ex5, file, indent=4)
