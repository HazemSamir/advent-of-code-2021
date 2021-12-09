# Solution for https://adventofcode.com/2021/day/8

import argparse
import numpy as np
from itertools import permutations


parser = argparse.ArgumentParser(description='Solve advent-of-code-2021 day#8 part#2')
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

all_perms = [''.join(p) for p in permutations('abcdefg')]

possible_numbers = []
for p in all_perms:
	numbers = 10 * [None]
	#             a      b      c      d      e      f      g
	numbers[0] = p[0] + p[1] + p[2] +        p[4] + p[5] + p[6]
	numbers[1] =               p[2]               + p[5]
	numbers[2] = p[0]        + p[2] + p[3] + p[4]        + p[6]
	numbers[3] = p[0]        + p[2] + p[3]        + p[5] + p[6]
	numbers[4] =        p[1] + p[2] + p[3]        + p[5]
	numbers[5] = p[0] + p[1]        + p[3]        + p[5] + p[6]
	numbers[6] = p[0] + p[1]        + p[3] + p[4] + p[5] + p[6]
	numbers[7] = p[0]        + p[2]               + p[5]
	numbers[8] = p[0] + p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
	numbers[9] = p[0] + p[1] + p[2] + p[3]        + p[5] + p[6]
	possible_numbers.append([''.join(sorted(n)) for n in numbers])

count = 0
for st in state:
	st_number = ''
	st[0] = [''.join(sorted(s)) for s in st[0]]
	st[1] = [''.join(sorted(s)) for s in st[1]]
	for n in possible_numbers:
		found_all = True
		for x in st[0] + st[1]:
			if x not in n:
				# print(x, "not in", n)
				found_all = False
				break
		if found_all:
			for output in st[1]:
				st_number += str(n.index(output))
			break
	count += int(st_number)
	# print(count, st_number)
print(count)
