def binary_to_decimal(binary: str):
    for i in range(len(binary) - 1):
        decimal = decimal * 2 + int(binary[i + 1])
    return decimal