#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        max_val = max(a_dictionary.keys(), key=(lambda x: a_dictionary[x]))
        return (a_dictionary[max_val])
    return None
