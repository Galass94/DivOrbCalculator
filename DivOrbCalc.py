import requests
import json

divOrbCount = float(input("Divine Orb Calculator\nHow many orbs do you need to pay in chaos?\n").replace(",", "."))

values = requests.get("https://poe.ninja/api/data/currencyoverview?league=Kalandra&type=Currency").text
valuesJson = json.loads(values)
# print(valuesJson["lines"][0])
for i in valuesJson["lines"]:
    if i["detailsId"] == "divine-orb":
        divOrbValue = i["receive"]["value"]
print(f"That's {round((divOrbValue)*(divOrbCount))} Chaos Orbs")