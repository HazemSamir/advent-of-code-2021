import argparse
import numpy as np

from functools import reduce

parser = argparse.ArgumentParser(description='Solve advent-of-code-2021 day#4 part#1')
parser.add_argument('-input', '-i', metavar='input_file', type=str, required=True,
                    help='file with puzzle input')

args = parser.parse_args()
print(args.input)

########################### Solution ############################
all_winning_pos = []
for x in range(5):
	#rows
	all_winning_pos.append(np.uint32(0b11111 << (x*5)))
	#cols
	all_winning_pos.append(np.uint32(0b0000100001000010000100001 << x))

# 01111
# 10111
# 11011
# 11101
# 11110
all_winning_pos.append(np.uint32(0b0111110111110111110111110))
# 11110
# 11101
# 11011
# 10111
# 01111
all_winning_pos.append(np.uint32(0b1111011101110111011101111))

# for board in all_winning_pos:
# 	print(np.binary_repr(board))

numbers = []
boards = []
board_map = {}

with open(args.input, "r") as p_input:
	for line in p_input:
		line = line.strip()
		# read input numbers from first line
		if len(numbers) == 0:
			numbers = [int(x) for x in line.split(",")]
			continue

		# empty line -> a new board
		if len(line) == 0:
			boards.append([])
			continue

		boards[-1] += [int(x) for x in line.split()]

for i, board in enumerate(boards):
	print(board)
	for j, x in enumerate(board):
		if x in board_map:
			board_map[x].append((i, j))
		else:
			board_map[x] = [(i, j)]

boards = np.array(boards, dtype=np.uint32)
board_mask = np.zeros((len(boards)), dtype=np.uint32)

for x in numbers:
	print(x)
	if x not in board_map:
		print("skipped", x, "not in any board")
		continue
	for i, j in board_map[x]:
		print (i, j)
		board_mask[i] |= np.uint32(1 << j)

	for winning_pos in all_winning_pos:
		for board, mask in zip(boards, board_mask):
			if mask & winning_pos == winning_pos:
				print("We have a winner!", board, mask)
				unpacker = 2**np.arange(25, dtype=mask.dtype)
				unpacked = (~(mask & unpacker).astype(bool)).astype(np.uint32)
				print(np.sum(unpacked * board) * x)
				exit(0)
	print()
