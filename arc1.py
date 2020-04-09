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
        
            
def create(building):                   # works for any object that has those methods
    building.build()
    building.visit()

notre_dame = Cathedral()    
java_house = Cafe()

things = notre_dame, java_house         # tuple

for the_thing in (things):              # iterate over tuple
    create(the_thing)
    print()






