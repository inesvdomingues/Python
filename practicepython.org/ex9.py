import random

player2=random.randint(0,9)
guesses=0

while True:
 player1=input("Insert a number or write exit: ")
 if(player1=="exit"):
  print ("Number of guesses: ",guesses)
  break
 guesses+=1
 if(int(player1)==int(player2)):
  print("Exactly right!")
  #break
 elif (int(player1) < int(player2)):
  print("Too low!")
 else:
  print("Too high!")
