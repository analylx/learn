def between_markers(text: str, begin: str=None, end: str=None) -> str:
    """
        returns substring between two given markers
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:
The initial and final markers are always different.
If there is no initial marker then the beginning should be considered as the beginning of a string.
If there is no final marker then the ending should be considered as the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker is standing in front of the initial one then return an empty string.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
Output: A string.
Precondition: can't be more than one final marker and can't be more than one initial
1.先过滤特殊条件，没有begin个end的直接返回
2.将begin的最后的位置和end的初始位置计算出来，用于后面的切片.str[1:3]表示1和2两个索引的元素，不包括索引3

    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]
    """
    if begin == None and end == None:
        return text
    if text.find(begin)== -1 and text.find(end)==-1:
        return text
    #find()返回字符串第一次出现位置的索引，没找到返回-1
    if begin == None or text.find(begin)== -1:
        return text[0:text.find(end)]
    if end == None or text.find(end)==-1:
        return text[text.find(begin)+len(begin):]
    st = text.find(begin)+len(begin)
    en = text.find(end)
    if en <= st:
        return ''
    #print("test temp is :",text[st:en],begin,end)
    return text[st:en]

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')