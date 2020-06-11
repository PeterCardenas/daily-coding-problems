'''
Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
'''

class Node:
	def __init__(self, val, next):
		self.val = val
		self.next = next
	def __eq__(self, other):
		if not other:
			return False
		return self.val == other.val and self.next == other.next
	def __str__(self):
		curr = self
		str = ''
		while curr.next:
			str += f'{curr.val} -> '
			curr = curr.next
		return str + f'{curr.val}'

def sol(head):
	if not head:
		return head
	new_head = head.next
	curr = head
	while curr and curr.next:
		temp = curr.next
		curr.next = curr.next.next
		temp.next = curr
		temp = curr.next
		if curr.next and curr.next.next:
			curr.next = curr.next.next
		curr = temp
	return new_head

def main():
	tests = [
		[Node(1, Node(2, Node(3, Node(4, None)))), Node(2, Node(1, Node(4, Node(3, None))))]
	]
	for test_num, test in enumerate(tests):
		eval = sol(test[0])
		print(f'Test {test_num}: {"PASSED" if eval == test[1] else "FAILED"}')
main()
