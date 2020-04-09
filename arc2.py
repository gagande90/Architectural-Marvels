class Cathedral():
    def build(self):
        print('building a cathedral...')
        
    def visit(self):
        print('Welcome to our Cathedral')


class Cafe():
    def build(self):
        print('building a cafe...')
    
    def visit(self):
        print('Welcome to our Cafe')
        

class Car():
    def build(self):
        print('building a car...')

    def visit(self):
        print("Welcome to our car")         #For fixing the error at line 27 
        
        
def create(building):                       
    building.build()
    building.visit()                        # AttributeError: 'Car' object has no attribute 'visit'


notre_dame = Cathedral()    
java_house = Cafe()
car = Car()

things = notre_dame, java_house, car

for the_thing in (things):
    create(the_thing)
    print()






