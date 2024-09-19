class Person:
    def __init__(self, first_name, last_name, age, job, hair_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.job = job
        self.hair = hair_color
    
    def print_description(self):
        print(f'Full name - {self.first_name} {self.last_name}')
        print(f'Age - {self.age}')
        print(f'Hair color - {self.hair}')
        print(f'Occupation - {self.job}')
    
    def age_check(self):
        if self.age > 21:
            print('You are over 21 years of age\n')
        elif self.age < 21:
            print('You are under 21 years of age\n')
        else:
            print('You are exactly 21 years of age\n')
    
jackson = Person('Jackson', 'Ball', 17, 'Student', 'Dark brown')
jackson.print_description()
jackson.age_check()

mother = Person('Marcy', 'Ball', 48, 'Acedemic advisor', 'Dark brown')
mother.print_description()
mother.age_check()

rando = Person('Gerold', 'Humflet', 21, 'Toothbrush engineer', 'Purple')
rando.print_description()
rando.age_check()