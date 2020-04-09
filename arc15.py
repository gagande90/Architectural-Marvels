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
              format(*self.building_info()))            # unpack tuple using star * syntax
    
    
class Cathedral(Building):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

notre = Cathedral(windows=1000)
notre.show_building()


















