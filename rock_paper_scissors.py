import random

emojis = {'r':'🪨','s':'✂️','p':'📄'}
choices = ('r','p','s')

def get_user_choice():
    while True:
        user_choice= input('Rock, paper,or scissors? (r/p/s):').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('invalid choice')
        
def display_choices(user_choice, comp_choice):    
        print(f'You chose {emojis[user_choice]}')
        print(f'Computer chose {emojis[comp_choice]}')
        
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        print('tie')
    elif (
        (user_choice =='r' and comp_choice == 's') or
        (user_choice =='s' and comp_choice == 'p') or
        (user_choice =='p' and comp_choice == 'r')):
        print('you win')
    else:
        print (' you lose')
        
def play_game():
    while True:
        user_choice = get_user_choice()
    
        comp_choice = random.choice(choices)

        display_choices(user_choice, comp_choice)
    
        determine_winner(user_choice, comp_choice)
    
        should_continue = input('Continue? (y/n):').lower()
        if should_continue == 'n':
          break
play_game()

    
