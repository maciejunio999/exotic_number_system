def decimal_to_binary_recursion(decimal):
    if decimal == 0:
        return "0"
    if decimal == 1:
        return "1"
    return decimal_to_binary_recursion(decimal // 2) + str(decimal % 2)
