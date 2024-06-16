import random 

player_choice = input('Enter a choice ( rock, paper, scissors ): ').lower()

possible_actions = ['rock', 'paper', 'scissors']
computer_choice = random.choice(possible_actions)

print(f'Your choice is {player_choice}, computers choice is {computer_choice}')

if player_choice == computer_choice :
    print("You both chose the same thing... It's a tie!")
elif player_choice == 'rock':
    if computer_choice == 'paper':
        print('Paper beats rock... Computer wins!')
    elif computer_choice == 'scissors':
        print('Rock beats scissors... You win!')
elif player_choice == 'paper':
    if computer_choice == 'rock':
        print('Paper beats rock... You win!')
    elif computer_choice == 'scissors':
        print('Scissors beats paper... Computer wins!')
elif player_choice == 'scissors':
    if computer_choice == 'paper':
        print('Scissors beats paper... You win!')
    elif computer_choice == 'rock':
        print('Rock beats scissors... Computer wins!')
    
