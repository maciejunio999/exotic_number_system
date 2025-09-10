###########################################################################################################################################
# test this will tell us which approach will be faster, if variables placed inside of the fuction or additional function
# in both cases we are trying to determin what type of value we want to get

# there are 4 different functions and each one has different approach to the problem
# first one uses for loop and math to determin reults
# second one is using int() function to get output
# third one is is using while loop
# fourth is with literal_eval function from asc library

from utils.exotic_to_decimal_testing import exotic_to_decimal_testing

from to_exotic.binary.bit_by_bit_function import decimal_to_binary_bit_by_bit
from to_exotic.binary.mathematical_function import decimal_to_binary_mathematical
from to_exotic.binary.recursion import decimal_to_binary_recursion

binary_functions = [decimal_to_binary_bit_by_bit, decimal_to_binary_mathematical, decimal_to_binary_recursion]
# '1001', '101000', '110010', '111011', '1011001010', '10000011010', '10101110110', '11101111100', '100001011001', '101000101000']
decimal_variables = [9, 40, 50, 59, 714, 1050, 1398, 1916, 2137, 2600]
iterations = 30

exotic_to_decimal_testing(binary_functions, decimal_variables, iterations)