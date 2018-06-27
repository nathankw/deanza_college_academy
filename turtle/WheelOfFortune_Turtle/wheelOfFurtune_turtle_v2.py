#!/usr/bin/env python3    
    
###    
# Nathaniel Watson    
# 2018-06-22   
# De Anza College Academy    
### 

"""
A variant of Wheel of Fortune. This is a single player game.
"""

import random
import time
import turtle as t

FONT_SIZE = 60
FONT = ("Arial", FONT_SIZE, "normal")

t.hideturtle()
t.bgcolor("blue")
t.penup()
t.pencolor("white")
# Turn animation off. Normally, each change triggers an update. But we only
# need a single update to display the drawing in one go. 
t.tracer(0)

possible_words = [
    "zebra",
    "tiger",
    "dolphin",
    "panda",
    "elephant",
    "kangaroo",
    "rabbit",
    "skunk",
    "rhino",
    "hippopotamus",
    "snake",
    "squirrel",
    "duckling",
    "goat",
    "hamster",
    "badger",
    "beaver",
    "walrus",
    "eel",
    "salmon",
    "lobster",
    "shrimp",
]

def start_game():
    random.shuffle(possible_words)
    puzzle = random.choice(possible_words)
    display = ["_"] * len(puzzle)
    wrong_letters = []

    def update_puzzle():
        # Clear the drawing and show the updated puzzle
        t.clear()
        t.write(" ".join(display), align="center", font=FONT)
        t.goto(-(t.window_width()/3), t.window_height()/3)
        t.write("Wrong letters: " + "".join(wrong_letters), align="left", font=FONT_SIZE/2)
        t.home()
        t.update() # Show changes. Required since the tracer is off (see t.tracer above).
        
    update_puzzle()

    turns = -1
    wrong_guesses_limit = 8
    wrong_guesses = 0
    while True:
        turns += 1
        print("Wrong guesses remaining: {}.".format(wrong_guesses_limit - wrong_guesses))
        win_message = "Congratulations! You finished solving the puzzle in {} turns".format(turns)
        user_letter = input("Choose a letter, or type the word to solve: ")
        user_letter = user_letter.lower()
        
        if len(user_letter) > 1:
          # User is trying to solve. Either the user wins or looses here. 
            if user_letter == puzzle:
                display = puzzle
                update_puzzle()
                print(win_message)
            else:
                print("You loose :<( The word was {}.".format(puzzle))
            break
            
        elif user_letter not in puzzle:
            wrong_guesses += 1
            if user_letter in wrong_letters:
                print("You already entered {}.".format(user_letter))
            else:
                print("Try again.")
                wrong_letters.append(user_letter)
            if wrong_guesses > wrong_guesses_limit:
                print("You loose :<(  Too many wrong guesses. The word was {}.".format(puzzle))
                break
        else:
            # The user letter is in the puzzle. Update the puzzle to show the user letter
            # in all places that it should appear:
            for index in range(len(puzzle)):
                letter = puzzle[index]
                if letter == user_letter:
                    display[index] = letter
        
        update_puzzle()
        
        # Check if all letters have been identified
        if "_" not in display:
            # Then all the letters have been found. Game over!
            print(win_message)
            break
    
    time.sleep(2)

while True:
    start_game()
    play = input("Play again? Hit enter twice to quit.")
    if not play:
        break
    
# 1. Before the game starts, print out a welcome message introducing the user to 
#    the game. 
#
# 2. The turtle is in the way in the puzzle. Hide the turtle so that just the
#    puzzle is visible. 
#
# 3. Change the background color of the drawing area to the color of your choosing.
#
# 4. Change the color of the letters in the puzzle. 
#
# 5. Update the last print statement so that it prints the number of turns instead
#    of the placeholder of "?". Keep track of the number of turns in a new variable
#    called "turns". 
#
# 6. Add a feature that allows the user to solve the puzzle. 
#    Hint: change the input line to be 
#
#        user_letter = input("Choose a letter, or type the puzzle to solve: ")
#
#    Next, you need to add a check to see if the user entered a single letter, 
#    or more than one letter (a word). If a word was entered, then check if that 
#    word equals the game puzzle's word. If they match, then congratulate the 
#    user and end the game. 
#
# 7. Currently, the puzzle is the same word every time the game is played. 
#    We need to make it so that a random word is chosen. Store a list of several
#    possible words, and pick one at random to be the puzzle's word each time the
#    game is played. Hint: import the random module and use functions found there
#    to pick a random word from a list of words.
# 
# 8. Limit the number of wrong guesses a user can make. If the user makes more
#    wrong guesses than this limit, end the game. Each turn should tell the user
#    how many wrong guesses they have left. 
#
# 9. Add a feature to keep track of all the guessed letters. If the user guesses
#    the same letter again, then notify the user that they need to choose a 
#    different letter. 
#
# 10. Improving on the previous step, show all the wrong letters the user has guessed on
#     the drawing area in addition to the puzzle word. You should place the wrongly guessed
#     letters out of the way of the puzzle, such as the top-left or top-right 
#     corner of the drawing area.
#
# 11. When playing the game, you should notice that the drawing area flickers 
#     with multiple updates happening (the puzzle word updates, the string of 
#     wrong letters updates). Rather than having the screen update every time we
#     draw something, make it so that the screen updates a single time after all screen
#     changes have been made. Hint: You'll need to use the turtle.tracer() and 
#     turtle.update() methods. 
#
# 12. Instead of ending the game and closing the window, ask the user if they want
#     to play again. Add support to restart the game if the user indicates yes. 
#
# 13. Update the game to allow for multi-word puzzles.

 
