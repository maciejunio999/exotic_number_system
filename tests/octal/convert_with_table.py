def octal_to_decimal(n):
    # Define a dictionary to map octal digits to their decimal equivalents
    lookup = {
        0: 0, 1: 1, 2: 2, 3: 3,
        4: 4, 5: 5, 6: 6, 7: 7
    }
    
    decimal = 0
    base = 1
    
    # Convert octal to decimal
    while n > 0:
        last_digit = n % 10  # Get the last digit of the octal number
        decimal += lookup[last_digit] * base  # Add the decimal equivalent to the result
        n //= 10  # Remove the last digit from the octal number
        base *= 8  # Move to the next octal place value (8^0, 8^1, 8^2, ...)
    
    return decimal
