LOW_BOUND = 1 #bounds constants that represent the inclusive min and max values that the secret number could be
HIGH_BOUND = 100 #the program is completly responsive to changing these constants

low = LOW_BOUND #initialize the low and high end points to the bounds, since the first guess must consider the entire range
high = HIGH_BOUND

print('Please think of a number between {} and {}'.format(LOW_BOUND, HIGH_BOUND))

while True:
    guess = (low+high)//2 #guess the midpoint between the current low and high end points
    
    print('Is your secret number {}?'.format(guess)) #display the guess to the user
    answer = input("Enter 'h' if my guess is too high, 'l' if too low, or 'c' if I am correct: ") #prompt the user for feedback
    
    if answer == 'l': #if the computer guess was too low
        low = guess
    elif answer == 'h': #if the computer guess was too high
        high = guess
    elif answer == 'c': #if the computer guess was correct
        print('Game over, your secret number was: {}. Guessed in {} tries.'.format(guess))
        break #break out of while loop (only break case)
    else: #if the user feedback answer was not one of the 3 valid letters
        print("Please enter the letter 'l', 'h', or 'c'.") #display an error message 
        continue #continue to next iteration, keeping same low and high bounds
