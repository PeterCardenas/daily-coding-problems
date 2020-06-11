'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
def _BAD_sol(arr, k):
	for i in range(0, len(arr) - 1):
		for j in range(i + 1, len(arr)):
			if arr[i] + arr[j] == k:
				return True
	return False

def sol(arr, k):
	if not arr:
		return False
	addends = {k - arr[0]}
	for i in range(1, len(arr)):
		if arr[i] in addends:
			return True
		addends.add(k - arr[i])
	return False

def main():
	tests = [
		[[10, 15, 3, 7], 17, True]
	]
	for test in tests:
		print(f'Test 1: {"PASSED" if sol(test[0], test[1]) == test[2] else "FAILED"}')

main()
