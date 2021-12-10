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
CHARS_SCORE = {'(': 1, '[': 2, '{': 3, '<': 4}

scores = []
for line in synt:
	stack = []
	is_illegal = False
	for c in line:
		if c in CHARS:
			if len(stack) == 0 or stack[-1] != CHARS[c]:
				is_illegal = True
				break
			else:
				stack.pop()
		else:
			stack.append(c)
	if not is_illegal:
		s = 0
		for c in reversed(stack):
			s *= 5
			s += CHARS_SCORE[c]
		scores.append(s)

scores = sorted(scores)
print(scores)
print(scores[int(len(scores) / 2)])

