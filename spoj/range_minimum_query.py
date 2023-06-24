# Input:
# 3
# 1 4 1
# 2
# 1 1
# 1 2

# [1 4 1]
#    | |

# n - 2 ** power + 1

def find_min(table, l, r):
	length = (r - l + 1) # 2
	max_power = math.floor(math.log(length, 2)) # 1

	# min(table[1][1], table[2 - 2 + 1][1])

	return min(table[l][max_power], table[r - (2 ** max_power) + 1][max_power])

def main():
	# Parse the input
	n = int(input().rstrip()); # 3
	array = [int(i) for i in input().rstrip().split()] # [1 4 1]

	# Build the sparse table
	LOG = math.floor(math.log(n, 2)) # 1
	table = [[math.inf] * (1 + LOG) for _ in range(n)] 

	# [
	# 	[math.inf, math.inf],
	# 	[math.inf, math.inf],
	# 	[math.inf, math.inf],
	# ]

	for power in range(1 + LOG): # 0, 1
		for start_index in range(n - (2 ** power) + 1): # for 1: 0, 1
			if power == 0:
				table[start_index][power] = array[start_index]
			else:
				table[start_index][power] = min(table[start_index][power - 1], table[start_index + (2 ** (power - 1))][power - 1])
 	# power: 1, start_index: 0
 	# table[0][1] = min(table[0][0], table[1][0])

 	# start_index: 1, power: 1
 	# table[1][1] = min(table[1][0], table[2][0])

	# [
	# 	[1, 1],
	# 	[4, 1],
	# 	[1, math.inf],
	# ]

	# loop through the queries
	# and print out the result
	q = int(input().rstrip()) # 2
	for i in range(q):
		l, r = [int(x) for x in input().rstrip().split()]
		print(find_min(table, l, r))

if __name__ == '__main__':
	import math

	main()

# 3
# 1 4 1
# 2
# 1 1
# 1 2

