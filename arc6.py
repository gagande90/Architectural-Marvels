class ThingToBuild():
    def __init__(self, name_of_thing='[unknown]'):
        self.name_of_thing= name_of_thing
        
    def build(self): 
        raise NotImplementedError('All subclasses have to implement this method')
    
    def visit(self): 
        print('This thing cannot be visited')


class Cathedral(ThingToBuild):
    def build(self):
        print('building a cathedral...')
        
    def visit(self):
        print('Welcome to {}'.format(self.name_of_thing))


class Cafe(ThingToBuild):
    def build(self):
        print('building a cafe...')
    
    def visit(self):
        print('Welcome to {}'.format(self.name_of_thing))
        

class Car(ThingToBuild):
    def build(self):
        print('building a car...')
        
        
def create(building):                       
    building.build()
    building.visit()                        # no more error for Car object


notre_dame = Cathedral('"Notre-Dame de Paris"')    
java_house = Cafe('"The Java House"')
car = Car()

things = notre_dame, java_house, car

for the_thing in (things):
    create(the_thing)
    print()






