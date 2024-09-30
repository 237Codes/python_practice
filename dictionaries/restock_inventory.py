'''

Write a function restock_inventory() that updates an inventory dictionary based 
on a restock list. 
It accepts two parameters:

current_inventory: a dictionary where each key-value pair represents an item and 
its current stock in the inventory

restock_list: a dictionary where each key-value pair represents an item and the 
quantity to be added to the inventory
If an item in restock_list is not present in the current_inventory, it should be added.
The function should return the updated dictionary current_inventory.

Example Usage:

Example Input:

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}


Example Output:

current_inventory = {
    "apples": 40,
    "bananas": 15,
    "oranges": 30,
    "pears": 5
}

'''

'''

UPI - Understand

- Given two dictionaries, update one based on the values of 
the same items in the other 

UPI - Plan

- Loop through the two dictionaries
- If the keys match, add their values and set it to the current dictionary value

UPI - Impliment

'''

def restock_inventory(current_inventory, restock_list):
    for item in restock_list:
        if item in current_inventory:
            current_inventory[item] += restock_list[item]
        else:
            current_inventory[item] = restock_list[item] # if item not found in dictionary, add it to dictionary
    return current_inventory

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10            
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

print(restock_inventory(current_inventory, restock_list))