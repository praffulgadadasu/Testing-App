# list where players are added
import json
from operator import le


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
rolls_1 = [1, 3, 1, 1, 1, 2, 4, 2, 6, 3, 5, 2, 2, 2, 4, 4, 6, 1, 4, 2, 6, 2, 1, 5, 4, 5, 6, 5, 6, 3, 6, 4, 4, 3, 5, 6, 2, 1, 6, 5, 1, 1, 6, 4, 5, 2, 2, 3, 5, 6]
rolls_2 = [5, 2, 2, 1, 4, 1, 2, 1, 3, 1, 4, 3, 5, 2, 3, 1, 3, 1, 1, 3, 4, 2, 1, 3, 2, 3, 5, 5, 3, 2, 4, 5, 2, 6, 5, 4, 3, 6, 2, 5, 5, 3, 2, 6, 5, 2, 6, 2, 6, 4, 5, 5, 6, 1, 6, 6, 2, 6, 4, 1, 1, 2, 6, 6, 6, 2, 1, 4, 6, 3, 5, 4, 1, 4, 2, 1, 5, 5, 2, 3, 3, 3, 4, 1, 2, 4, 5, 4, 5, 2, 2, 2, 2, 6, 1, 5, 3, 6, 3, 2]
a = len(rolls_1)
b = len(rolls_2)
print(f'a is {a} and b is {b}')

