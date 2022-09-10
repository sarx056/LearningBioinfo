# project 2
# creating a simple number guessing game
# its not that great btw


# import all the modules needed
import simplegui
import random

# create the variables
num_range = 100
remain_guess = 7


# create a function which initializes the game and selects the number
def new_game():
    global num_range
    global remain_guess
    print('New game: range 0 to 100!')
    print('remaining guesses', remain_guess)
    num_range = random.randint(0, 101)
    return num_range


# create a function to take guesses
def input_guess(guess):
    guess = int(guess)
    global num_range
    global remain_guess
    remain_guess -= 1
    print('your guess was', guess)
    print('remaining guesses', remain_guess)
    if remain_guess == 0 and guess != num_range:
        print('Oops out of guesses, try again!')
        print('the correct answer was ', num_range)
        new_game()
    elif guess > num_range:
        print('Lower!')
    elif guess < num_range:
        print('higher')
    elif guess == num_range:
        print('Correct!')


# create frame
frame = simplegui.create_frame('guess the number game', 200, 200)
frame.add_button('0 to 100', new_game, 100)
frame.add_input('type in your guess', input_guess, 100)

# start frame
frame.start()
