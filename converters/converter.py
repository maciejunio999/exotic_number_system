from hex_decimal import hex_to_decimal
from binary_decimal import binary_to_decimal
from oct_decimal import octal_to_decimal
from roman_decimal import roman_to_decimal

def conversion(coversion, number):
    match coversion:
        case 'hex_dec':
            return hex_to_decimal(number)
        case 'bin_dec':
            return binary_to_decimal(number)
        case 'oct_dec':
            return octal_to_decimal(int(number))
        case 'rom_dec':
            return roman_to_decimal(number)

def convert(number: str, from_system: str, to_system: str):
    return 'convert'