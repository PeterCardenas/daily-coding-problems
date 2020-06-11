'''
Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
'''
def sol(lists):
	if not lists:
		return lists
	if len(lists) == 1:
		return lists[0]
	if len(lists) == 2:
		left = lists[0]
		right = lists[1]
	else:
		left = sol(lists[0 : len(lists) // 2])
		right = sol(lists[len(lists) // 2 : len(lists)])
	merged = []
	left_index = 0
	right_index = 0
	while (left_index < len(left) and right_index < len(right)):
		if (left[left_index] < right[right_index]):
			merged.append(left[left_index])
			left_index += 1
		else:
			merged.append(right[right_index])
			right_index += 1
	while (left_index < len(left)):
		merged.append(left[left_index])
		left_index += 1
	while (right_index < len(right)):
		merged.append(right[right_index])
		right_index += 1
	return merged

def main():
	tests = [
		[[[1, 4, 6, 8], [2, 3, 7, 8]], [1, 2, 3, 4, 6, 7, 8, 8]],
		[[[0, 2, 4, 6, 8, 9], [0, 1, 2, 3, 4, 6, 7, 8, 9], [1, 3, 5, 7, 9], [1, 2, 2, 3, 3, 4, 5, 8]], [0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 9]]
	]
	for test_num, test in enumerate(tests):
		print(f'Test {test_num}: {"PASSED" if sol(test[0]) == test[1] else "FAILED"}')

main()
