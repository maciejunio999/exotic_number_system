###########################################################################################################################################
# test this will tell us which approach will be faster, if variables placed inside of the fuction or additional function
# in both cases we are trying to determin what type of value we want to get

# two functions with two different type of build in variables
# FIRST on is with two lists, SECOND one with one dictionary
#                     but also
# two functions which call another function to determin the value
# FIRST function has bunch of if's inside, SECOND has swich case in it

import time
import numpy as np
import matplotlib.pyplot as plt

from tests.roman.function_with_dictionary import roman_to_decimal_dictionary_function
from tests.roman.function_with_lists import roman_to_decimal_list_function
from tests.roman.if_function import roman_to_decimal_if_function
from tests.roman.switch_function import roman_to_decimal_switch_function

variables = ['IX', 'XL', 'L', 'LIX', 'DCCXIV', 'ML', 'MCCCXCVIII', 'MCMXVI', 'MMCXXXVII', 'MMDC']
times = 30

results = {
    'roman_to_decimal_switch_function': [],
    'roman_to_decimal_if_function': [],
    'roman_to_decimal_dictionary_function': [],
    'roman_to_decimal_list_function': []
}

for i in range(0,times):
    start = time.time()
    for variable in variables:
        print(f'roman number: {variable}, in decimal by roman_to_decimal_switch_function = {roman_to_decimal_switch_function(variable)}')
    end = time.time()
    duration = end - start
    results['roman_to_decimal_switch_function'].append(duration)

for i in range(0,times):
    start = time.time()
    for variable in variables:
        print(f'roman number: {variable}, in decimal by roman_to_decimal_if_function = {roman_to_decimal_if_function(variable)}')
    end = time.time()
    duration = end - start
    results['roman_to_decimal_if_function'].append(duration)

for i in range(0,times):
    start = time.time()
    for variable in variables:
        print(f'roman number: {variable}, in decimal by roman_to_decimal_dictionary_function = {roman_to_decimal_dictionary_function(variable)}')
    end = time.time()
    duration = end - start
    results['roman_to_decimal_dictionary_function'].append(duration)

for i in range(0,times):
    start = time.time()
    for variable in variables:
        print(f'roman number: {variable}, in decimal by roman_to_decimal_list_function = {roman_to_decimal_list_function(variable)}')
    end = time.time()
    duration = end - start
    results['roman_to_decimal_list_function'].append(duration)

average_results = {}
for i in results:
   average_results[i] = np.average(results[i])

average_results = dict(sorted(average_results.items(), key=lambda x: x[1]))
labels = list(average_results.keys())
values = list(average_results.values())

plt.figure(figsize=(10, 5))
plt.bar(labels, values)
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania funkcji (bezwzględna wartość)')
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

average_results_db = {k: 10 * np.log10(v) for k, v in average_results.items()}
labels_db = list(average_results_db.keys())
values_db = list(average_results_db.values())

plt.figure(figsize=(10, 5))
plt.bar(labels_db, values_db)
plt.ylabel('Różnica względem najszybszego (dB)')
plt.title('Różnice czasów wykonania w skali decybelowej')
plt.ylim(-35, -30)
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()