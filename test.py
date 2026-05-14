
store = {
        1 : {"name": "Sword", "description": "Heavy and deals damage", "Coins": 10},
        2: {"name": "Water Bottle", "description": "Refreshing", "Coins": 5}, 
        "Shovel": {"name": "Shovel", "description": "Dig for treasure","Coins": 0}, 
        "WW2 Rations": {"name": "WW2 Rations", "description": "Food for energy", "Coins": 5},
        "Energy Drnk": {"name": "Energy Drink", "description": "Drink for Energy", "Coins": 3},
        "Fishing Rod": {"name": "Fishing Rod", "description": "Fish for Food", "Coins": 6},
        "Raft": {"name": "Life Raft", "description": "Escape Boat To FREEDOM", "Coins": 1000}
        }

consumer = input("Do You Want To Buy From Store??? ").lower
if consumer == "yes":
    print("work")