
Coins = 30


store = {
        1 : {"name": "Sword", "description": "Heavy and deals damage", "Coins": 10},
        2: {"name": "Water Bottle", "description": "Refreshing", "Coins": 5}, 
        3 : {"name": "Shovel", "description": "Dig for treasure","Coins": 0}, 
        4 : {"name": "WW2 Rations", "description": "Food for energy", "Coins": 5},
        5 : {"name": "Energy Drink", "description": "Drink for Energy", "Coins": 3},
        6 : {"name": "Fishing Rod", "description": "Fish for Food", "Coins": 6},
        7 : {"name": "Life Raft", "description": "Escape Boat To FREEDOM", "Coins": 1000}
        }

consumer = input("Do You Want To Buy From Store???").lower()
if consumer == "yes":
        for i in range(1,7):
                print(store[i]["name"])
        buy = input("Buy WHat?")
        for x in range(1,7):
                store[x][buy]

