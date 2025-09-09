def binary_to_decimal_loops_function(binary_str: str):
    binary = int(binary_str) # unfortunately i dont know how to overcome this with my latest refactoring, so this function will have a bit harder time
    decimal, p = 0, 0
    while binary:
        decimal += (binary % 10) * (2 ** p)
        binary //= 10
        p += 1
    return decimal