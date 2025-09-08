import time

def run_function_in_loop(times, variables, function):
    results = []
    for _ in range(0,times):
        start = time.time()
        for variable in variables:
            print(f'roman number: {variable}, in decimal by {function.__name__} = {function(variable)}')
        end = time.time()
        duration = end - start
        results.append(duration)
    
    return results