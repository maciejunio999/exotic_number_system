def binary_to_decimal_hornet_function(binary: str):
    decimal = 1
    for i in range(len(binary) - 1):
        decimal = decimal * 2 + int(binary[i + 1])
    return decimal