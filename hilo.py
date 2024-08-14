# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 18:17:54 2022

@author: thehumbleking
"""

low = 1
high = 100

print("think of a number between {} and {}".format(low,high))
input("press ENTER to start")

guesses = 1
while True:
    guess = low + (high - low) // 2
    high_low = input("my guess is {}.Should i guess higher or lower?"
                     "ENTER h or l,or c if my guess was correct: "
                     .format(guess)).casefold()
    
    
    if high_low == "h":
        # Guess higher. Then low end of the range becomes 1 greater than the guess.
           low = guess + 1
    elif high_low == "l":
        #guess lower. The high end of the range becomes one less than the guess
         high = guess - 1 
    elif high_low == "c":
        print ("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h,l or c")
        
    guesses += 1
    
    