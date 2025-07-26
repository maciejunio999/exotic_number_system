def binary_to_decimal(n: str):
    result = 0
    i = 0
    l = len(n)
    while l > i:
        if n[l-1-i] == '1':
            result += 2**i
        elif n[l-1-i] == '0':
            pass
        else:
            print('Wrong number!')
            break
        i += 1
    return result

def decimal_to_binary(n: int):
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result
