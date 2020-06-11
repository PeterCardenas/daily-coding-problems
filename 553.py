'''
You are given an N by M 2D matrix of lower case letters. Determine the minimum number of columns 
that can be removed to ensure that each row is ordered from top to bottom lexicographically. That
is, the letter at each column is lexicographically later as you go down each row. It does not
matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi

This is not ordered because of the a in the center. We can remove the second column to make it
ordered.

ca
df
gi

So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef

Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr

Your function should return 3, since we would need to remove all the columns to order it.
'''

def sol(matrix):
	if not matrix or len(matrix) == 1 or len(matrix[0]) == 0:
		return 0
	num_deleted = 0
	for col in range(len(matrix[0])):
		row = 0
		while row < len(matrix) - 1 and matrix[row][col] < matrix[row + 1][col]:
			row += 1
		if row < len(matrix) - 1 and matrix[row][col] > matrix[row + 1][col]:
			num_deleted += 1
	return num_deleted

def main():
	tests = [
		[[['c', 'b', 'a'], ['d', 'a', 'f'], ['g', 'h', 'i']], 1],
		[[['a', 'b', 'c', 'd', 'e', 'f']], 0],
		[[['z', 'y', 'x'], ['w', 'v', 'u'], ['t', 's', 'r']], 3]
	]
	for test_num, test in enumerate(tests):
		print(f'Test {test_num}: {"PASSED" if sol(test[0]) == test[1] else "FAILED"}')

main()
