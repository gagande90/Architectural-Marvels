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
    def __init__(self):                         # TypeError: __init__() takes 1 positional argument but 3 were given
        pass


notre_dame = Cathedral('Cathedral', 'Notre-Dame de Paris')
notre_dame.info()














