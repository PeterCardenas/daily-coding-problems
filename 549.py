'''
Given an array of integers where every integer occurs three times except for one integer, which
only occurs once, find and return the non-duplicated integer.

For example, given, [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
'''

def sol(ints):
	ones = 0
	twos = 0
	for i in ints:
		twos |= ones & i
		ones ^= i
		remove_third = ~(ones & twos)
		ones &= remove_third
		twos &= remove_third
	return ones

def main():
	tests = [
		[[6, 1, 3, 3, 3, 6, 6], 1],
		[[13, 19, 13, 13], 19]
	]
	for test_num, test in enumerate(tests):
		print(f'Test {test_num}: {"PASSED" if sol(test[0]) == test[1] else "FAILED"}')

main()
