from itertools import combinations
def longest_palindromic(text):
    subs = (text[start: end] for start, end in combinations(range(len(text) + 1), 2))
    return max((s for s in subs if s == s[::-1]), key=len)
#穷举法范围从大到小
def longest_palindromic2(text):
    s = len(text)
    for size in range(s)[::-1]:
        for index in range(s - size):
            word = text[index:index + size + 1]
            if word == word[::-1]:
                #print(word)
                return word    
                
if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    
    assert longest_palindromic2("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic2("abacada") == "aba", "The First"
    assert longest_palindromic2("aaaa") == "aaaa", "The A"
    #assert longest_palindromic2("100011110") == "1111", "num"