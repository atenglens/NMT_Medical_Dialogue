# outputs average of numbers in a file

import sys

# data file
file = sys.argv[1]

numbers = open(file, encoding='utf-8').read().split('\n')
while("" in numbers):
    numbers.remove("")

average = sum([float(n) for n in numbers]) / len(numbers)

print(average)