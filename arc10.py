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
    def __init__(self, **kwargs):                    # accept unknown number of keyword arguments     
        super().__init__(**kwargs)                   # forward keyword arguments to base/super class


notre_dame = Cathedral(type_of='Cathedral', name='Notre-Dame de Paris')     # have to use keywords now
notre_dame.info()












