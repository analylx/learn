import re
def popular_words(text: str, words: list) -> dict:
    dic= {}
    #返回全部相匹配字符串.\b  表示匹配单词边界前面再加一个\来转义
    for n in range(len(words)):
         dic[words[n]]=len(re.findall("\\b"+words[n]+"\\b",text.lower()))
    return dic

if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")


"""
def popular_words(text: str, words: list) -> dict:
    # your code here
    text = text.replace("\n"," ")
    text_list = list(map(lambda x: x.lower(),text.split(" ")))
    print(text_list)
    result_dict = {i:0 for i in words}
    for i in words:
        for a in range(0,len(text_list)):
            if text_list[a] == i:
                result_dict[i] += 1
    return result_dict

def popular_words(text: str, words: list) -> dict:
    # your code here
    splitted_words = text.lower().split()
    answer={}
    for i in words:
        if i in splitted_words:
            answer[i] = splitted_words.count(i)
        else:
            answer[i] = 0

    return answer

"""
