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
    def __init__(self, *args):                    # accept unknown number of positional arguments     
        super().__init__(*args)                   # forward positional arguments to base/super class


notre_dame = Cathedral('Cathedral', 'Notre-Dame de Paris')      # arguments passed in by position
notre_dame.info()













