# from single to multiple Inheritance

class Building():
    def __init__(self, walls=4, doors=1, windows=0):
        self.walls = walls
        self.doors = doors
        self.windows = windows
    
    def building_info(self):
        return self.walls, self.doors, self.windows
    
    def show_building(self):
        print('Walls: {}, doors: {}, Windows: {}'.\
              format(*self.building_info()))            # unpack tuple using * syntax
    
    
class Cathedral(Building):
    def __init__(self):
        super().__init__()
        

notre = Cathedral()
notre.show_building()


















