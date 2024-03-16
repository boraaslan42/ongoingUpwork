import json


with open("links.json") as f:
    data = json.load(f)

chap = int(input("Enter the chapter number (1,2,3,...,11): "))
chapter = data[str(chap)]
target_key = (input("Enter the problem number (1,2,3,...): ")) + "E"


found_solution = None

for item in chapter:
    if target_key in item:
        found_solution = item[target_key]

        break
print(found_solution)
#bora aslan zart zort