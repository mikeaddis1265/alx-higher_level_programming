#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys of the dictionary alphabetically
    sorted_keys = sorted(a_dictionary.keys())
    
    # Iterate over the sorted keys
    for key in sorted_keys:
        # Print each key-value pair
        print(f"{key}: {a_dictionary[key]}")
