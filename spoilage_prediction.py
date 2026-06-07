import random

foods = [
    "Rice",
    "Milk",
    "Bread",
    "Vegetables"
]

for food in foods:
    days = random.randint(1,7)

    print(
        f"{food} likely remains safe for {days} day(s)"
    )