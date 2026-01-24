import random
print('******** String Manipulation ******** ')
Words = ['python','javascript','java','automation','pytest','guvi','selenium']
scrambled_words = "".join(random.sample(Words, len(Words)))
print(scrambled_words)
print()


print('******** Condition check of random words ******** ')
random_word = random.choice(Words)
Player_guess = input('Guess the word: ')
if Player_guess == random_word:
    print('Guess is Correct')
    print('Random word is ' +random_word)
else:
    print('Guess is Wrong')
    print('Random word is ' +random_word)
print()


print('******** Loop scenario ******** ')
attempts = 0
while True:
    Guess_word = input('Guess the word: ')
    if Guess_word == random_word:
        print('Guess is Correct')
        print('Random word is ' +random_word)
        break
    else:
        print('Guess is Wrong. Try again!')
    attempts += 1