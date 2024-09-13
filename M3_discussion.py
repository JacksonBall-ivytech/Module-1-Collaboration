class User:
    def __init__(self, first_name, last_name, middle_initial, age, username, color, pets, gender, crayon):
        self.frist = first_name
        self.last = last_name
        self.middle = middle_initial
        self.age = age
        self.username = username
        self.color = color
        self.pets = pets
        self.gender = gender
        self.crayon = crayon
    
    def describe_user(self):
        print(f'Full name - {self.frist} {self.middle}. {self.last}')
        print(f'  • Username: {self.username}')
        print(f'  • Age: {self.age}')
        print(f'  • Gender: {self.gender}')
        print(f'  • Favorite color: {self.color}')
        print(f'  • # of pets: {self.pets}')
        print(f'  • Favorite crayon to eat: {self.crayon}')
    
    def greet_user(self):
        print(f'Greetings {self.frist}!\n')

jackson = User('Jackson', 'Ball', 'L', 17, 'SpeedyBanan', 'Yellow', 2, 'Male', 'Deep blue')
jackson.describe_user()
jackson.greet_user()

luis = User('Luis', 'Velasques-Ramirez', 'F', 17, 'LuisTheSup', 'Baby Blue', 1, 'Male', 'Red')
luis.describe_user()
luis.greet_user()

aung = User('Aung', 'Aung', 'A', 17, 'bommy101', 'Yellow', 0, 'Femboy', 'Black')
aung.describe_user()
aung.greet_user()

obeth = User('Obeth', 'Cruz', 'S', 17, '05sigma', 'Orange', 3, 'Male', 'Coal')
obeth.describe_user()
obeth.greet_user()

logan = User('Logan', 'Ghast', 'M', 17, 'E3GHast5', 'Black', 8, 'Female', 'Purple')
logan.describe_user()
logan.greet_user()
