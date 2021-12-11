# Solution for https://adventofcode.com/2021/day/11

import argparse
import numpy as np


parser = argparse.ArgumentParser(description='Solve advent-of-code-2021 day#11 part#2')
parser.add_argument('-input', '-i', metavar='input_file', type=str, required=True,
                    help='file with puzzle input')

args = parser.parse_args()
print(args.input)

########################### Solution ############################
def ReadInput():
	inpt = []
	with open(args.input, "r") as p_input:
		for line in p_input:
			inpt.append([int(c) for c in line.strip()])

	return np.array(inpt, dtype=np.uint8)

def Adjecent(i, j):
	return [(i + x, j + y) for x in range(-1, 2) for y in range(-1, 2)]

def Flash(i, j, octmap, flashed):
	if i < 0 or j < 0 or i >= octmap.shape[0] or j >= octmap.shape[1] or flashed[i][j]:
		return 0
	if octmap[i][j] <= 9:
		octmap[i][j] += 1
		return 0

	flashed[i][j] = True
	octmap[i][j] = 0
	s = 1
	for x, y in Adjecent(i, j):
		s += Flash(x, y, octmap, flashed)
	return s

def FlashAll(octmap, flashed):
	flash_count = 0
	for i, j in np.transpose((octmap > 9).nonzero()):
		flash_count += Flash(i, j, octmap, flashed)
	return flash_count

def Step(octmap):
	octmap += np.uint8(1)
	flashed = np.zeros(octmap.shape, dtype=bool)
	all_flash_count = 0
	flash_count = FlashAll(octmap, flashed)
	while flash_count > 0:
		all_flash_count += flash_count
		flash_count = FlashAll(octmap, flashed)

	return all_flash_count

octmap = ReadInput()
step_count = 0
while np.count_nonzero(octmap) > 0:
	Step(octmap)
	step_count += 1

print(step_count)
