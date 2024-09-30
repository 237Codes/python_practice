'''

Write a function keys_v_values() that takes in a dictionary dictionary whose 
keys and values are both integers. The function should find the sum of all keys 
in the dictionary and the sum of all values.
If the sum of all keys is greater than the sum of all values, the function should 
return the string "keys". 
If the sum of all values is greater than the sum of all keys,
the function should return the string "values".
If keys and values have equal sums, the function should return the string "balanced".

Example Usage:

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

'''

'''

UPI - Understand

- Given a dictionary whose keys and values are both integers
- Sum all the keys in the dictionary
- sum all the values in the dictionary
- return a string based on the condition between the keys and the values sum 

UPI - Plan

- Get the list of keys and sum it 
- Get a list of values and sum it 
- Check the condition and retun the appriopriate string 

UPI - Impliment

'''

def keys_v_values(dictionary):
    sum_keys = 0
    sum_values = 0
    
    keys = dictionary.keys()
    values = dictionary.values()

    sum_keys += sum(keys)
    sum_values += sum(values)

    if sum_keys > sum_values:
        return "Keys"
    elif sum_keys < sum_values:
        return "Values"
    else:
        return "Balanced"
    
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)