#Desmend Thomas
#12th Period
#Computer Programming
##Game Marathon
#ALPHA FINISHED
#Single player games against AI
def menu():
    print('''
-GAME MENU-
    This is a 2 game Marathon, more like a sprint. Fist game will be a number guessing game, and
    the second will be a classic game of Rock Paper Scissors. Have fun and finish strong!!
    (PRESS 
    1. Game Marathon
    2. Quit
    -GAME MENU-
    
    1. Game Marathon
    2. Quit
    

    (Press either 1, or 2)
    ''')
    choice=input(": ")
    if choice=='1':
        ('LOADING..... ')
    elif choice=='2':
        quit()
    else:
        print('Incorrect entry, please enter a number only')
        menu()


menu()

import random
randomNumber = random.randrange(0,100)
print('''
The First Game is The Guessing Game, Then Rock Paper Scissors. Have Fun!!
Guess a Random Number Between 1 and 100. Good Luck!''')
guessed = False
while guessed==False:
    userInput = int(input("Your guess please: "))
    if userInput==randomNumber:
        guessed = True
        print("Good Job:) YOU WIN!")
    elif userInput>100:
        print("Our guess range is between 0 and 100, please try a bit lower")
    elif userInput<0:
        print("Our guess range is between 0 and 100, please try a bit higher")
    elif userInput>randomNumber:
        print("Try one more time, a bit lower")
    elif userInput < randomNumber:
        print("Try one more time, a bit higher")

print("The End")


def menuu():
    print('''
    -GAME MENU-
    
    1. Rock Paper Scissors

    (Press either 1, or 2)
    ''')
    choice=input(": ")
    if choice=='1':
        ('LOADING..... ')
    elif choice=='2':
        Random()
    else:
        print('Incorrect entry, please enter a number only')
        menuu()
        

menuu()

import random
def main():
    print("Let's play 'Rock, Paper, Scissors'!")
    number = user_guess()
    num = computer_number()
    results(num, number)

def computer_number():
    num = random.randrange(1,4)
    if num == 1:
        print("Computer chooses rock")
    elif num == 2:
        print("Computer chooses paper")
    elif num == 3:
        print("Computer chooses scissors")
    return num

def user_guess():
    guess = input("Choose 'rock', 'paper', or 'scissors' by typing that word. ")
    if is_valid_guess(guess):
        if guess == 'rock':
            number = 1
        elif guess == 'paper':
            number = 2
        elif guess == 'scissors':
            number = 3
        return number
    else:
        print('That response is invalid.')
        user_guess()

def is_valid_guess(guess):
    if guess == 'rock' or 'paper' or 'scissors':
        status = True
    else:
        status = False
    return status

def restart():
    answer = input("Would you like to play again? Enter 'y' for yes or \
    'n' for no: ")
    if answer == 'y':
        main()
    elif answer == 'n':
        menu()
    else:
        print("Please enter only 'y' or 'n'!")
        restart()

def results(num, number):
    difference = num - number
    if difference == 0:
        print("TIE!")
        restart()
    elif difference % 3 == 1:
        print("Oof, You lost:( That's tuff! ")
        restart()
    elif difference % 3 == 2:
        print("Congratulations! You won :)")
        restart()

main()

