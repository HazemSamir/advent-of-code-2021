# Solution for https://adventofcode.com/2021/day/12

import argparse
import numpy as np


parser = argparse.ArgumentParser(description='Solve advent-of-code-2021 day#12 part#1')
parser.add_argument('-input', '-i', metavar='input_file', type=str, required=True,
                    help='file with puzzle input')

args = parser.parse_args()
print(args.input)

########################### Solution ############################
def ReadInput():
	inpt = {}
	with open(args.input, "r") as p_input:
		for line in p_input:
			s, e = line.strip().split("-")
			if e != 'start' and s != 'end':
				AddToAdjecentList(s, e, inpt)
			if s != 'start' and e != 'end':
				AddToAdjecentList(e, s, inpt)

	return inpt

def AddToAdjecentList(s, e, adj_list):
	if s not in adj_list:
		adj_list[s] = []
	adj_list[s].append(e)


def dfs(c, cave_map, visited):
	if c in visited:
		return 0
	if c == 'end':
		return 1
	if c.islower():
		visited.append(c)
	count = 0
	for adj in cave_map[c]:
		count += dfs(adj, cave_map, visited)
	if c.islower():
		visited.pop()
	return count

cave_map = ReadInput()
print(dfs('start', cave_map, []))

