import json

#Task 1 — Read the inventory 

with open("data/inventory.json", "r") as file:
    inventory_data = json.load(file)
    print(f"number of books in inventory: {len(inventory_data)}")

#Task 2 — Update and save
new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}
with open("data/inventory.json", "w") as file:
    inventory_data.append(new_book)
    json.dump(inventory_data, file, indent=4)
    

#Task 3 — Display the inventory 
with open("data/inventory.json", "r") as file:
    inventory_data = json.load(file)
    print("Current Inventory:")
    for book in inventory_data:
        print(f"Title: {book['title']}, Author: {book['author']}, Price: ${book['price']}, In Stock: {book['in_stock']}")