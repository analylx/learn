"""
sorted(iterable, *, key=None, reverse=False) 
Return a new sorted list from the items in iterable.
"""

def bigger_price(limit, data):  
    result=[]      
    #传入的data是一个数组，其中的每个元素都是一个字典的类型，lambda中的x就是传入的字典值，获取key（“price”）的值来作为关键字排序
    data=sorted(data, key=lambda x: x['price'], reverse=True)
    for i in range(limit):
        result.append(data[i])
    return result
    #    return sorted(data, key=lambda x:x["price"], reverse=True)[0:limit] #一行代码就搞定了，最简洁的答案了

if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
