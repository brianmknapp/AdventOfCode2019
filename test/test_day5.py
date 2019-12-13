import mock
import pytest
from intcode_computer import IntcodeComputer


@pytest.mark.parametrize('initial_state, test_input, expected_output', [(
        [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 7, 0)])
def test_part_2(initial_state, test_input, expected_output):
    actual_output = None
    computer = IntcodeComputer(initial_state)
    for i in range(100):
        for j in range(100):
            program = list(initial_state)
            program[1] = i
            program[2] = j
            actual_output = computer.run_program(program)
    assert actual_output == expected_output
