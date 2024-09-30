'''

Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

'''

def  contains_duplicate(nums):
    seen= {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = True
    return False


def test_contains_duplicate():
    # Test case 1: List with duplicates
    nums = [1, 2, 3, 1]
    assert contains_duplicate(nums) == True

    # Test case 2: List without duplicates
    nums = [1, 2, 3, 4]
    assert contains_duplicate(nums) == False

    # Test case 3: Empty list
    nums = []
    assert contains_duplicate(nums) == False

    # Test case 4: List with one element
    nums = [1]
    assert contains_duplicate(nums) == False

    # Test case 5: List with all elements the same
    nums = [1, 1, 1, 1]
    assert contains_duplicate(nums) == True

    # Test case 6: List with negative numbers
    nums = [-1, -2, -3, -1]
    assert contains_duplicate(nums) == True

    # Test case 7: List with mixed positive and negative numbers
    nums = [1, -1, 2, -2, 1]
    assert contains_duplicate(nums) == True

    # Test case 8: List with large numbers
    nums = [1000000, 2000000, 3000000, 1000000]
    assert contains_duplicate(nums) == True

    # Test case 9: List with no duplicates but large numbers
    nums = [1000000, 2000000, 3000000, 4000000]
    assert contains_duplicate(nums) == False

    # Test case 10: List with duplicates at the end
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    assert contains_duplicate(nums) == True

# Run the test cases
test_contains_duplicate()
print("All test cases passed!")