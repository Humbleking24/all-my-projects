import random

rock = '🪨'
scissor = '✄'
paper = '📃'
l=[rock,paper,scissor]

player_choose = input('choose one of the following rock, paper, scissor:')

if(player_choose == 'rock', 'paper', 'scissor' or player_choose == 'Rock', 'Paper', 'Scissor' or player_choose == 'ROCK', 'PAPER', 'SCISSOR'):
    computer_choose = random.choice(l)
    print ("The computer chooses:",computer_choose)
    if (player_choose == 'rock' and computer_choose == scissor):
        print("Player Wins")
    elif(player_choose == 'rock' and computer_choose == paper):
        print('Computer Wins')
    elif(player_choose == 'rock' and computer_choose == rock):
        print("Its a Tie")
    if (player_choose == 'paper' and computer_choose == scissor):
         print("Computer Wins")
    elif(player_choose == 'paper' and computer_choose == paper):
           print('Its a Tie')
    elif(player_choose == 'paper' and computer_choose == rock):
          print("Player Wins")
    if (player_choose == 'scissor' and computer_choose == scissor):
        print("Its a Tie")
    elif(player_choose == 'scissor' and computer_choose == paper):
        print('Player Wins')
    elif(player_choose == 'scissor' and computer_choose == rock):
        print("Computer Wins")
