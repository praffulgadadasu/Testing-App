
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
        # checks to see if the property the player landed on is available, and then to see if that player owns it. If they don't? rent will be subtracted from that players balance.
        if board[bPos[i]][0] != available[bPos[i]]:                         # Player starts from GO
            if board[bPos[i]][0] not in own[i]:
                rent_owed = random.randint(3,10)
                money[i] = money[i] - rent_owed
                print(f"Unfortunately {board[bPos[i]][0]} is owned by another player. You paid $ {rent_owed} in rent. Your new balance is $ {(money[i])}")
            # if player passes GO index[1] == "no" (go to jail, free parking, etc)
            if board[bPos[i]][1]=="no":
                money[i] = money[i] + 1
        else:
            print(f"Buy for {board[bPos[i]][1]}$")
            if money[i] >= board[bPos[i]][1]:
                money[i]=money[i]-board[bPos[i]][1]
                own[i].append(available[bPos[i]])
                available[bPos[i]]=""
                print("Congratulations! You bought",board[bPos[i]][0])
