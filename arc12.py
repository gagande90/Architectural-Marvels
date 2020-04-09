# Inheritance: 'is-a' 
# Composition: 'has-a'

class Engine():
    def __init__(self, engine_type='[unknown]'):
        self.engine_type = engine_type


class Vehicle():
    def __init__(self, seats=1):
        self.number_of_seats = seats
    
class Airplane(Vehicle):                            # Airplane is-a Vehicle
    def __init__(self, model, engine, seats=1):
        super().__init__(seats)
        self.airplane_model = model
        self.airplane_engine = Engine(engine)       # Airplane has an Engine
        
        
    def airplane_info(self):
        print('{} with \n{} type of engine and \n{} passenger seats\n'.\
                format(self.airplane_model, 
                self.airplane_engine.engine_type,
                self.number_of_seats))



boing = Airplane(model='Boing 787 Dreamliner', 
                 engine='Rolls-Royce Trent 1000',
                 seats=300)

airbus = Airplane(model='Airbus A350', 
                       engine='Rolls-Royce Trent XWB',
                       seats=299)

for plane in (boing, airbus):
    plane.airplane_info()







