import time

def animation(action):
    print(f'You selected {action}')
    print('Processing request', end='')
    # Add a dot animation effect
    time.sleep(0.8)
    print('.', end='')
    time.sleep(0.8)
    print('.', end='')
    time.sleep(0.8)
    print('.')


# Start with the inital amount for both checking and savings
savings = 1000
checking = 800
# Get some "varification from user"
first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
middle_initial = input('Please enter your middle initial: ')
user_info = [first_name,  middle_initial, last_name]
# Keep reapeating until they type EXIT
while True:
    print(f'Hello, {first_name}! Would you like to check your balance (C), make a deposit (D), or withdraw money (W)?')
    action = input('  ─ ')
    # Check balance
    if action.lower() in ['c', 'check']:
        animation('CHECK YOUR BALANCE')
        print('Enter the account you want to check: SAVINGS (s) or CHECKING (c)?')
        account = input('  ─ ')
        if account.lower() in ['savings', 's', 'saving']:
            print(f'SAVINGS CURRENT BALANCE - ${savings:,}')
        elif account.lower() in ['checking', 'c']:
            print(f'CHECKING CURRENT BALANCE - ${checking:,}')
        elif account.lower() in ['both', 'b', 'checking and savings']:
            print('Oh yeah! I forgot about both. Here ya go:')
            print(f'SAVINGS CURRENT BALANCE - ${savings:,}')
            print(f'CHECKING CURRENT BALANCE - ${checking:,}')
        else:
            print('INVALID ACCOUNT. Make sure you spelled it right. :D')
    # Deposit money
    elif action.lower() in ['deposit', 'd']:
        animation('MAKE A DEPOSIT')
        print('Which account would you like to deposit to: SAVINGS (s) or CHECKING (c)?')
        account = input('  ─ ')
        try:
            print('Enter the amount you want to deposit')
            deposit = float(input('  ─ '))
        except ValueError:
            print('ERROR: INCORRECT VALUE. Please try to type in a number :D')
            deposit = 0
        if account.lower() in ['savings', 'saving', 's']:
            savings += deposit
        elif account.lower() in ['c', 'checking']:
            checking += deposit
    # Withdraw money
    elif action in ['withdraw', 'w']:
        pass