# single inheritance

class Building():
    def __init__(self, type_of, name):
        self.type_of_building = type_of
        self.name_of_building = name

    def build(self):
        print('building a {}...'.format(self.type_of_building))
        
    def visit(self):
        print('Welcome to {}'.format(self.name_of_building))

    def info(self):
        return self.build(), self.visit()
        

class Cathedral(Building):
    pass

class Cafe(Building):
    pass


notre_dame = Cathedral('Cathedral', 'Notre-Dame de Paris')
notre_dame.info()
print()
Cafe('Cafe', 'The Java House').info()





















