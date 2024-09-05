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
# Welcome message with UI elements
print('''
╔═════════════════════════════╗
║       _      _       ___    ║
║    _ | |    /_\     | _ )   ║
║   | || |   / _ \ _  | _ \   ║
║    \__(_) /_/ \_(_) |___/   ║
║             ATM             ║
║─────────────────────────────║
║     Press ENTER to start    ║
╚═════════════════════════════╝
''')
start = input('')

print('Processing request', end='')
# Add a dot animation effect
time.sleep(0.8)
print('.', end='')
time.sleep(0.8)
print('.', end='')
time.sleep(0.8)
print('.')
print("Welcome to \033[1mJ\033[0mackson's \033[1mA\033[0mmazing \033[1mB\033[0mank ATM!")
# Get some "varification from user"
first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
middle_initial = input('Please enter your middle initial: ')
user_info = [first_name,  middle_initial, last_name]
print('(Type EXIT to end your session)\n')
# Var to log all the actions they did in the session
log = []
# Keep reapeating until they type EXIT
while True:
    print(f'Hello, {first_name}! Would you like to check your balance (C), make a deposit (D), or withdraw money (W)?')
    action = input('  ─ ')
    # Check if they ended the session
    if action.lower() == 'exit':
        break
    # Check balance
    if action.lower() in ['c', 'check']:
        animation('CHECK YOUR BALANCE')
        print('Enter the account you want to check: SAVINGS (s) or CHECKING (c)?')
        account = input('  ─ ')
        if account.lower() in ['savings', 's', 'saving']:
            print(f'''
            {first_name} {middle_initial}
            {last_name}
                            ╔═══════════════════════╗
                            ║   Account - SAVINGS   ║
                            ╠───────────────────────╣''')
            print('                            ║' + f'${savings:,}'.center(23) + '║')
            print('                            ╚═══════════════════════╝')
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
        else:
            print('INVALID ACCOUNT. Make sure you spelled it right. :D')
    # Withdraw money
    elif action in ['withdraw', 'w']:
        animation('WITHDRAW MONEY')
        print('Which account would you like to withdraw from: SAVINGS (s) or CHECKING (c)?')
        account = input('  ─ ')
        try:
            print('Enter the amount you want to withdraw')
            withdraw = float(input('  ─ '))
        except ValueError:
            print('ERROR: INCORRECT VALUE. Please try to type in a number :D')
            withdraw = 0
        if account.lower() in ['savings', 'saving', 's']:
            if withdraw <= savings:
                savings -= withdraw
            else:
                print('Oops. You entered a value that is greater than your savings. Try again :D')
        elif account.lower() in ['c', 'checking']:
            if withdraw <= savings:
                checking -= withdraw
            else:
                print('Oops. You entered a value that is greater than your checking. Try again :D')
        else:
            print('INVALID ACCOUNT. Make sure you spelled it right. :D')
print('Thanks for your service. Have a great day! :D')
