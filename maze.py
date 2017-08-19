class Maze:
    def __init__(self):
        self.array = []
        self.start = None
        self.finish = None
        self.partial_solutions = None
        self.state = 'incomplete'
        self.width = None
        self.height = None

    def set_start(self, start):
        self.start = start

    def set_finish(self, finish):
        self.finish = finish

    def append(self, item):
        self.array.append(item)

    def __str__(self):
        return str(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def generate_partial_solutions(self):
        self.partial_solutions = []
        for row in range(self.height):
            self.partial_solutions.append([])
            for collumn in range(self.width):
                self.partial_solutions[row].append([])
