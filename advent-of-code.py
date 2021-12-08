# Solution for https://adventofcode.com/2021/day/7

import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Solve advent-of-code-2021 day#7 part#2')
parser.add_argument('-input', '-i', metavar='input_file', type=str, required=True,
                    help='file with puzzle input')

args = parser.parse_args()
print(args.input)

########################### Solution ############################
state = []

with open(args.input, "r") as p_input:
	for line in p_input:
		state = [int(x) for x in line.strip().split(",")]


lo = min(state)
hi = max(state)

def CalcCost(p):
	cost = 0
	for st in state:
		diff = abs(p - st)
		cost += (diff * (diff + 1)) / 2
	return cost

while lo < hi:
	mid = int((lo+hi) / 2)
	if mid == lo:
		break

	if CalcCost(mid) > CalcCost(mid+1):
		lo = mid
	else:
		hi = mid

print(min(CalcCost(lo), CalcCost(hi)))
