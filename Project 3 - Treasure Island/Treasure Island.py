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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

step1 = input("You're at a crossroad. Where do you want to go? Press 'L' for Left and 'R' Right. ").lower()

if step1 == "l":
  step2 = input("You have come to a lake. There is an island in the middle of the lake. Press 'S' for Swim and 'W' for Wait.\n").lower()
  if step2 == "w":
    step3 = input("You arrived at the island unharmed. There is a house with 3 doors. Choose 'R' for Red Door, 'B' for Blue Door, 'Y' for Yellow Door.\n").lower()
    if step3 == "y":
      print("You Win.")
    elif step3 == "r":
      print("Burned by Fire. Game Over!")
    elif step3 == "b":
      print("Eaten by Beasts. Game Over!")
    else:
      print("Sorry... You chose the door that does not exist. Game Over!")
  elif step2 != "w":
    print("Attacked by trout. Game Over!")

elif step1 != "l":
  print("You fall into a hole. Game Over!")
else:
  print("Game Over!")
