###########################################################################################################################################
# test this will tell us which approach will be faster, if variables placed inside of the fuction or additional function
# in both cases we are trying to determin what type of value we want to get

# two functions with two different type of build in variables
# FIRST on is with two lists, SECOND one with one dictionary
#                     but also
# two functions which call another function to determin the value
# FIRST function has bunch of if's inside, SECOND has swich case in it

import time

from function_with_dictionary import roman_to_decimal_dictionary_function
from function_with_lists import roman_to_decimal_list_function
from if_function import roman_to_decimal_if_function
from switch_function import roman_to_decimal_switch_function

variables = ['IX', 'XL', 'L', 'LIX', 'DCCXIV', 'ML', 'MCCCXCVIII', 'MCMXVI', 'MMCXXXVII', 'MMDC']

start = time.time()
for variable in variables:
    print(f'roman number: {variable}, in decimal by roman_to_decimal_switch_function = {roman_to_decimal_switch_function(variable)}')
end = time.time()
duration = end - start
print(f"Czas wykonania dla roman_to_decimal_switch_function: {duration:.6f} sekundy")
print('#'*15)

start = time.time()
for variable in variables:
    print(f'roman number: {variable}, in decimal by roman_to_decimal_if_function = {roman_to_decimal_if_function(variable)}')
end = time.time()
duration = end - start
print(f"Czas wykonania dla roman_to_decimal_if_function: {duration:.6f} sekundy")
print('#'*15)

start = time.time()
for variable in variables:
    print(f'roman number: {variable}, in decimal by roman_to_decimal_dictionary_function = {roman_to_decimal_dictionary_function(variable)}')
end = time.time()
duration = end - start
print(f"Czas wykonania dla roman_to_decimal_dictionary_function: {duration:.6f} sekundy")
print('#'*15)

start = time.time()
for variable in variables:
    print(f'roman number: {variable}, in decimal by roman_to_decimal_list_function = {roman_to_decimal_list_function(variable)}')
end = time.time()
duration = end - start
print(f"Czas wykonania dla roman_to_decimal_list_function: {duration:.6f} sekundy")
print('#'*15)
