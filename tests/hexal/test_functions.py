###########################################################################################################################################
# test this will tell us which approach will be faster, if variables placed inside of the fuction or additional function
# in both cases we are trying to determin what type of value we want to get

# there are 4 different functions and each one has different approach to the problem
# first one uses for loop and math to determin reults
# second one is using int() function to get output
# third one is is using while loop
# fourth is with literal_eval function from asc library

import time
import numpy as np
import matplotlib.pyplot as plt

from for_loop_function import hexal_to_decimal as hexal_to_decimal_for_loop_function
from int_function import hexal_to_decimal as hexal_to_decimal_int_function
from while_loop_function import hexal_to_decimal as hexal_to_decimal_while_loop_function
from literal_eval import hexal_to_decimal as hexal_to_decimal_literal_eval

variables = ['9', '28', '32', '3B', '2CA', '41A', '576', '77C', '859', 'A28']
#            9     40    50    59    714    1050   1398  1916   2137   2600
times = 30

results = {
    'hexal_to_decimal_for_loop_function': [],
    'hexal_to_decimal_int_function': [],
    'hexal_to_decimal_while_loop_function': [],
    'hexal_to_decimal_literal_eval': []
}

for i in range(0,times):
    start = time.time()
    for variable in variables:
        print(f'hexal number: {variable}, in decimal by hexal_to_decimal_for_loop_function = {hexal_to_decimal_for_loop_function(variable)}')
    end = time.time()
    duration = end - start
    results['hexal_to_decimal_for_loop_function'].append(duration)

for i in range(0,times):
    start = time.time()
    for variable in variables:
        print(f'hexal number: {variable}, in decimal by hexal_to_decimal_int_function = {hexal_to_decimal_int_function(variable)}')
    end = time.time()
    duration = end - start
    results['hexal_to_decimal_int_function'].append(duration)

for i in range(0,times):
    start = time.time()
    for variable in variables:
        print(f'hexal number: {variable}, in decimal by hexal_to_decimal_while_loop_function = {hexal_to_decimal_while_loop_function(str(variable))}')
    end = time.time()
    duration = end - start
    results['hexal_to_decimal_while_loop_function'].append(duration)

for i in range(0,times):
    start = time.time()
    for variable in variables:
        print(f'hexal number: {variable}, in decimal by hexal_to_decimal_literal_eval = {hexal_to_decimal_literal_eval(variable)}')
    end = time.time()
    duration = end - start
    results['hexal_to_decimal_literal_eval'].append(duration)

average_results = {}
for i in results:
   average_results[i] = np.average(results[i])

