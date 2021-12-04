import numpy as np
from functools import reduce

p_input = [
"00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010",
]

vectorized_invert = np.vectorize(lambda x : (x ^ 1))

all_numbers = []
with open("input.txt", "r") as p_input:
	for line in p_input:
		chars = [c for c in line.strip()]
		all_numbers.append(np.array([int(c) for c in chars]))

all_numbers = np.array(all_numbers)
num_bits = all_numbers.shape[1]

def calc(numbers, filter_func):
	bit_pos = 0
	while len(numbers) > 1:
		bits = numbers[:, bit_pos]
		ones = np.sum(bits)
		zeros = np.sum(vectorized_invert(bits))
		numbers = numbers[np.where(numbers[:, bit_pos] == filter_func(ones, zeros))]
		bit_pos += 1

	return reduce(lambda a, b: ((a << 1) | b), numbers[0])

print(calc(all_numbers, lambda ones, zeros: ones >= zeros) * calc(all_numbers, lambda ones, zeros: ones < zeros))
