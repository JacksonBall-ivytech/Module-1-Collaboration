'''
Jackson Ball

GPA_qualifer.py

This app will have you enter your full name and your current gpa. We will then use this information to 
tell the user if they made it on the Dean's list or if they are in honor roll. These messages will be
printed on the console.
'''


import sys

# Get the last name and quit program if it's ZZZ
last_name = input('Please enter your last name: ')
if last_name == 'ZZZ':
    sys.exit()
first_name = input('Please enter your first name: ')

# Store the gpa as a float and redo input if not inputed as float
while True:
    try:
        gpa = float(input('Please enter your GPA: '))
    except ValueError:
        print('Wrong value. Try again :D')
    else:
        break

# Print statements for respective gpa requirements
if gpa >= 3.5:
    print(f"Great job {first_name.title()} {last_name.title()}! You made it to the Dean's list.")
if gpa >= 3.25:
    print(f"{first_name.title()} {last_name.title()}, you have made it to Honor Roll. Nicely done.")