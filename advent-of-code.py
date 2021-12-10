# Solution for https://adventofcode.com/2021/day/9

import argparse
import numpy as np
from itertools import permutations


parser = argparse.ArgumentParser(description='Solve advent-of-code-2021 day#9 part#1')
parser.add_argument('-input', '-i', metavar='input_file', type=str, required=True,
                    help='file with puzzle input')

args = parser.parse_args()
print(args.input)

########################### Solution ############################
hmap = []

with open(args.input, "r") as p_input:
	for line in p_input:
		hmap.append([int(x) for x in line.strip()])

h = len(hmap)
w = len(hmap[0])

s = 0
for i in range(h):
	for j in range(w):
		s += (hmap[i][j] + 1) if (i - 1 < 0 or hmap[i][j] < hmap[i - 1][j]) and (j - 1 < 0 or hmap[i][j] < hmap[i][j - 1]) and (i + 1 >= h or hmap[i][j] < hmap[i + 1][j]) and (j + 1 >= w or hmap[i][j] < hmap[i][j + 1]) else 0
print(s)
