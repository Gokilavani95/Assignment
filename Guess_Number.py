print('******** Guess the Number ********')
print('******** variables and Condition statement ********')
import random
Random_numb = random.randint(1,10)
attempts = 0
player_guess = 8
if player_guess == Random_numb:
    print('Player guess is correct')
elif player_guess > Random_numb:
    print('Player guess is too high')
else:
    print('Player guess is too low')
    #Print the random number to check the player guess
print('Random number = '+str(Random_numb))

print()
print('******** Loop *******')
while True:
    guess = int(input('Guess the Number: '))
    if guess == Random_numb:
        print('Player guess is correct')
        break
    else:
        print('Player guess is wrong')
    attempts += 1


