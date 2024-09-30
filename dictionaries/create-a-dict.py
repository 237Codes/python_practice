'''

Write a function create_dictionary() that takes in a list of keys 
and a list of values as parameters. The function returns a dictionary 
where each item in keys is paired with a corresponding item in values.

keys[i] should be paired with values[i] in the dictionary where 
0 <= i <= len(keys). You may assume keys and values are the same length.

Example Input:

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]

Example Output:

# {"peanut": "butter", "dragon": "fly", "star": "fish", "pop": "corn", "space": "ship"}

'''

'''

UPI - Understand

- Given alist of keys  and a list of values
- return a dictionary which pairs each item in keys with each corresponding
item in values list 
- Two lists are assumed to be the dame length

UPI - Plan

- loop through keys and values vlists and add the key, value to the dictionary
- return a dictionary

UPI - Impliment

'''

def create_dictionary(keys, values):
    dict = {}
    for key, value in zip(keys, values):
        dict[key] = value
    return dict


def test_create_dictionary():
    # Test case 1: Normal case
    keys = ["peanut", "dragon", "star", "pop", "space"]
    values = ["butter", "fly", "fish", "corn", "ship"]
    expected_output = {
        "peanut": "butter",
        "dragon": "fly",
        "star": "fish",
        "pop": "corn",
        "space": "ship"
    }
    assert create_dictionary(keys, values) == expected_output

    # Test case 2: Empty keys and values
    keys = []
    values = []
    expected_output = {}
    assert create_dictionary(keys, values) == expected_output

    # Test case 3: Keys with one element, values with one element
    keys = ["one"]
    values = ["1"]
    expected_output = {"one": "1"}
    assert create_dictionary(keys, values) == expected_output

    # Test case 4: Keys with more elements than values
    keys = ["one", "two"]
    values = ["1"]
    expected_output = {"one": "1"}
    assert create_dictionary(keys, values) == expected_output

    # Test case 5: Values with more elements than keys
    keys = ["one"]
    values = ["1", "2"]
    expected_output = {"one": "1"}
    assert create_dictionary(keys, values) == expected_output

    # Test case 6: Keys and values with different data types
    keys = [1, 2, 3]
    values = ["one", "two", "three"]
    expected_output = {1: "one", 2: "two", 3: "three"}
    assert create_dictionary(keys, values) == expected_output

    # Test case 7: Keys with duplicate elements
    keys = ["one", "one"]
    values = ["1", "2"]
    expected_output = {"one": "2"}
    assert create_dictionary(keys, values) == expected_output

    # Test case 8: Values with duplicate elements
    keys = ["one", "two"]
    values = ["1", "1"]
    expected_output = {"one": "1", "two": "1"}
    assert create_dictionary(keys, values) == expected_output

    # Test case 9: Keys with None value
    keys = [None, "two"]
    values = ["1", "2"]
    expected_output = {None: "1", "two": "2"}
    assert create_dictionary(keys, values) == expected_output

    # Test case 10: Values with None value
    keys = ["one", "two"]
    values = [None, "2"]
    expected_output = {"one": None, "two": "2"}
    assert create_dictionary(keys, values) == expected_output

# Run the test cases
test_create_dictionary()
print("All test cases passed!")