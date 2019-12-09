import csv
from intcode_computer import TEST

if __name__ == '__main__':
    with open('data/day5.txt') as csvfile:
        csv_data = [row for row in csv.reader(csvfile, delimiter=',')]
        int_data = [int(i) for i in csv_data[0]]
    test_program = TEST(int_data)
