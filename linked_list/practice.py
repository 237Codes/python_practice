'''
Given the head of a linked list where each node is an integer value, 
return the maximum value in the linked list.

U: from head, find max value 
P: traverse through the list, compare values 
I: while a loop to the end of the LL, variable to store max value
'''

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def find_max(head):
#     if head is None:
#         return None

#     maxVal = 0
#     current = head
#     while current:
#         if current.value > maxVal:
#             maxVal = current.value 
#         current = current.next
#     return maxVal

# LL = Node(1, Node(4, Node(1, Node(2))))
# print(find_max(LL))







'''
Problem 3: Remove First Value
The following code attempts to remove the first node with a given value 
from a singly linked list based but it contains a bug!

Step 1: Copy this code into Replit.

Step 2: Create your own test cases to run the code against,
 and use print statements and the stack trace to identify and fix the bug 
 so that the function correctly removes a node by value from the list.


 Understand
    Removes the value given
 Plan 
    Walk through the code and find the correct imlimentation
 Impliment

'''
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# Function with a bug!
def remove_by_value(head, val):
    # Check if the list is empty
    if head is None:
        return head

    # If the node to be removed is the head of the list
    if head.value == val:
        return head.next

    # Initialize pointers
    current = head.next
    previous = head

    # Traverse the list to find the node to remove
    while current.next:
        # print(current.value)
        if current.next == val:
            print("Yay")
        
        # if current.value == val:
        #     previous.next = current.next
        #     return head

        # previous = current
        current = current.next

    # If no node was found with the value `val`, return the original head
    return head


# Input List: 1 -> 2 -> 3 -> 4
            #      |    |
# Value to Remove: 3

# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 4

LL = Node(3, Node(4, Node(1, Node(2))))
print_list(LL)
new_head = remove_by_value(LL, 2)
print_list(new_head)