print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

decisionOne = input("You come upon a crossroad. Which direction do you choose? Left or Right.\n").lower()
if decisionOne == "right":
    print("You've activated a trap and spikes end your hunt early.")
elif decisionOne == "left":
    print('You\'ve come to a large lake. What do you do?')
    decisionTwo = input("Swim or wait?\n").lower()
    if decisionTwo == "swim":
        print("You were suddenyly swarmed by Aligators and are torn to pieces.")
    elif decisionTwo == "wait":
        print("Wise decision. A boat comes for you and carries you safely across.")
        finalDecision = input("Once you cross the lake, you are met with 3 doors. Which door to choose: Red, Blue or Yellow?\n").lower()
        if finalDecision == "red":
            print("An angry, giant Orc spots you and crushs you!")
        elif finalDecision == "yellow":
            print("You set off a trap and an explosion ends your treasure hunt.")
        else:
            print("Congratulations! You found the treasure!")