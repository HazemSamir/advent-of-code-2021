# Solution for https://adventofcode.com/2021/day/9

import argparse
import numpy as np
from itertools import permutations


parser = argparse.ArgumentParser(description='Solve advent-of-code-2021 day#9 part#2')
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

vis = [[False for y in range(w)] for x in range(h)]

def dfs_basin(x, y):
	if x < 0 or y < 0 or x >= h or y >= w:
		return 0
	if vis[x][y]:
		return 0
	vis[x][y] = True
	if hmap[x][y] == 9:
		return 0
	return 1 + dfs_basin(x + 1, y) + dfs_basin(x - 1, y) + dfs_basin(x, y + 1) + dfs_basin(x, y - 1)

basins = []
for i in range(h):
	for j in range(w):
		if not vis[i][j] and hmap[i][j] != 9:
			basins.append(dfs_basin(i, j))

basins = sorted(basins)
print(basins[-1] * basins[-2] * basins[-3])
