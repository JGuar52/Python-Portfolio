import random

rock = ''' Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
moves = [rock, paper, scissors]
wins = 0
losses = 0
again = True

print("Let's play Rock, Paper, Scissors!\n")

while again == True:
  print("======================================================================")
  player = input("\nWhat do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")
  if len(player) > 1:
    print("Invalid input!")
    break
  cpu = random.randint(0,2)
  result = player+str(cpu)

  if int(player) == cpu:
    print(f"\nPlayer: {moves[int(player)]} \nCPU: {moves[cpu]} \n\n--It's a tie!--")
  elif result == '02' or result == '10' or result == '21':
    print(f"\nPlayer: {moves[int(player)]} \nCPU: {moves[cpu]} \n\n--Player wins!--")
    wins += 1
  elif result == '01' or result == '12' or result == '20':
    print(f"\nPlayer: {moves[int(player)]} \nCPU: {moves[cpu]} \n\n--CPU wins!--")
    losses += 1
  else:
    print("Invalid input!")

  print(f'''___________________
|Wins: {wins} Losses: {losses}|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
  print("======================================================================")
  prompt = input("Press 'Enter' to play again, or type 'Exit' to quit: ")
  if prompt.upper() == "EXIT":
    again = False
    break
  else:
    again = True
