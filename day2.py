import csv

from intcode_computer import IntcodeComputer


def part_1(input_data):
    int_comp = IntcodeComputer(input_data)
    input_data[1] = 12
    input_data[2] = 2
    return int_comp.run_program(input_data)


def part_2(input_data, desired_value):
    int_comp = IntcodeComputer(input_data)
    for i in range(100):
        for j in range(100):
            input_data[1] = i
            input_data[2] = j
            output = int_comp.run_program(input_data)
            if output == desired_value:
                return 100 * i + j


if __name__ == '__main__':
    with open('data/day2.txt') as csvfile:
        csv_data = [row for row in csv.reader(csvfile, delimiter=',')]
        int_data = [int(i) for i in csv_data[0]]

    part_1_result = part_1(int_data)
    part_2_result = part_2(int_data, 19690720)
