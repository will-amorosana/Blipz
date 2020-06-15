class Blip(object):

    def __init__(self, blip_name='A blip!', max_val=3, curr_val=3):
        self.name = blip_name
        self.max_value = int(max_val)
        self.curr_value = int(curr_val)

    def tick(self, up = False):
        if up:
            if self.curr_value < self.max_value:
                self.curr_value += 1
                return True
            return False
        else:
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

