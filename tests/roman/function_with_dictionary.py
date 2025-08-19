def roman_to_decimal_dictionary_function(str):
    result = 0
    i = 0

    dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    while (i < len(str)):
        # Getting value of symbol s[i]
        s1 = dictionary[str[i]]

        if (i + 1 < len(str)):
            # Getting value of symbol s[i + 1]
            s2 = dictionary[str[i + 1]]

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