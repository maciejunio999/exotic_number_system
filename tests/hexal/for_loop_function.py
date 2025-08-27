def hexal_to_decimal(hex):
    ref = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
       'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    
    r = 0
    s = len(hex) - 1
    
    for num in hex:
        r = r + ref[num] * 16 ** s
        s = s - 1
    
    return r