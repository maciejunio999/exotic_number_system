import numpy as np

from utils.draw_plot import draw_plot
from utils.run_choosen_function_in_loop import run_function_in_loop

def exotic_to_decimal_testing(functions_list, varaibles_list, iterations):
    average_results = {}

    for func in functions_list:
        average_results[func.__name__] = np.average(run_function_in_loop(iterations, varaibles_list, func))

    draw_plot(average_results, True)
    draw_plot(average_results)