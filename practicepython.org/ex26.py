def check_winner(game):
    board_size=len(game)    
   
    #check horizontal lines:
    for i in range(0,board_size):
        if(game[i][0] == game[i][1] and game[i][1] == game[i][2] and game[i][0] != 0 ):
            print ("The winner is the player {}!" .format(game[i][0]))
            return
    
    #check vertical lines:
    for i in range(0,board_size):
        if(game[0][i] == game[1][i] and game[1][i] == game[2][i] and game[0][i] != 0 ):
            print ("The winner is the player {}!" .format(game[0][i]))
            return

    #check cross lines:
    if(game[0][0] == game[1][1] and game[1][1] == game[2][2] and game[0][0] != 0 ):
        print ("The winner is the player {}!" .format(game[0][0]))
        return
    
    if(game[0][2] == game[1][1] and game[1][1] == game[2][0] and game[0][2] != 0 ):
        print ("The winner is the player {}!" .format(game[0][2]))
        return

    print("No winner, sorry!")
    

my_game = [[1, 2, 0],[2, 1, 0],[2, 1, 1]]
check_winner (my_game)

#test cases:
winner_is_2 = [[2, 2, 0],	[2, 1, 0],	[2, 1, 1]]
winner_is_1 = [[1, 2, 0],	[2, 1, 0],	[2, 1, 1]]
winner_is_also_1 = [[0, 1, 0],	[2, 1, 0],	[2, 1, 1]]
no_winner = [[1, 2, 0],	[2, 1, 0],	[2, 1, 2]]
also_no_winner = [[1, 2, 0],	[2, 1, 0],	[2, 1, 0]]    
#check_winner (winner_is_1)