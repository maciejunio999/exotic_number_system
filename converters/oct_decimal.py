def octal_to_decimal(octal):
    if octal == 0:
        return 0
    else:
        return (octal % 10) + 8 * octal_to_decimal(octal // 10)
