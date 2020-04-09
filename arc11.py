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
        self.number_of_bells = 10

    def ring_bell(self, bell=1):                        # add a new method
        print('ringing bell number {}'.format(bell))
        
    def info(self):                                     # overwrite base class method
        super().info()                                  # call method in base class
        self.ring_bell()                                # add new method call
        

class Cafe(Building):
    pass


notre_dame = Cathedral(type_of='Cathedral', name='Notre-Dame de Paris')     
notre_dame.info()                                                           # calls derived class method
print() 
Cafe('Cafe', 'The Java House').info()                                       # calls base class method













