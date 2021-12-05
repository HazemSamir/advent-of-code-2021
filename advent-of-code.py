import argparse
import numpy as np

from functools import reduce

parser = argparse.ArgumentParser(description='Solve advent-of-code-2021 day#5 part#1')
parser.add_argument('-input', '-i', metavar='input_file', type=str, required=True,
                    help='file with puzzle input')

args = parser.parse_args()
print(args.input)

########################### Solution ############################
vents = []
dims = [0, 0]

with open(args.input, "r") as p_input:
	for line in p_input:
		line = [p.split(",") for p in line.strip().split(" -> ")]
		vents.append([[int(c[0]), int(c[1])] for c in line])
		dims = [max([dims[0]] + [vents[-1][i][0] + 1 for i in range(2)]),
				max([dims[1]] + [vents[-1][i][1] + 1 for i in range(2)])]

m = np.zeros(dims, dtype=np.int32)
for b, e in vents:
	if b[0] == e[0]:
		m[b[0], min(b[1], e[1]) : max(b[1], e[1]) + 1] += 1
	if b[1] == e[1]:
		m[min(b[0], e[0]) : max(b[0], e[0]) + 1, b[1]] += 1

print(m)
# converting first bit to 0 only keeps values > 1, converts 1 to zeros.
# we don't actually care about other values.
m &= (~np.int32(0) << 1)
print(np.count_nonzero(m))
