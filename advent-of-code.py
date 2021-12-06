# Solution for https://adventofcode.com/2021/day/6

import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Solve advent-of-code-2021 day#6 part#2')
parser.add_argument('-input', '-i', metavar='input_file', type=str, required=True,
                    help='file with puzzle input')

args = parser.parse_args()
print(args.input)

########################### Solution ############################
state = []

with open(args.input, "r") as p_input:
	for line in p_input:
		state = [int(x) for x in line.strip().split(",")]

NUM_DAYS = 256
dp = (NUM_DAYS + 9) * [0]

for d in range(NUM_DAYS-1, -1, -1):
	dp[d] = 1 + dp[d + 7] + dp[d + 9]

s = len(state)
for x in state:
	s += dp[x]
print(s)
