###########################################################################################################################################
# there are 4 different functions and each one has different approach to the problem
# first one does the conversion with while loop and does it bit by bit
# second one uses math approach
# third one is with recursion
# fourth one uses build in format function

from utils.exotic_to_decimal_testing import exotic_to_decimal_testing

from to_exotic.binary.bit_by_bit_function import decimal_to_binary_bit_by_bit
from to_exotic.binary.mathematical_function import decimal_to_binary_mathematical
from to_exotic.binary.recursion import decimal_to_binary_recursion
from to_exotic.binary.format_function import decimal_to_binary_format

binary_functions = [decimal_to_binary_bit_by_bit, decimal_to_binary_mathematical, decimal_to_binary_recursion, decimal_to_binary_format]
# '1001', '101000', '110010', '111011', '1011001010', '10000011010', '10101110110', '11101111100', '100001011001', '101000101000']
decimal_variables = [9, 40, 50, 59, 714, 1050, 1398, 1916, 2137, 2600]
iterations = 30

exotic_to_decimal_testing(binary_functions, decimal_variables, iterations)