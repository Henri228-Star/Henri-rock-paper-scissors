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
import random

# Start the  game
print("Welcome to the Rock-Paper-Scissors game! Let\'s go!")

# Capturing the user input
player = input("Rock...Paper...Scissors.... What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
# Converting the user input
player_int = int(player)
# Listing the parameters of the game
list = [rock, paper, scissors]

# Calling the import function
cpu = random.randint(0,len(list)-1)

# Putting the if statements into perspective and combining the list and possible outcomes into the print statements

if player_int >= 3 or player_int < 0:
  print("You have typed an invalid number, you lose!")
elif player_int == 0 and cpu == 2:
  print(f"{list[0]}\n Computer Chose:\n {list[2]} \n You win.")
elif player_int == 1 and cpu == 0:
  print(f"{list[1]}\n Computer Chose:\n {list[0]} \n You win.")
elif player_int == 2 and cpu ==1:
  print(f"{list[2]}\n Computer Chose:\n {list[1]} \n You win.")
elif player_int == cpu:
  print(f"{list[player_int]}\n Computer chose: \n {list[cpu]} \n It\'s a draw" )
  
# This last statement might not be relevant
else:
  print(f"{list[player_int]}\n Computer chose: \n {list[cpu]} \n Error! Try again" )

