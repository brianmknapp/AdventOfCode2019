class TEST(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.run_diagnostic()

    def run_diagnostic(self):
        compy = IntcodeComputer(self.input_data)
        print('Final position 0 value: {}'.format(compy.run_program()))


class IntcodeComputer(object):
    def __init__(self, memory):
        self.memory = list(memory)
        self.cache = []
        self.ip = 0

    def run_program(self, program=None):
        if program is None:
            program = list(self.memory)
        self.cache = list(program)
        self.ip = 0
        while self.ip < len(self.cache):
            try:
                param_3_mode, param_2_mode, param_1_mode, case = self.parse_instruction(self.cache[self.ip])
                if case == 99:
                    break
                elif case == 1:
                    self.add(self.ip + 1, param_1_mode, self.ip + 2, param_2_mode, self.ip + 3, param_3_mode)
                    self.ip += 4
                elif case == 2:
                    self.multiply(self.ip + 1, param_1_mode, self.ip + 2, param_2_mode, self.ip + 3, param_3_mode)
                    self.ip += 4
                elif case == 3:
                    self.save(self.ip + 1, param_1_mode)
                    self.ip += 2
                elif case == 4:
                    self.output(self.ip + 1, param_1_mode)
                    self.ip += 2
                elif case == 5:
                    jump, position = self.jump_if_true(self.ip + 1, param_1_mode, self.ip + 2, param_2_mode)
                    if jump:
                        self.ip = position
                    else:
                        self.ip += position
                elif case == 6:
                    jump, position = self.jump_if_false(self.ip + 1, param_1_mode, self.ip + 2, param_2_mode)
                    if jump:
                        self.ip = position
                    else:
                        self.ip += position
                elif case == 7:
                    self.less_than(self.ip + 1, param_1_mode, self.ip + 2, param_2_mode, self.ip + 3, param_3_mode)
                    self.ip += 4
                elif case == 8:
                    self.equals(self.ip + 1, param_1_mode, self.ip + 2, param_2_mode, self.ip + 3, param_3_mode)
                    self.ip += 4
                else:
                    self.ip += 1
            except Exception as ex:
                print('debug')
        return self.cache[0]

    @staticmethod
    def parse_instruction(instruction):
        instruction = str(instruction).zfill(5)
        opcode = int(instruction[-2:])
        param_1_mode = int(instruction[2])
        param_2_mode = int(instruction[1])
        param_3_mode = int(instruction[0])
        return param_3_mode, param_2_mode, param_1_mode, opcode

    def get_values(self, param_1, param_1_mode, param_2, param_2_mode, param_3, param_3_mode):
        value_1 = self.cache[param_1] if param_1_mode == 1 else self.cache[self.cache[param_1]]
        value_2 = self.cache[param_2] if param_2_mode == 1 else self.cache[self.cache[param_2]]
        value_3 = param_3 if param_3_mode == 1 else self.cache[param_3]
        return value_1, value_2, value_3

    def add(self, param_1, param_1_mode, param_2, param_2_mode, param_3, param_3_mode):
        value_1, value_2, position = self.get_values(param_1, param_1_mode, param_2, param_2_mode, param_3,
                                                     param_3_mode)
        self.cache[position] = value_1 + value_2

    def multiply(self, param_1, param_1_mode, param_2, param_2_mode, param_3, param_3_mode):
        value_1, value_2, position = self.get_values(param_1, param_1_mode, param_2, param_2_mode, param_3,
                                                     param_3_mode)
        self.cache[position] = value_1 * value_2

    def save(self, param, mode):
        position = param if mode == 1 else self.cache[param]
        self.cache[position] = int(input('Input integer to save in position {}: '.format(position)))

    def output(self, param, mode):
        position = param if mode == 1 else self.cache[param]
        print(self.cache[position])

    def jump_if_true(self, param_1, param_1_mode, param_2, param_2_mode):
        value_1 = self.cache[param_1] if param_1_mode == 1 else self.cache[self.cache[param_1]]
        value_2 = self.cache[param_2] if param_2_mode == 1 else self.cache[self.cache[param_2]]
        if value_1 != 0:
            return True, value_2
        else:
            return False, 3

    def jump_if_false(self, param_1, param_1_mode, param_2, param_2_mode):
        value_1 = self.cache[param_1] if param_1_mode == 1 else self.cache[self.cache[param_1]]
        value_2 = self.cache[param_2] if param_2_mode == 1 else self.cache[self.cache[param_2]]
        if value_1 == 0:
            return True, value_2
        else:
            return False, 3

    def less_than(self, param_1, param_1_mode, param_2, param_2_mode, param_3, param_3_mode):
        value_1, value_2, position = self.get_values(param_1, param_1_mode, param_2, param_2_mode, param_3,
                                                     param_3_mode)
        self.cache[position] = 1 if value_1 < value_2 else 0

    def equals(self, param_1, param_1_mode, param_2, param_2_mode, param_3, param_3_mode):
        value_1, value_2, position = self.get_values(param_1, param_1_mode, param_2, param_2_mode, param_3,
                                                     param_3_mode)
        self.cache[position] = 1 if value_1 == value_2 else 0
