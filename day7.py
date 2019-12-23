import csv
from itertools import permutations
from intcode_computer import AmplifierControlSoftware

if __name__ == '__main__':
    with open('data/day7.txt') as csvfile:
        csv_data = [row for row in csv.reader(csvfile, delimiter=',')]
        int_data = [int(i) for i in csv_data[0]]
    result_data = {}
    perms = permutations([0, 1, 2, 3, 4])
    for perm in perms:
        test_program = AmplifierControlSoftware(int_data, list(perm))
        test_program_result = test_program.run_program()
        for k, v in test_program_result.items():
            result_data[k] = v
    result_data_values = sorted(result_data.items(), reverse=True, key=lambda x: x[1])
    print('debug')
