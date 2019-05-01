LOW_BOUND = 1 #bounds constants that represent the inclusive min and max values that the secret number could be
HIGH_BOUND = 100 #the program is completly responsive to changing these constants

low = LOW_BOUND #initialize the low and high end points to the bounds, since the first guess must consider the entire range
high = HIGH_BOUND
tries = 1 #the number of tries before the computer guesses the secret number

print('Please think of a number between {} and {}'.format(LOW_BOUND, HIGH_BOUND))

while True:
    guess = (low+high)//2 #guess the midpoint between the current low and high end points
    
    print('Is your secret number {}?'.format(guess)) #display the guess to the user
    answer = input("Enter 'h' if my guess is too high, 'l' if too low, or 'c' if I am correct: ").strip().lower() #prompt the user for feedback. strip whitespace, make lowercase

    #first validation, needs to be first since this case is more specific than the second validation, but this case will also be caught by second validation
    if (guess == HIGH_BOUND) and (answer == 'l'): #if the current guess is the high bound, and yet the user still inputs that the guess is too low
        print('Impossible, the secret number cannot be higher than {}.'.format(HIGH_BOUND)) #display an error message
        break
    if (guess == LOW_BOUND) and (answer == 'h'): #if the current guess is the low bound, and yet the user still inputs that the guess is too high
        print('Impossible, the secret number cannot be lower than {}.'.format(LOW_BOUND)) #diplay an error message
        break

    #second validation
    if low > high: #if the low end point was increased to be greater than the high end point, or the high end point was decreased to be lesser than the low end point
        if answer == 'l':
            print('Impossible, the secret number cannot simultaneously be lower than {} yet higher than {}.'.format(high+1, guess))
        if answer == 'h':
            print('Impossible, the secret number cannot simultaneously be higher than {} yet lower than {}.'.format(low-1, guess))
        break
    
    if answer == 'l': #if the computer guess was too low
        low = guess + 1
    elif answer == 'h': #if the computer guess was too high
        high = guess - 1
    elif answer == 'c': #if the computer guess was correct
        print('Game over, your secret number was: {}. Guessed in {} tries.'.format(guess, tries))
        break #break out of while loop (only break case)
    else: #if the user feedback answer was not one of the 3 valid letters
        print("Please enter the letter 'l', 'h', or 'c'.") #display an error message 
        continue #continue to next iteration, keeping same low and high bounds, and not incrementing the tries counter
    
    tries += 1 #increment the number of tries (this line of code only runs if (answer == 'l') or (answer == 'h'))
