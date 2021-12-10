# Solution for https://adventofcode.com/2021/day/10

import argparse


parser = argparse.ArgumentParser(description='Solve advent-of-code-2021 day#10 part#1')
parser.add_argument('-input', '-i', metavar='input_file', type=str, required=True,
                    help='file with puzzle input')

args = parser.parse_args()
print(args.input)

########################### Solution ############################
synt = []

with open(args.input, "r") as p_input:
	for line in p_input:
		synt.append(line.strip())

CHARS = {')': '(', ']':'[', '}':'{', '>':'<'}
CHARS_SCORE = {')': 3, ']': 57, '}': 1197, '>': 25137}

score = 0
for line in synt:
	stack = []
	for c in line:
		if c in CHARS:
			if len(stack) == 0 or stack[-1] != CHARS[c]:
				score += CHARS_SCORE[c]
				break
			else:
				stack.pop()
		else:
			stack.append(c)
print(score)

