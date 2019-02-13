#反转字典 即key和val互换,然后用max获取反转后的最大键值，这个最大值的值就是所要求的
def invert_dict(d):
    return dict((v,k) for k,v in d.items()) 

def best_stock(data):
    rdata= invert_dict(data)
    return rdata[max(rdata.keys())]


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")