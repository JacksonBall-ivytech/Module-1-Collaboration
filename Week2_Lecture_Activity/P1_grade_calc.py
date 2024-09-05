grade = input('Please input your grade: ')

if int(grade) >= 90:
    print('You got an A!!!')
elif int(grade) >= 80:
    print('You got a B!')
elif int(grade) >= 70:
    print('You got a C!')
elif int(grade) >= 60:
    print('You got a D.')
else:
    print('Oh no. You got a F :(')
