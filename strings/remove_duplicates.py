'''
Write a function remove_duplicates() that takes in a sorted list of 
integers nums as a parameter and removes all duplicates in the list. 
The function returns the modified list.

'''

'''

UPI - Understand
 
- Given a sorted list of integers nums
- Remove all duplicates
- return the modified list



UPI - Plan

- check if the list is empty ? return empty list
- create a variable for the loop index
- Use a while loop to keep looping as long as 


UPI - Impliment

     |
[1,1,1,2,3,4,4,5,6,6]

'''

# def remove_duplicates(nums):
#     no_dups = []
#     index = 0
#     while index < len(nums):
#         if len(no_dups) == 0 or nums[index] != no_dups[-1]:
#             no_dups.append(nums[index])
#         index += 1
#     return no_dups


def remove_duplicates(nums):
    last_unique = 1
    for element in nums:
        print(element)
        if nums[element] != nums[last_unique]:
            last_unique = element
        nums.pop(element               
    return nums




nums = [1,1,1,2,3,4,4,5,6,6]
# Example Output: no_dups = [1,2,3,4,5,6]
nums2 = remove_duplicates(nums)
print(nums2)
        
