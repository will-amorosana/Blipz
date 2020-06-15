from blip import Blip

class Block(object):
    def add_blip(self, name, maxval, currval):
        new_blip = Blip(name, maxval, currval)
        self.blips.append(new_blip)

    def tick(self, blip_name):
        for i in self.blips:
            if i.name == blip_name:
                return i.tick()
            else:
                return False

    def display(self):
        print('========================================')
        print('**'+self.name+'**')
        print('['+'|'*self.chp + ' '*(self.mhp-self.chp) + ']' + '|'*self.thp +
              (str(self.chp + self.thp)) + '/' + str(self.mhp) + ' HP')
        print(str(self.xp) + ' XP (Level ' + str(self.levelcalc(self.xp)) + ')')
        gold = int((self.cp ) /100)
        silver = int((self.cp % 100) / 10)
        copper = int(self.cp % 10)
        print(str(gold) + 'GP, ' + str(silver) + 'SP, ' + str(copper) + 'CP')
        for i in self.blips:
            print(i.textualize())
        print('=======================================')

    def longrest(self):
        for i in self.blips:
            i.fill()
        self.thp = 0
        self.chp = self.mhp

    def __init__(self, nm='Creed', new_mhp=32, new_chp = 32, new_thp=0, new_xp = 0, new_cp = 2135 ):
        self.name = nm
        print('Welcome, '+self.name)
        self.mhp = new_mhp
        self.chp = new_chp
        self.thp = new_thp
        self.xp = new_xp
        self.cp = new_cp

        self.blips = list()

    def levelcalc(self, xp):
        thresholds = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000,
                      64000, 85000, 100000, 120000, 140000, 165000,
                      195000, 225000, 265000, 305000, 355000]
        for x in thresholds:
            if xp < x:
                return thresholds.index(x)