def decimal_to_binary_mathematical(decimal):
    binary= ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary