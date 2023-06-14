#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        x = max(list(a_dictionary.values()))
        for i, v in a_dictionary.items():
            if v == x:
                return i
