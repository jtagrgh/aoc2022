from itertools import cycle

class Sim:
    y_top = 0
    jet_seq = []
    grid = [[] for _ in range(7)]
    rocks_fallen = 0

class Rock:
    def __init__(self, sim):
        self.sim = sim

    def set(self):
        self.position = [[x+2,y] for x,y in self.shape]
        self.sim.y_top += 3 + self.height
        for col in sim.grid:
            for _ in range(3 + self.height):
                col.insert(0, '.')

    def move_right(self):
        if any(x + 1 == len(sim.grid) or sim.grid[x+1][y] == "#" for x,y in self.position):
            return
        else:
            for i, (x,y) in enumerate(self.position):
                self.position[i][0] += 1

    def move_left(self):
        if any(x == 0 or sim.grid[x-1][y] == '#' for x,y in self.position):
            return
        else:
            for i, (x,y) in enumerate(self.position):
                self.position[i][0] -= 1

    def move_down(self):
        if any(y+1 == len(sim.grid[0]) or sim.grid[x][y+1] == "#" for x,y in self.position):
            return False
        else:
            for i, (x,y) in enumerate(self.position):
                self.position[i][1] += 1
            return True

    def readjust_grid(self):
        for col in sim.grid:
            for _ in range(sim.y_top):
                col.pop(0)
        sim.y_top = 0

    def sim_to_rest(self):
        while(1):
            jet = get_next_jet(sim.jet_seq)

            if jet == '<':
                self.move_left()
            if jet == '>':
                self.move_right()

            if not self.move_down():
                self.draw('#')
                sim.y_top = min(sim.y_top, self.position[0][1])
                self.readjust_grid()
                sim.rocks_fallen += 1
                break


    def draw(self, char):
        for x,y in self.position:
            sim.grid[x][y] = char


class Flat(Rock):
    width = 4
    height = 1
    shape = [
        [0,0], [1,0], [2,0], [3,0] 
    ]

class Plus(Rock):
    width = 3
    height = 3
    shape = [
               [1,0], 
        [0,1], [1,1], [2,1], 
               [1,2]
    ]

class L(Rock):
    width = 3
    height = 3
    shape = [
                      [2,0], 
                      [2,1], 
        [0,2], [1,2], [2,2]
    ]

class I(Rock):
    width = 1
    height = 4
    shape = [
        [0,0],
        [0,1],
        [0,2],
        [0,3],
    ]

class Square(Rock):
    width = 2
    height = 2
    shape = [
        [0,0], [1,0], 
        [0,1], [1,1]
    ]

def get_next_jet(jet_seq):
    try:
        get_next_jet.index += 1 
        get_next_jet.index %= len(jet_seq)
        return jet_seq[get_next_jet.index]
    except AttributeError:
        get_next_jet.index = -1
        return get_next_jet(jet_seq)

if __name__ == '__main__':
    sim = Sim()

    with open("in.txt", "r") as f:
        sim.jet_seq = f.readline().strip()

    sim.grid = [[] for _ in range(7)]

    shapes = [Flat(sim), Plus(sim), L(sim), I(sim), Square(sim)]

    for shape in cycle(shapes):
        if sim.rocks_fallen == 50000: break
        shape.set()
        shape.sim_to_rest()

    for row in [*zip(*sim.grid)]:
        for x in row:
            print(x, end='')
        print()

    print(len(sim.grid[0]))
