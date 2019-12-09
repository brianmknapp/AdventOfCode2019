class IntcodeComputer(object):
    def __init__(self, memory):
        self.memory = list(memory)
        self.cache = []

    def run_program(self, program=None):
        if program is None:
            program = list(self.memory)
        self.cache = list(program)
        for i in range(0, len(self.cache) - 1, 4):
            case = self.cache[i]
            if case == 99:
                break
            elif case == 1:
                self.add(i + 1, i + 2, i + 3)
            elif case == 2:
                self.multiply(i + 1, i + 2, i + 3)
            else:
                continue
        return self.cache[0]

    def add(self, value_1_cell, value_2_cell, placement_cell):
        value_1_location = self.cache[value_1_cell]
        value_2_location = self.cache[value_2_cell]
        placement_location = self.cache[placement_cell]
        self.cache[placement_location] = self.cache[value_1_location] + self.cache[value_2_location]

    def multiply(self, value_1_cell, value_2_cell, placement_cell):
        value_1_location = self.cache[value_1_cell]
        value_2_location = self.cache[value_2_cell]
        placement_location = self.cache[placement_cell]
        self.cache[placement_location] = self.cache[value_1_location] * self.cache[value_2_location]
