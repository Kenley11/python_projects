import random

intro_msg = ('Welcome to Higher or Lower! You have 5 attempts.\n')
print(intro_msg)

random_num = random.randint(1,100)
# print(random_num)

end_of_game = False
total_attempts_left = 5
guesses = 1
invalid_counter = 0

while not end_of_game and total_attempts_left > 0:
    try:
        user_guess = int(input('Guess a number:\n'))
    except ValueError:
        invalid_counter += 1
        print('Invalid input. Please enter a number.')
        if invalid_counter >= 2:
            total_attempts_left -= 1
        continue


    if user_guess not in range(1,101):
        print('You have to guess between 1 & 100. Try again!')
        invalid_counter += 1
        if invalid_counter >= 2:
            total_attempts_left -= 1
            print(f'You have to guess between 1 & 100. {total_attempts_left} attempts left!')
    elif user_guess == random_num and guesses == 1:
        print(f'Correct! It was {random_num}. It took {guesses} attempt.')
        end_of_game = True
    elif user_guess == random_num:
        print(f'Correct! It was {random_num}. It took {guesses} attempts.')
        end_of_game = True
    elif user_guess > random_num and total_attempts_left != 1:
        total_attempts_left -= 1
        guesses += 1
        print(f'Go lower. You have {total_attempts_left} attempts left.')
    elif user_guess < random_num and total_attempts_left != 1:
        total_attempts_left -= 1
        guesses += 1
        print(f'Go higher. You have {total_attempts_left} attempts left.')
    
    while total_attempts_left == 1 and not end_of_game:
        user_guess = int(input('Guess a number:\n'))

        if user_guess == random_num:
            print(f'Correct! It was {random_num}. It took {guesses} attempts.')
            end_of_game = True
        elif user_guess > random_num:
            total_attempts_left -= 1
            guesses += 1
        elif user_guess < random_num:
            total_attempts_left -= 1
            guesses += 1
        if total_attempts_left == 0 and user_guess != random_num:
            print(f'Game Over. The number was {random_num}.')
            end_of_game = True
    
    