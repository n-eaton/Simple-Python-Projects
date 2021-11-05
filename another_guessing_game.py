import sys
def lets_begin():
    start_a_game = input('Would you like play a game? y/n ').lower()
    if start_a_game == 'y':
        print("Let's begin! Guess a country!")
    elif start_a_game == 'n':
        print("Sorry to see you go :(")
        sys.exit()



lets_begin()

end_of_the_game = False
countries = ['nepal', 'peru', 'india', 'spain', 'germany', 'argentina', 'morocco', 'colombia', 'kazakhstan', 'cambodia']

import random

lives = 7
word = random.choice(countries)
word_length = len(word)

display = []
for _ in range(word_length):
    display += '_'

while not end_of_the_game:
    guess_input = input("Please enter a letter: ").lower()

    for place in range(word_length):
        letter = word[place]

        if letter == guess_input:
            display[place] = letter

    if guess_input not in word:
        lives -= 1
        print(f'Oops life is gone! you have: {lives} lives left ')

        if lives == 0:
            end_of_the_game == True
            print("You lost. Please try again")
            print("The word was", word, "!")
            sys.exit()
        else:
            end_of_the_game == False


    print(f" {' '.join(display)}")

    if "_" not in display:
        print('Congratulations! You won!')
        sys.exit()