from converters import converter
from calculator import calculate

def main_function():
    while True:
        x = input('For Conversion mode type "Con", for Calculator mode type "Cal"\nWhich operation? ')
        if x == "Con":
            converter.conversion()
            break
        elif x == "Cal":
            calculate()
            break
        else:
            print('Passed wrong value!')
            pass

if __name__ == '__main__':
    main_function()