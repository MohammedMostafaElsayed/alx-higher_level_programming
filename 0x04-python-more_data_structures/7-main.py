#!/usr/bin/python3
u = __import__('7-update_dictionary').update_dictionary
p = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = u(a, 'language', "Python")
p(new_dict)
print("--")
p(a)

print("--")
print("--")

new_dict = u(a, 'city', "San Francisco")
p(new_dict)
print("--")
p(a)