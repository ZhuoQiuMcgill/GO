class StoneSet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.parent = None
        # self.rank = 0
        self.adjacent = []


# def find(stone_set):
#     if stone_set.parent is None:
#         return stone_set
#     else:
#         return find(stone_set.parent)

def union(set1, set2):
    set1.adjacent.append(set2)
    set2.adjacent.append(set1)

