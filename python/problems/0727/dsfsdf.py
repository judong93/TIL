class Doggy:
    birth_of_dogs = 0
    num_of_dogs = 0
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Doggy.birth_of_dogs += 1
        Doggy.num_of_dogs += 1
        
    def __del__(self):
        Doggy.num_of_dogs -= 1
        
    def bark(self):
        return "왈왈!"
    
    @classmethod
    def get_status(cls):
        return f"Birth: {cls.birth_of_dogs}, Current: {cls.num_of_dogs}"

d1 = Doggy('초코', '푸들')
d2 = Doggy('꽁이', '말티즈')
d3 = Doggy('별이', '시츄')

print(d1.bark())
print(Doggy.get_status())