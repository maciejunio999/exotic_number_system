###########################################################################################################################################
# test this will tell us which approach will be faster, if variables placed inside of the fuction or additional function
# in both cases we are trying to determin what type of value we want to get

# two functions with two different type of build in variables
# FIRST on is with two lists, SECOND one with one dictionary
#                     but also
# two functions which call another function to determin the value
# FIRST function has bunch of if's inside, SECOND has swich case in it

import numpy as np

from utils.draw_plot import draw_plot
from utils.run_choosen_function_in_loop import run_function_in_loop

from roman.function_with_dictionary import roman_to_decimal_dictionary_function
from roman.function_with_lists import roman_to_decimal_list_function
from roman.if_function import roman_to_decimal_if_function
from roman.switch_function import roman_to_decimal_switch_function

variables = ['IX', 'XL', 'L', 'LIX', 'DCCXIV', 'ML', 'MCCCXCVIII', 'MCMXVI', 'MMCXXXVII', 'MMDC']
times = 30
average_results = {}
functions = [roman_to_decimal_dictionary_function, roman_to_decimal_list_function, roman_to_decimal_if_function, roman_to_decimal_switch_function]

for func in functions:
    average_results[func.__name__] = np.average(run_function_in_loop(times, variables, func))

draw_plot(average_results, True)
draw_plot(average_results)