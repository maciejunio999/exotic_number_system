###########################################################################################################################################
# test this will tell us which approach will be faster, if variables placed inside of the fuction or additional function
# in both cases we are trying to determin what type of value we want to get

# there are 4 different functions and each one has different approach to the problem
# first one uses table with values that helps it determin reults
# second one is based on pure math and counting outcome
# third one is just predefined python function
# fourth is based on recursion

import time
import numpy as np
import matplotlib.pyplot as plt

from convert_with_table import octal_to_decimal as octal_to_decimal_convert_with_table
from counting import octal_to_decimal as octal_to_decimal_counting
from predefined import octal_to_decimal as octal_to_decimal_predefined
from recursion import octal_to_decimal as octal_to_decimal_recursion

variables = [11, 50, 62, 73, 1312, 2032, 2566, 3574, 4131, 5050]
#            9   40  50  59  714   1050  1398  1916  2137  2600
times = 30

results = {
    'octal_to_decimal_convert_with_table': [],
    'octal_to_decimal_counting': [],
    'octal_to_decimal_predefined': [],
    'octal_to_decimal_recursion': []
}

for i in range(0,times):
    start = time.time()
    for variable in variables:
        print(f'octal number: {variable}, in decimal by octal_to_decimal_convert_with_table = {octal_to_decimal_convert_with_table(variable)}')
    end = time.time()
    duration = end - start
    results['octal_to_decimal_convert_with_table'].append(duration)

for i in range(0,times):
    start = time.time()
    for variable in variables:
        print(f'octal number: {variable}, in decimal by octal_to_decimal_counting = {octal_to_decimal_counting(variable)}')
    end = time.time()
    duration = end - start
    results['octal_to_decimal_counting'].append(duration)

for i in range(0,times):
    start = time.time()
    for variable in variables:
        print(f'octal number: {variable}, in decimal by octal_to_decimal_predefined = {octal_to_decimal_predefined(str(variable))}')
    end = time.time()
    duration = end - start
    results['octal_to_decimal_predefined'].append(duration)

for i in range(0,times):
    start = time.time()
    for variable in variables:
        print(f'octal number: {variable}, in decimal by octal_to_decimal_recursion = {octal_to_decimal_recursion(variable)}')
    end = time.time()
    duration = end - start
    results['octal_to_decimal_recursion'].append(duration)

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