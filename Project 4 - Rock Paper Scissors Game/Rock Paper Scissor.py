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
print("Welcome to Rock Paper Scissors Game...")
user = int(input("What do you choose? Type \n0 for Rock\n1 for Paper\n2 for Scissors:\n"))
comp = random.randint(0,2)

if user == 0:
  if comp == 0:
    print("\n\nYour Choice:\n")
    print(rock)
    print("\n\nComputer Choice:\n")
    print(rock)
    print("Draw.")
  elif comp == 1:
    print("Your Choice:\n")
    print(rock)
    print("\n\nComputer Choice:\n")
    print(paper)
    print("You Lose.")
  elif comp == 2:
    print("Your Choice:\n")
    print(rock)
    print("\n\nComputer Choice:\n")
    print(scissors)
    print("You Won.")
  else:
    print("Wrong Choice.")

elif user == 1:
  if comp == 0:
    print("Your Choice:\n")
    print(paper)
    print("\n\nComputer Choice:\n")
    print(rock)
    print("You Won.")
  elif comp == 1:
    print("Your Choice:\n")
    print(paper)
    print("\n\nComputer Choice:\n")
    print(paper)
    print("Draw.")
  elif comp == 2:
    print("Your Choice:\n")
    print(paper)
    print("\n\nComputer Choice:\n")
    print(scissors)
    print("You Lose.")
  else:
    print("Wrong Choice.")
elif user == 2:
  if comp == 0:
    print("Your Choice:\n")
    print(scissors)
    print("\n\nComputer Choice:\n")
    print(rock)
    print("You Lose.")
  elif comp == 1:
    print("Your Choice:\n")
    print(scissors)
    print("\n\nComputer Choice:\n")
    print(paper)
    print("You Won.")
  elif comp == 2:
    print("Your Choice:\n")
    print(scissors)
    print("\n\nComputer Choice:\n")
    print(scissors)
    print("Draw.")
  else:
    print("Wrong Choice.")
