import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
all_moves = [rock, paper, scissors]
computer_move = random.randint(0,2)
# print(all_moves[computer_move])
user_move = input('''What is your move:\n
Choose 0 for ROCK\n
Choose 1 for PAPER\n
Choose 2 for SCISSORS\n
''')
if(user_move == '0'):
  print(f"Your move: {all_moves[0]}")
  print(f"Computer move: {all_moves[computer_move]}")
  if(computer_move == 0):
    print("It is a tie")
  elif(computer_move == 1):
    print("User lost")
  elif(computer_move == 2):
    print("User won")
elif(user_move == '1'):
  print(f"Your move: {all_moves[1]}")
  print(f"Computer move: {all_moves[computer_move]}")
  if(computer_move == 1):
    print("It is a tie")
  elif(computer_move == 0):
    print("User won")
  elif(computer_move == 2):
    print("Computer lost")
elif(user_move == '2'):
  print(f"Your move: {all_moves[2]}")
  print(f"Computer move: {all_moves[computer_move]}")
  if(computer_move == 2):
    print("It is a tie")
  elif(computer_move == 1):
    print("Computer lost")
  elif(computer_move == 0):
    print("User won")
else:
  print("Invalid Move")
  exit()
