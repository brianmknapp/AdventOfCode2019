import pytest
import day4


@pytest.mark.parametrize('input_password, validity', [(111111, False), (223450, False), (123789, False)])
def test_part_1(input_password, validity):
    password_valid = day4.password_valid(input_password)
    assert password_valid == validity


@pytest.mark.parametrize('input_password, validity', [(112233, True), (123444, False), (111122, True)])
def test_part_1(input_password, validity):
    password_valid = day4.password_valid(input_password)
    assert password_valid == validity
