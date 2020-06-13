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
        plat = int(self.cp / 1000)
        gold = int((self.cp % 1000) /100)
        silver = int((self.cp % 100) / 10)
        copper = int(self.cp % 10)
        print(str(plat) + 'PP, '+str(gold) + 'GP, ' + str(silver) + 'SP, ' + str(copper) + 'CP')
        for i in self.blips:
            print(i.textualize() + '\n')
        print('=======================================')

    def longrest(self):
        for i in self.blips:
            i.fill()
        self.thp = 0
        self.chp = self.mhp

    def __init__(self, nm='Creed', max_hp=10, ):
        print('Welcome, '+self.name)
        self.mhp = max_hp
        self.chp = self.mhp
        self.thp = 0
        self.xp = 9055
        self.cp = 987654
        self.blips = list()

