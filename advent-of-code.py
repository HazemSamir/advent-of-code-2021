# Solution for https://adventofcode.com/2021/day/8

import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Solve advent-of-code-2021 day#8 part#1')
parser.add_argument('-input', '-i', metavar='input_file', type=str, required=True,
                    help='file with puzzle input')

args = parser.parse_args()
print(args.input)

########################### Solution ############################
state = []

with open(args.input, "r") as p_input:
	for line in p_input:
		line = line.strip().split("|")
		state.append([x.split() for x in line])

count = 0
for x in state:
	for output in x[1]:
		if len(output) in [2, 3, 4, 7]:
			count += 1
print(count)
