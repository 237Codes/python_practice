'''
Write a function sum_of_number_strings() that takes in a list of strings nums. 
Each string is a representations of integers. The function should return the sum 
of these strings as an integer.

'''

'''

UPI - Understand

- Given a list of strings 
- Each string is a representation of an integer.
- Return the sum of these strings as an integer


UPI - Plan

- variable to hold the total value and set value to 0
- loop through the list of strings
-  take the integer value of eact string and add it to the total
- return the total



UPI - Impliment

'''

def sum_of_number_strings(nums):
    total = 0

    for string in nums:
        total += int(string)
    return total
        

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
