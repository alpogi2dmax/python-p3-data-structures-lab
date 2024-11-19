spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_foods_names = list()
    for item in spicy_foods:
        spicy_foods_names.append(item['name'])
    return spicy_foods_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [item for item in spicy_foods if item['heat_level'] > 5]
    return spiciest_foods


def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        chili_level =  "🌶" * item['heat_level']
        print(f"{item['name']} ({item['cuisine']}) | Heat Level: {chili_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item['cuisine'] == cuisine:
            return item

def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        if item['heat_level'] > 5:
            chili_level =  "🌶" * item['heat_level']
            print(f"{item['name']} ({item['cuisine']}) | Heat Level: {chili_level}")

def get_average_heat_level(spicy_foods):
    heat_numbers = list()
    for item in spicy_foods:
        heat_numbers.append(item['heat_level'])
    return sum(heat_numbers) / len(heat_numbers)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
