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
    def __init__(self, walls, doors, windows):
        self.walls = walls
        self.doors = doors
        self.windows = windows
    
    def building_info(self):
        return self.walls, self.doors, self.windows
    
    def show_building(self):
        print('Walls: {}, doors: {}, Windows: {}'.\
              format(*self.building_info()))            # unpack tuple using star * syntax


class TheGods():
    def __init__(self, gods=10):
        self.number_of_gods = gods
        
    def show_statues(self):
        return self.number_of_gods   


class Temple(Building, TheGods):                
    def __init__(self, walls=4, doors=1, windows=0, gods=10):
        super().__init__(walls, doors, windows)
        TheGods.__init__(self, gods)

    def __str__(self):                                                  # implement string representation of class
        return "Temple floor plan view: {} Temple front view: {}".\
            format(EUSTYLE_TEMPLE_FLOORPLAN, EUSTYLE_TEMPLE_FRONTVIEW)


eustyle = Temple()
print(eustyle)
eustyle.show_building()
print("This Temple has {} Gods: ".format(eustyle.show_statues()))














