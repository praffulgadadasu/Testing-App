
import json
import random


# list where players are added
players=["Peter", "Billy", "Charlotte", "Sweedal"]

# Total Number of players
numOfPlayers = 4

# 2D board list 
board=[["GO","no"],["The Burvale",1],["Fast Kebabs",1],["The Grand Tofu",2],["Lanzhou Beef Noodle",2],["Betty's Burgers",3],["YOMG",3],["Gami Chicken",4],["Massizim",4]]

# showing what is available
available=["GO","The Burvale","Fast Kebabs","The Grand Tofu","Lanzhou Beef Noodle","Betty's Burgers","YOMG","Gami Chicken","Massizim"]

# each players starting board position 
bPos=[0,0,0,0]

# each players portfolio
own=[[],[],[],[]]

# balance of each player
money=[16,16,16,16]

# Dice Roll
rolls_1 = [1, 3, 1, 1, 1, 2, 4, 2, 6, 3, 5, 2, 2, 2, 4, 4, 6, 1, 4, 2, 6, 2, 1, 5, 4, 5, 6, 5, 6, 3, 6, 4, 4, 3, 5, 6, 2, 1, 6, 5, 1, 1, 6, 4, 5, 2, 2, 3, 5, 6]
rolls_2 = [5, 2, 2, 1, 4, 1, 2, 1, 3, 1, 4, 3, 5, 2, 3, 1, 3, 1, 1, 3, 4, 2, 1, 3, 2, 3, 5, 5, 3, 2, 4, 5, 2, 6, 5, 4, 3, 6, 2, 5, 5, 3, 2, 6, 5, 2, 6, 2, 6, 4, 5, 5, 6, 1, 6, 6, 2, 6, 4, 1, 1, 2, 6, 6, 6, 2, 1, 4, 6, 3, 5, 4, 1, 4, 2, 1, 5, 5, 2, 3, 3, 3, 4, 1, 2, 4, 5, 4, 5, 2, 2, 2, 2, 6, 1, 5, 3, 6, 3, 2]
game = True
while game == True:
    #Set the dice value for player position
    for i in range(numOfPlayers):
        bPos[i] = rolls_1[i] + bPos[i]
        # property the player landed on is not available, and if they don't own it? rent will be subtracted from that players balance.
        if board[bPos[i]][0] != available[bPos[i]]:
            if board[bPos[i]][0] not in own[i]:
                rent_owed = 3
                money[i] = money[i] - rent_owed
                print(f"Unfortunately {board[bPos[i]][0]} is owned by another player. You paid $ {rent_owed} in rent. Your new balance is $ {(money[i])}")
                
                # Adding the person rented money to the person who owned the property
                if board[bPos[i]][0] in own[0]:
                    money[0] +=3
                elif board[bPos[i]][0] in own[1]:
                    money[1] += 3
                elif board[bPos[i]][0] in own[2]:
                    money[2] += 3
                elif board[bPos[i]][0] in own[3]:
                    money[3] += 3 

        
        # property the player landed is available, and want to buy it? money will be subtracted from their initial money and property will be added into their owned portfolio
        else:
            print(f"Buy for {board[bPos[i]][1]}$")
            if money[i] >= board[bPos[i]][1]:
                money[i]=money[i]-board[bPos[i]][1]
                own[i].append(available[bPos[i]])
                available[bPos[i]]=""
                print(f"Congratulations! {players[i]} bought {board[bPos[i]][0]}. Your new balance is {(money[i])}$")
            else:
                print("Uh oh! You can't afford this!")
        print(f"Board Position will be {bPos[i]} and owned properties will be {own[i]}")
            
