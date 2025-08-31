from ast import literal_eval   

def hexal_to_decimal(hex):
    h = '0x' + hex
    return literal_eval(h) 
