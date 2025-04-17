import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

HANDS_ASCI = [rock,paper,scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(HANDS_ASCI[choice])
print("Computer chose:")
bot_choice = random.randrange(0,2)
print(HANDS_ASCI[bot_choice])

if choice == bot_choice:
    print("Tie")
elif (choice == 0 and bot_choice == 2) or (choice == 1 and bot_choice==0):
    print("You win")
else:
    print("You lose")