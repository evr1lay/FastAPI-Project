class Human:
    name = None
    age = None
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
new_human = Human("evr1lay", 14)
print(new_human.name)