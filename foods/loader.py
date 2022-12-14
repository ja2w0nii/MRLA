import json


with open("foods/csvjson.json", "r", encoding="UTF-8") as f:
    foods = json.load(f)

with open("foods/major_category.json", "r", encoding="UTF-8") as f:
    categories = json.load(f)

new_list = []
for category in categories:
    new_data = {"model": "foods.majorcategory"}
    new_data["fields"] = category
    new_list.append(new_data)
    
for food in foods:
    new_data = {"model": "foods.food"}
    new_data["fields"] = food
    new_list.append(new_data)

with open("foods/fixtures.json", "w", encoding="UTF-8") as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)
