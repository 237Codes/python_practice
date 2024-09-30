'''

Write a function index_to_value_map() that takes in a list 
lst and returns a dictionary that maps the index of each element 
in lst to its value.

Example Input: lst = ["apple", "banana", "cherry"]

Example Output: {0: "apple", 1: "banana", 2: "cherry"}

'''

'''

UPI - Understand

- given a list, map each list value to its index
- index is the key, list_item is the value
- return the dictionary that maps them in that order



UPI - Plan

- create a dictionary
- Loop through the list
- get the index and set it to a map key
- get the list_item and set it to the map value
- return the dictionary

UPI - Impliment

'''

def index_to_value_map(list):
    dict = {}
    index = 0
    for item in list:
        dict[index] = item
        index += 1
    return dict

lst = ["apple", "banana", "cherry"]
print (index_to_value_map(lst))