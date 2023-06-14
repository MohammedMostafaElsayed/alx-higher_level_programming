#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        x = max(list(a_dictionary.values()))
        for i in a_dictionary:
            if a_dictionary[i] == x:
                break
    return i
