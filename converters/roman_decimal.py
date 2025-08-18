def roman_to_decimal_list_function(str):
    result = 0
    i = 0

    roman_dictionary = [
        'I',
        'V',
        'X',
        'L',
        'C',
        'D',
        'M'
        ]
    decimal_dictionary = [
        1,
        5,
        10,
        50,
        100,
        500,
        1000
    ]
    

    while (i < len(str)):
        # Getting value of symbol s[i]
        index_for_s1 = roman_dictionary.index(str[i])
        s1 = decimal_dictionary[index_for_s1]

        if (i + 1 < len(str)):
            # Getting value of symbol s[i + 1]
            index_for_s2 = roman_dictionary.index(str[i + 1])
            s2 = decimal_dictionary[index_for_s2]

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