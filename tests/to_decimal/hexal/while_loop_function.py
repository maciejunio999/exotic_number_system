def hexal_to_decimal_while_loop_function(number: str):
    hex = number.strip().upper( )
    l = count = i = 0
    s = len(hex) - 1
    while s >= 0:
        if hex[s] >= '0' and hex[s] <= '9':
            r = int(hex[s])
        elif hex[s] >= 'A' and hex[s] <= 'F':
            r = ord(hex[s]) - 55
        else:
            l = 1
            break
        count = count + (r * 16 ** i)
        s = s - 1
        i = i + 1 
    if l == 0:
        return count
    else:
        print('Incorrect input')
