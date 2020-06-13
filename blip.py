class Blip(object):

    def __init__(self, blip_name='A blip!', max_val=3, curr_val=3):
        self.name = blip_name
        self.max_value = int(max_val)
        self.curr_value = int(curr_val)

    def tick(self):
        if self.curr_value <= 0:
            return False
        else:
            self.curr_value -= 1
            return True

    def fill(self):
        self.curr_value = self.max_value

    def empty(self):
        self.curr_value= 0

    def expand(self):
        self.max_value += 1

    def textualize(self):
        return self.name + ': ' + '[X]'*self.curr_value + '[ ]'*(self.max_value - self.curr_value)

    def levelcalc(self, xp):
        thresholds = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000,
                      64000, 85000, 100000, 120000, 140000, 165000,
                      195000, 225000, 265000, 305000, 355000]
        for x in thresholds:
            if xp < x:
                return thresholds.index(x)