import random

options = ["Rock", "Paper", "Scissors"]
player1=input("Rock, Paper, Scissors: ")
 
if(player1 not in options):
 print("Invalid play!")
else:
 player2=options[random.randint(0,2)]
 
print("Player 2: ", player2)
#First check draws!
if (player1==player2):
 print('Call it a draw!')
else:
 #Find the winner:
 if player1 == "Rock" and player2 == "Scissors":
   print("Player 1 won!")
 elif player1 == "Paper" and player2 == "Rock":
   print("Player 1 won!")
 elif player1 == "Scissors" and player2 == "Paper":
   print("Player 1 won!")
 else:
   print("Player 2 won!")