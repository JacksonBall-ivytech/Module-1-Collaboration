food = []

food.append('Sushi')
food.insert(0, 'Fried Rice')
food += ['Cooked Salmon']
food.extend(['Bacon burger'])
food.append('Peperoni Pizza')

print(food)

food.sort()

print(food)

for i in food:
    print(f'I really like a good {i}.')