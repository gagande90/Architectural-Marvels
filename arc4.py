class ThingToBuild():
    def build(self): 
        raise NotImplementedError('All subclasses have to implement this method')
    
    def visit(self): 
        raise NotImplementedError('All subclasses have to implement this method')


class Cathedral(ThingToBuild):
    def build(self):
        print('building a cathedral...')
        
    def visit(self):
        print('Welcome to our Cathedral')


class Cafe(ThingToBuild):
    def build(self):
        print('building a cafe...')
    
    def visit(self):
        print('Welcome to our Cafe')
        

class Car(ThingToBuild):
    def build(self):
        print('building a car...')
        
        
def create(building):                       
    building.build()
    building.visit()                        # NotImplementedError: All subclasses have to implement this method


notre_dame = Cathedral()    
java_house = Cafe()
car = Car()

things = notre_dame, java_house, car

for the_thing in (things):
    create(the_thing)
    print()






