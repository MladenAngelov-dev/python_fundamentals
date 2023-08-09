
plants = {"Arnoldii": {"rarity": 4, "rating": [3.5, 4.3, 3.2]}}
for plant, value in plants.items():
    avarage_rating = sum(value['rating'])/ len(value['rating'])
    print(f"Plant:{plant} Raraty: {value['rarity']} Rating:{avarage_rating:.2f}")