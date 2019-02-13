def checkio(number):
    l = ""
    if number>=1000:
        l+='M'*int(number/1000)
        number = number%1000
    if number<1000 and number>=900:
        l+='CM'
        number -=900
    if number<1000 and number>=500:
        l+='D'
        l+='C'*int(number/100-5)
        number = number%100
    if number<1000 and number>=400:
        l+="CD"
        number = number%100
    if number<1000 and number>=100:
        l+="C"*int(number/100)
        number = number%100
    if number<100 and number>=90:
        l+='XC'
        number -=90
    if number<100 and number>=50:
        l+='L'
        l+='X'*int(number/10-5)
        number = number%10
    if number<100 and number>=40:
        l+="XL"
        number = number%10
    if number<100 and number>=10:
        l+="X"*int(number/10)
        number = number%10
    if number<10 and number>=9:
        l+='IX'
    if number<9 and number>=5:
        l+='V'
        l+='I'*(number-5)
    if number==4:
        l+="IV"
    if number<4 and number>=1:
        l+="I"*number
    return l
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')