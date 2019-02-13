"""
roman_values = (('I',1), ('IV',4), ('V',5), ('IX',9),('X',10),('XL',40),('L',50),('XC',90),('C',100),
                    ('CD', 400), ('D', 500), ('CM', 900), ('M',1000))
 
def roman_value(roman):
    total=0
    for symbol,value in reversed(roman_values):
        while roman.startswith(symbol):
            total += value
            roman = roman[len(symbol):]
    return total
"""

elements = { 1000 : 'M', 900 : 'CM', 500 : 'D', 400 : 'CD', 
             100 : 'C', 90 : 'XC', 50 : 'L', 40: 'XL', 
             10 : 'X', 9 : 'IX', 5 : 'V', 4: 'IV', 1 : 'I' }
              
def checkio(data):
    roman = ''
    for n in sorted(elements.keys(), reverse=True):
        while data >= n:
            roman += elements[n]
            data -= n
            print(data,roman)
    return roman
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')