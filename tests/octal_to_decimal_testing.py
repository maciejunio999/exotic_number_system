###########################################################################################################################################
# test this will tell us which approach will be faster, if variables placed inside of the fuction or additional function
# in both cases we are trying to determin what type of value we want to get

# there are 4 different functions and each one has different approach to the problem
# first one uses table with values that helps it determin reults
# second one is based on pure math and counting outcome
# third one is just predefined python function
# fourth is based on recursion

from utils.exotic_to_decimal_testing import exotic_to_decimal_testing

from octal.convert_with_table import octal_to_decimal_with_dictionary
from octal.counting import octal_to_decimal_using_math
from octal.predefined import octal_to_decimal_predefined_function
from octal.recursion import octal_to_decimal_using_recursion

octal_functions = [octal_to_decimal_with_dictionary, octal_to_decimal_using_math, octal_to_decimal_predefined_function, octal_to_decimal_using_recursion]
octal_variables = [11, 50, 62, 73, 1312, 2032, 2566, 3574, 4131, 5050]
#                  9   40  50  59  714   1050  1398  1916  2137  2600
iterations = 30

exotic_to_decimal_testing(octal_functions, octal_variables, iterations)