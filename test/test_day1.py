import pytest
import day1


@pytest.mark.parametrize('mass, expected_fuel', [(14, 2), (1969, 654), (100756, 33583)])
def test_part_1(mass, expected_fuel):
    calculated_fuel = day1.fuel_required(mass)
    assert calculated_fuel == expected_fuel


@pytest.mark.parametrize('mass, expected_fuel', [(14, 2), (1969, 966), (100756, 50346)])
def test_part_2(mass, expected_fuel):
    calculated_fuel = day1.fuel_required_recursive(mass)
    assert calculated_fuel == expected_fuel
