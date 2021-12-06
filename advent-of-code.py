# Solution for https://adventofcode.com/2021/day/5

import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Solve advent-of-code-2021 day#6 part#1')
parser.add_argument('-input', '-i', metavar='input_file', type=str, required=True,
                    help='file with puzzle input')

args = parser.parse_args()
print(args.input)

########################### Solution ############################
state = []

with open(args.input, "r") as p_input:
	for line in p_input:
		state = [int(x) for x in line.strip().split(",")]

NUM_DAYS = 80

def generate(x):
	if x > NUM_DAYS:
		return 0
	return 1 + generate(x + 7) + generate(x + 9)

s = len(state)
for x in state:
	s += generate(x+1)
print(s)


