# from single to multiple Inheritance

class Building():
    def __init__(self, walls, doors, windows):
        self.walls = walls
        self.doors = doors
        self.windows = windows
    
    def building_info(self):
        return self.walls, self.doors, self.windows
    
    def show_building(self):
        print('Walls: {}, doors: {}, Windows: {}'.\
              format(*self.building_info()))            # unpack tuple using star * syntax

class SpaceShip():
    def __init__(self, destination):
        self.destination = destination
        
    def show_spaceshhip(self):
        print('Flying:', self.destination)
          
                    
class Cathedral(Building, SpaceShip):
    def __init__(self, destination, walls=4, doors=1, windows=0):
        super().__init__(walls, doors, windows)                     # first super call uses first/left-hand inherited class
        SpaceShip.__init__(self, destination)                       # second init we name the parent class


notre = Cathedral(windows=1000, destination='Beyond Mars')
notre.show_building()
notre.show_spaceshhip()





