def binary_to_decimal(binary: int):
    decimal, p = 0, 0
    while binary:
        decimal += (binary % 10) * (2 ** p)
        binary //= 10
        p += 1
    return decimal