###########################################################################################################################################
# test this will tell us which approach will be faster, if variables placed inside of the fuction or additional function
# in both cases we are trying to determin what type of value we want to get

# two functions with two different type of build in variables
# FIRST on is with two lists, SECOND one with one dictionary
#                     but also
# two functions which call another function to determin the value
# FIRST function has bunch of if's inside, SECOND has swich case in it

from utils.exotic_to_decimal_testing import exotic_to_decimal_testing

from to_decimal.roman.function_with_dictionary import roman_to_decimal_dictionary_function
from to_decimal.roman.function_with_lists import roman_to_decimal_list_function
from to_decimal.roman.if_function import roman_to_decimal_if_function
from to_decimal.roman.switch_function import roman_to_decimal_switch_function

roman_variables = ['IX', 'XL', 'L', 'LIX', 'DCCXIV', 'ML', 'MCCCXCVIII', 'MCMXVI', 'MMCXXXVII', 'MMDC']
roman_functions = [roman_to_decimal_dictionary_function, roman_to_decimal_list_function, roman_to_decimal_if_function, roman_to_decimal_switch_function]

octal_variables = [11, 50, 62, 73, 1312, 2032, 2566, 3574, 4131, 5050]
#                  9   40  50  59  714   1050  1398  1916  2137  2600
iterations = 30

exotic_to_decimal_testing(roman_functions, roman_variables, iterations)