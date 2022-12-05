import json

with open('foods/foods.json', 'r', encoding='UTF-8') as f:
    foods = json.load(f)

new_list = []
for food in foods:
    new_data = {"model": "foods.food"}
    new_data["fields"] = food
    new_list.append(new_data)

with open('foods/foods_data.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)
