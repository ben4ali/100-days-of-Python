CHEST_ASCII_ART = """
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"''"-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." '.."` . "-._ _______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
"""
print(CHEST_ASCII_ART)
print("Welcome to Treasure Island.\nYou're mission is to find the treasure.\nYou're at a cross road. Where do you want to go?")
direction = input('\tType "left or "right"\n')
if direction=="left":
    choice = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if choice == "swim":
        print("Oh no! the lake is infested with sharks. Game Over.")
    elif choice == "wait":
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if color == "red":
            print("It's a room full of fire. Game Over.")
        elif color == "yellow":
            print("You find a suspicious patch of dirt in the middle of the room and start digging.")
            print("You hear a bang and then...")
            print("Congratulation! You have found the chest.")
        elif color == "blue":
            print("The door closes behind you and water start rising till you drown. Game over.")
elif direction == "right":
    print("The road leads you to a hungry lion. Game over.")