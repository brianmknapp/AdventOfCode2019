class TEST(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.run_diagnostic()

    def run_diagnostic(self):
        system_id = int(input('Enter the System ID to test: '))
        if system_id == 1:
            compy = IntcodeComputer(self.input_data)
            compy.run_program()


class IntcodeComputer(object):
    def __init__(self, memory):
        self.memory = list(memory)
        self.cache = []

    def run_program(self, program=None):
        if program is None:
            program = list(self.memory)
        self.cache = list(program)
        i = 0
        while i < len(self.cache):
            param_3_mode, param_2_mode, param_1_mode, case = self.parse_instruction(self.cache[i])
            if case == 99:
                break
            elif case == 1:
                self.add(i + 1, param_1_mode, i + 2, param_2_mode, i + 3, param_3_mode)
                i += 4
            elif case == 2:
                self.multiply(i + 1, param_1_mode, i + 2, param_2_mode, i + 3, param_3_mode)
                i += 4
            elif case == 3:
                self.save(i + 1, param_1_mode)
                i += 2
            elif case == 4:
                self.output(i + 1, param_1_mode)
                i += 2
            else:
                i += 1
        return self.cache[0]

    @staticmethod
    def parse_instruction(instruction):
        instruction = str(instruction).zfill(5)
        opcode = int(instruction[-2:])
        param_1_mode = int(instruction[2])
        param_2_mode = int(instruction[1])
        param_3_mode = int(instruction[0])
        return param_3_mode, param_2_mode, param_1_mode, opcode

    def add(self, param_1, param_1_mode, param_2, param_2_mode, param_3, param_3_mode):
        value_1 = self.cache[param_1] if param_1_mode == 1 else self.cache[self.cache[param_1]]
        value_2 = self.cache[param_2] if param_2_mode == 1 else self.cache[self.cache[param_2]]
        position = param_3 if param_3_mode == 1 else self.cache[param_3]
        self.cache[position] = value_1 + value_2

    def multiply(self, param_1, param_1_mode, param_2, param_2_mode, param_3, param_3_mode):
        value_1 = self.cache[param_1] if param_1_mode == 1 else self.cache[self.cache[param_1]]
        value_2 = self.cache[param_2] if param_2_mode == 1 else self.cache[self.cache[param_2]]
        position = param_3 if param_3_mode == 1 else self.cache[param_3]
        self.cache[position] = value_1 * value_2

    def save(self, param, mode):
        position = param if mode == 1 else self.cache[param]
        self.cache[position] = int(input('Input integer to save in position {}: '.format(position)))

    def output(self, param, mode):
        position = param if mode == 1 else self.cache[param]
        print(self.cache[position])
