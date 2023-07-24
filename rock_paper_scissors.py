import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper =  '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_play = int(input('Please choose - | 0: Rock | 1: Paper | 2: Scissors\n'))
cpu_play = random.randint(0,2)

if cpu_play == 0:
    print(rock)
    if user_play == 0:
        print(rock)
        print('It is a draw')
    elif user_play == 1:
        print(paper)
        print('You win!')
    else:
        print(scissors)
        print('You lose!')
elif cpu_play == 1:
    print(paper)
    if user_play == 0:
        print(rock)
        print('You lose!')
    elif user_play == 1:
        print(paper)
        print('It is a draw!')
    else:
        print(scissors)
        print('You win!')
else:
    print(scissors)
    if user_play == 0:
        print(rock)
        print('You win!')
    elif user_play == 1:
        print(paper)
        print('You lose!')
    else:
        print(scissors)
        print('It is a draw!')