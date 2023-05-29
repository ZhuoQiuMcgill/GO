class StoneSet:
    def __init__(self, x, y, parent, rank):
        self.x = x
        self.y = y
        self.parent = None
        self.rank = 0

def find(stone_set):
    if stone_set.parent is None:
        return 
