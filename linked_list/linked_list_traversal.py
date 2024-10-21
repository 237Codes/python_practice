'''
To perform a traversal, take the following steps:

- Create a pointer current and initialize it to the first node in the list.

- Create a while loop that continues iterating as long as the current node is not None 
(aka as long as there are still nodes in the list we haven't traversed).

- In the body of the while loop:
	perform whatever actions you would like to the current node 
	(e.g. printing the current node's value)
	update current to point at the next node in the linked list

'''
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next

def print_linked_list(head):
	current = head
	while current:
		curr = current
		if current.next is not None:
			nex = current.next
		print(f'{curr.value} -> {nex.value}')
		current = current.next


node_1 = Node("a")
node_2 = Node("b")
node_3 = Node("c")
node_4 = Node("d")
node_5 = Node("e")

# Link the nodes to each nother

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

# Traverse the list starting from node1 (the head)
print("Traversing the linked list:")
print_linked_list(node_1) 