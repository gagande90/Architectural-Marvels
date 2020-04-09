EUSTYLE_TEMPLE_FLOORPLAN = """\

╔═════════════════════╗
║╔═══════════════════╗║
║║╔═════════════════╗║║
║║║╔═══════════════╗║║║
║║║║╔═════════════╗║║║║
║║║║║▀ ▀ ▀   ▀ ▀ ▀║║║║║
║║║║║▀ ▀ ▀   ▀ ▀ ▀║║║║║
║║║║║▀ ▌────────▌▀║║║║║ 
║║║║║▀ ▌        ▌▀║║║║║
║║║║║▀ ▌        ▌▀║║║║║
║║║║║▀ ▌───  ───▌▀║║║║║
║║║║║▄ ▌   ──   ▌▄║║║║║
║║║║║▄ ▌        ▌▄║║║║║
║║║║║▄ ▌        ▌▄║║║║║
║║║║║▄ ▄─▄───▄─▄ ▄║║║║║
║║║║║▄ ▄ ▄   ▄ ▄ ▄║║║║║
║║║║╚═════════════╝║║║║
║║║╚═══════════════╝║║║
║║╚═════════════════╝║║
║╚═══════════════════╝║
╚═════════════════════╝

"""

EUSTYLE_TEMPLE_FRONTVIEW = """\
              
             __۩__
          ___    ___
      ____          ____
       ༼___                   ___༽
    ䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀
  ┃                        ┃
    ䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀ 
   ╰ ╯ ╰ ╯ ╰ ╯  ╰ ╯ ╰ ╯ ╰ ╯
              ▏   ▏          ▏   ▏          ▏   ▏             ▏    ▏         ▏   ▏          ▏   ▏   
              ▏   ▏          ▏   ▏          ▏   ▏             ▏    ▏         ▏   ▏          ▏   ▏   
              ▏   ▏          ▏   ▏          ▏   ▏ ▁▁▁▏    ▏         ▏   ▏          ▏   ▏  
              ▏   ▏          ▏   ▏          ▏   ▏ ║      ║  ▏   ▏         ▏   ▏          ▏   ▏    
              ▏   ▏          ▏   ▏          ▏   ▏ ║      ║  ▏   ▏         ▏   ▏          ▏   ▏   
              ▏   ▏          ▏   ▏          ▏   ▏ ║      ║  ▏   ▏         ▏   ▏          ▏   ▏   
              ▏   ▏          ▏   ▏          ▏   ▏ ║      ║  ▏   ▏         ▏   ▏          ▏   ▏      
   ╭ ╮ ╭ ╮ ╭ ╮  ╭ ╮ ╭ ╮ ╭ ╮  
          ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
    ䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀
  ䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀
䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀

"""

class Building():
    def __init__(self, walls, doors, windows):          # a building "has" walls and doors
        self.walls = walls
        self.doors = doors
        self.windows = windows
    
    def building_info(self):
        return self.walls, self.doors, self.windows
    
    def show_building(self):
        print('Walls: {}, doors: {}, Windows: {}'.\
              format(*self.building_info()))            # unpack tuple using star * syntax


class Place():
    def __init__(self, lassitude=0, attitude=1):
        self.ns = lassitude
        self.we = attitude                              # (pun intended)
    
    def located_at(self):
        return self.ns, self.we

    
class TheGods():
    def __init__(self, gods=10):
        self.number_of_gods = gods
        
    def show_statues(self):
        return self.number_of_gods   


class Temple(Building, Place):                                 # a Temple "is-a" building and also a Place on Earth
    def __init__(self, walls=4, doors=1, windows=0):
        super().__init__(walls, doors, windows)
        Place.__init__(self, lassitude='34.0060 N', attitude='36.2039 E')
        self.gods = TheGods(gods=10)                                    # Temple "has" gods
        self.dancing_girls = 100
        self.gallons_of_wine = 10000

    def party_at_the_temple(self):
        print('Dancing with {} goddesses drinking {} gallons of wine...'.\
              format(self.dancing_girls, self.gallons_of_wine))
        print('This Temple is dedicated to Bacchus...')

    def __str__(self):                                                              # string representation of class
        return "Temple floor plan view: {} Temple front view: {}".\
            format(EUSTYLE_TEMPLE_FLOORPLAN, EUSTYLE_TEMPLE_FRONTVIEW)


if __name__ == '__main__':
    eustyle = Temple()
    print(eustyle)
    eustyle.show_building()
    print("This Temple has {} Gods: ".\
          format(eustyle.gods.show_statues()))
    eustyle.party_at_the_temple()
    print("Our Temple is located at: {}, {}".\
          format(*eustyle.located_at()))
















