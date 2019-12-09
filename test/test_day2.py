import pytest
from intcode_computer import IntcodeComputer


@pytest.mark.parametrize('initial_state, expected_state',
                         [([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]), ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
                          ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
                          ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99])])
def test_part_1(initial_state, expected_state):
    computer = IntcodeComputer(initial_state)
    computer.run_program()
    assert computer.cache == expected_state


@pytest.mark.parametrize('initial_state, desired_output, expected_calculation', [(
        [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 6, 19,
         1, 5, 19, 23, 1, 23, 6, 27, 1, 5, 27, 31, 1, 31, 6, 35, 1,
         9, 35, 39, 2, 10, 39, 43, 1, 43, 6, 47, 2, 6, 47, 51, 1, 5,
         51, 55, 1, 55, 13, 59, 1, 59, 10, 63, 2, 10, 63, 67, 1, 9,
         67, 71, 2, 6, 71, 75, 1, 5, 75, 79, 2, 79, 13, 83, 1, 83, 5,
         87, 1, 87, 9, 91, 1, 5, 91, 95, 1, 5, 95, 99, 1, 99, 13,
         103, 1, 10, 103, 107, 1, 107, 9, 111, 1, 6, 111, 115, 2,
         115, 13, 119, 1, 10, 119, 123, 2, 123, 6, 127, 1, 5, 127,
         131, 1, 5, 131, 135, 1, 135, 6, 139, 2, 139, 10, 143, 2,
         143, 9, 147, 1, 147, 6, 151, 1, 151, 13, 155, 2, 155, 9,
         159, 1, 6, 159, 163, 1, 5, 163, 167, 1, 5, 167, 171, 1, 10,
         171, 175, 1, 13, 175, 179, 1, 179, 2, 183, 1, 9, 183, 0, 99,
         2, 14, 0, 0], 19690720, 8051)])
def test_part_2(initial_state, desired_output, expected_calculation):
    actual_calculation = None
    computer = IntcodeComputer(initial_state)
    for i in range(100):
        for j in range(100):
            program = list(initial_state)
            program[1] = i
            program[2] = j
            output = computer.run_program(program)
            if output == desired_output:
                actual_calculation = 100 * i + j
    assert actual_calculation == expected_calculation
