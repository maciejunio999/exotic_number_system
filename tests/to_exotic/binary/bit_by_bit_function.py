def decimal_to_binary_bit_by_bit(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal & 1) + binary
        decimal >>= 1
    return binary