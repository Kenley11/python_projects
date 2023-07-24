#Step 5

import random
import hangman_words
import hangman_art

logo = hangman_art.logo
print(logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

attempted_guesses = []
doubles = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    attempted_guesses.append(guess)

    if attempted_guesses.count(guess) > 1:
        attempted_guesses.remove(guess)
        doubles.append(guess)
        print(f'You already guessed {guess}. Try again')
    print(f"So far you've attempted:     {doubles}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        #     f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
        # )
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        if guess not in chosen_word:
            print(f'{guess} is not in the word.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
