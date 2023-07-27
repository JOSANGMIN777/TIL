class person:
    blood_color = 'green'
    name = 'python'
    
    def __init__(self, name):
        self.name = name

    
    def singing(self):
        return f'{self.name}가 노래합니다.'
    

person1 = person('jo')

print(person.name)
print(person1.singing())
print(person1.blood_color)

          