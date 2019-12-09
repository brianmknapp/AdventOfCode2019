import math


def fuel_required(mass):
    floor = mass / 3
    return math.floor(floor) - 2


def fuel_required_recursive(mass):
    floor = mass / 3
    fuel = math.floor(floor) - 2
    if fuel <= 0:
        return 0
    return fuel + fuel_required_recursive(fuel)


if __name__ == '__main__':
    part_1 = 0
    part_2 = 0
    with open('data/day1.txt') as f:
        lines = f.readlines()
    int_list = [int(i) for i in lines]
    for value in int_list:
        part_1 += fuel_required(value)
        part_2 += fuel_required_recursive(value)
    print('debug')
