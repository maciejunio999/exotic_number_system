from ast import literal_eval   

def hexal_to_decimal(hex: str):
    h = '0x' + hex
    return literal_eval(h) 
