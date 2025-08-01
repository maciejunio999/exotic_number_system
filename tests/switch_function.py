def decimal_value(r):
    match r:
        case 'I':
            return 1
        case 'V':
            return 5
        case 'X':
            return 10
        case 'L':
            return 50
        case 'C':
            return 100
        case 'D':
            return 500
        case 'M':
            return 1000
        case _:
            return -1

def roman_to_decimal_switch_function(str):
    result = 0
    i = 0

    while (i < len(str)):
        # Getting value of symbol s[i]
        s1 = decimal_value(str[i])

        if (i + 1 < len(str)):
            # Getting value of symbol s[i + 1]
            s2 = decimal_value(str[i + 1])

            # Comparing both values , if current symbol is greater or equal to the next symbol
            if (s1 >= s2):
                result = result + s1
                i = i + 1
            else:
                result = result + s2 - s1
                i = i + 2
        else:
            result = result + s1
            i = i + 1

    return result