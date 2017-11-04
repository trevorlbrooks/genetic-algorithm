import random
import math
class Gene:
    is_normalized = True
    def __init__(self):
        self.start = 0
        self.size = 0
        self.length = 0
        self.decimal_divider = 0
    
    def randomize(self, is_normalized):
        if is_normalized:
            return (str(bin(random.randrange(0, self.size)))[2:]).zfill(self.length)
    def set(self, start, size):
        self.start = start
        self.size = size
        self.length = math.ceil(math.log(size, 2))
        return self.length
    def __str__(self):
        return 'Start: '+ str(self.start) + ' Size: ' + str(self.size) + ' Length: ' + str(self.length)
