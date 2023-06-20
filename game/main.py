import random

options = ('piedra', 'papel', 'tijera')

def get_user_option():
    user_option = input('piedra, papel o tijera => ').lower()
    while user_option not in options:
        print('esa opcion no es valida')
        user_option = input('piedra, papel o tijera => ').lower()
    return user_option

def get_computer_option():
    return random.choice(options)

def determine_winner(user_option, computer_option):
    if user_option == computer_option:
        return None
    elif (user_option == 'piedra' and computer_option == 'tijera') or (user_option == 'papel' and computer_option == 'piedra') or (user_option == 'tijera' and computer_option == 'papel'):
        return 'user'
    else:
        return 'computer'

def print_round_results(user_option, computer_option, winner):
    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    if winner == 'user':
        print(f'{user_option} gana a {computer_option}')
        print('user gano!')
    elif winner == 'computer':
        print(f'{computer_option} gana a {user_option}')
        print('computer gano!')
    else:
        print('Empate!')

def play_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_wins', computer_wins)
        print('user_wins', user_wins)

        user_option = get_user_option()
        computer_option = get_computer_option()
        winner = determine_winner(user_option, computer_option)
        
        print_round_results(user_option, computer_option, winner)
        
        if winner == 'user':
            user_wins += 1
        elif winner == 'computer':
            computer_wins += 1

        rounds += 1

        if computer_wins == 2:
            print('El ganador es la computadora')
            break

        if user_wins == 2:
            print('El ganador es el usuario')
            break

play_game()
