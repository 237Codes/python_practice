'''

Write a function is_subsequence() that takes in a list of integers lst 
and a list of integers sequence as parameters. Given these two lists, 
determine whether the sequence list is a subsequence of the lst list. 
A subsequence of a list is a set of numbers that aren't necessarily 
adjacent but are in the same relative order as they appear in the list. 
Return True if sequence is a subsequence, and False otherwise.

Example Usage:

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))
Example Output: True

'''

'''

UPI - Understand

- Given two lists, check whether a list is a subsequenc of another list.
- They do not need to be near each other but the elements need to be in the same 
- relative position in the list

UPI - Plan

- ny idea is to go though the lists using a two pointer approach and check to see if each 
elemtns dalls in the same relative position/ 

UPI - Impliment

'''
def is_subsequence(lst, sequence):
    if not sequence:     # check if the sequence lsit is empty, and we are return True
        return True

    index = 0 
    for value in lst:
        if index < len(sequence) and value == sequence[index]:
            index += 1
    if index == len(sequence):
        return True
    else:
        return False
    

# Test whether is works.

def test_is_subsequence():
    # Test case 1: Both lists are empty
    assert is_subsequence([], []) == True

    # Test case 2: Main list is empty, sequence is not
    assert is_subsequence([], [1, 2, 3]) == False

    # Test case 3: Sequence list is empty, main list is not
    assert is_subsequence([1, 2, 3], []) == True

    # Test case 4: Sequence is a subsequence of the main list
    assert is_subsequence([1, 2, 3, 4, 5], [1, 3, 5]) == True

    # Test case 5: Sequence is not a subsequence of the main list
    assert is_subsequence([1, 2, 3, 4, 5], [1, 4, 3]) == False

    # Test case 6: Sequence is the same as the main list
    assert is_subsequence([1, 2, 3], [1, 2, 3]) == True

    # Test case 7: Sequence has elements not in the main list
    assert is_subsequence([1, 2, 3], [4, 5, 6]) == False

    # Test case 8: Sequence is longer than the main list
    assert is_subsequence([1, 2], [1, 2, 3]) == False

    # Test case 9: Sequence is a single element present in the main list
    assert is_subsequence([1, 2, 3], [2]) == True

    # Test case 10: Sequence is a single element not present in the main list
    assert is_subsequence([1, 2, 3], [4]) == False

# Run the test cases
test_is_subsequence()
print("All test cases passed!")