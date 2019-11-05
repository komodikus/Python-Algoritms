class Cell:
    def __init__(self, x, y):
        self.coordinates = (x, y)

    def __hash__(self):
        return hash(self.coordinates)

    def __eq__(self, other):
        if isinstance(other, (Cell, Stone, Grass, Water)):
            return other == self.coordinates
        return other == self.coordinates


class Stone(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)


class Water(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)


class Grass(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)


if __name__ == '__main__':
    world = {Grass(1, 2), Stone(3, 4), Water(5, 3), Stone(2, 2), Cell(3, 4)}

    print(Cell(3, 4) in world)
    # print(Cell(4, 3) in world)
    # print(Water(3, 4) in world)
    # print(Cell(3, 5) in world)
    print((3, 4) in world)

    # assert Stone(1, 2) in world
    # assert Grass(3, 5) not in world
    # assert (3, 4) in world
    # assert (4, 3) not in world
