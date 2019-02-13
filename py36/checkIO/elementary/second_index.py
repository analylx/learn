def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
        通过判断从1开始的每个切片是否包含2个symbol，并且输出第一个包含两个symbol的切片长度-1做为位置
    """
    #range返回的是从0开始的数组，所以要从n+1开始
    for n in range(len(text)):
        if text[0:n+1].count(symbol)==2:
            return len(text[0:n+1])-1
    return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
