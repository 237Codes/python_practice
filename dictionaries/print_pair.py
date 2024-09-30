'''

Write a function print_pair() that takes in a dictionary
dictionary and a key target as parameters. The function 
looks for the target and when found, it prints the key and 
it's associated value as "Key: <key>" followed by "Value: <value>". 
If target is not in dictionary, print "That pair does not exist!".


Example Usage:

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")

'''

'''

UPI - Understand

- Given a dictionary and a key target
- Look for the key in the dictionary, when found  print the key and its associated value
- If the target is not in the dictionary, print "pair does not exist"

UPI - Plan

- Loop through the dictionary and look if a key is there
- If we see the key, print the key and its value
- If we dont see the key, return "That pair does not exist"

UPI - Impliment

'''

def print_pair(dictionary, target_key):
    for key in dictionary:
        if key == target_key:
            print(f"Key: {key}", f"Value: {dictionary[key]}")
    if target_key not in dictionary:
        print("Pair does not exist")
            


dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")