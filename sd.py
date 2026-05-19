
Coins = 30
cart = []

store = [
         {"name": "Sword", "description": "Heavy and deals damage", "Coins": int(10)},
         {"name": "Water Bottle", "description": "Refreshing", "Coins": 5}, 
         {"name": "Shovel", "description": "Dig for treasure","Coins": 0}, 
         {"name": "WW2 Rations", "description": "Food for energy", "Coins": 5},
         {"name": "Energy Drink", "description": "Drink for Energy", "Coins": 3},
         {"name": "Fishing Rod", "description": "Fish for Food", "Coins": 6},
         {"name": "Life Raft", "description": "Escape Boat To FREEDOM", "Coins": 1000}
        ]





while True:
    for index, items in enumerate(store):
        print(index, ":", items["name"],"-", "Description:", items["description"], "-", "Cost:", items["Coins"])

    asker = int(input("Buy What?? ")) 
    if Coins > store[asker]["Coins"]:
        Coins -= store[asker]["Coins"]
        cart.append(store[asker]["name"])
        print(cart)
        print(Coins)
    else:
        print("You're Too Poor")

    asker = input('Do You Want To Continue??').upper()
    if asker == "NO":
        break



