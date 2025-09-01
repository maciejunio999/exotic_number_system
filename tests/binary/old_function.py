def binary_to_decimal(binary: str):
    decimal = 0
    i = 0
    l = len(binary)
    while l > i:
        if binary[l - 1 - i] == '1':
            decimal += 2 ** i
        elif binary[l - 1 - i] == '0':
            pass
        else:
            print('Wrong number!')
            break
        i += 1
    return decimal
