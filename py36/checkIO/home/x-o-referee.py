"""
#对三行三列两个对角线8种可能进行判断是否等于”XXX”或者”OOO”,我的解题是将八种可能的单个字符进行比较
def checkio(game_result):
    #行判断,可以一条式子走下来不需要与或非连接符。
    #一个字符串可以当作一个不可变的列表，也就是说game_result本身就是一个二维数组。可以先写出每个位置的坐标值或者坐标函数
    for row in game_result:
        if row[0] == row[1] == row[2] != ".":
            return row[0]
    #列判断
    for col in range(3):
        if game_result[0][col] == game_result[1][col] == game_result[2][col] != ".":
            return game_result[0][col]            
    #对角线判断
    if game_result[0][0] == game_result[1][1] == game_result[2][2] != ".":
        return game_result[1][1]
    if game_result[2][0] == game_result[1][1] == game_result[0][2] != ".":
        return game_result[1][1]
    return "D"

#看懂并写出思路
def checkio(board):
    # First we put everything together into a single string
    x = "".join(board)   
    # Next we outline the 8 possible winning combinations. 
    combos = ["012", "345", "678", "036", "147", "258", "048", "246"]   
    # We go through all the winning combos 1 by 1 to see if there are any all Xs or all Os in the combos
    for i in combos:
        if x[int(i[0])] == x[int(i[1])] == x[int(i[2])] and x[int(i[0])] in "XO":
            return x[int(i[0])]
    return "D" 
    
#用zip()和map()函数拼接列和对角线字符串
def checkio(result):
    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)
    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'

#用切片的方式得到列和对角线的字符串
def checkio(game_result):
    sample = "".join(game_result)
    data=game_result + [sample[i:9:3] for i in range(3)] + [sample[0:9:4], sample[2:8:2]]
    if "OOO" in data:
        return "O"
    elif "XXX" in data:
        return "X"
    else:
        return "D"
"""

import re
def checkio(game_result):
    # join the array to one long string
    # row - search for 3 equal game characters next to each other: r"([OX])\1{2}"
    # column - search for 3 equal game characters separated by any 3 characters: r"([OX]).{3}\1.{3}\1"
    # diagonals - like a column, different offsets: r"([OX]).{4}\1.{4}\1" and r"([OX]).{2}\1.{2}\1" 
    res=re.search(r"([OX])(\1{2}|.{3}\1.{3}\1|.{4}\1.{4}\1|.{2}\1.{2}\1)","-".join(game_result))
    if res!=None: return res.group(0)[0]
    return "D"

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
