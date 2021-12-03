import random

print("WELCOME TO THE ROCK PAPER SCISSORS GAME ^__________^")

rock = '''

     _____________
----'     _________)
         (__________)
         (___________)
----.    (__________)
     '____(________)
'''
paper='''
     _________
----'      ___)______
           __________)
           ___________)
----       __________)
    '____________)
'''

scissors='''
     _____________
----'         _____)______
              _____________)
              ______________)
----         (_______)
    ''_______(______)
'''
game_images = [rock,paper,scissors]

your_choice=int(input("What is your choice? Type 0 for rock,1 for paper or 2 for scissors\n"))

if(your_choice > 2 and computer_choice < 0):
    print("You type an invalid number,you lose")
else:
    print(game_images[your_choice])

    computer_choice = random.randint(0,2)
    print("computer choice:")
    print(game_images[computer_choice])

    if(computer_choice > your_choice):
        print("You lose")
    elif(computer_choice == 0 and your_choice== 2):
        print("You lose")
    elif(your_choice == 0 and computer_choice == 2):
        print("You wins")
    elif(your_choice > computer_choice):
        print("You wins")
    elif(your_choice == computer_choice):
        print("It's a draw")
