#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    largest_value = max(a_dictionary, key=a_dictionary.get)
    return (largest_value)
