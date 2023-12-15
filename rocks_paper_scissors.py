import random

def rocks_ppr_scissors():
   player_1 = input("Choose one:\n-rock\n-paper\n-scissors\n\n") 
   player_2 = ["rock","paper","scissors"]
   computer_action = random.choice(player_2)
   print(f"Player 1: {player_1}")
   print(f"Player 2: {computer_action}")

   if player_1 == player_2:
      print ("It's a tie!")
   elif player_1 == "rock":
      if player_2 == "scissors":
         print ("Rock smashes scissors, you win!")
      else:
         print ("Paper covers rock, you lose!")
   elif player_1 == "scissors":
      if player_2 == "rock":
         print ("Rock smashes scissors, you lose!")
      else:
         print ("Scissors cut paper, you win!")
   elif player_1 == "paper":
      if player_2 == "scissors":
         print ("Scissors cut paper, you lose!")
      else:
        print ("Paper covers rock, you win!") 

rocks_ppr_scissors()