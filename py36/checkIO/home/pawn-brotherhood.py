"""思路：遍历给定的集合（set）里面的所有元素，然后转换为list。然后利用ord 和chr 转换求出该棋子左下和右下的棋子的位置坐标。
如果该坐标在原来的集合中，则num+1。最后返回num。
def safe_pawns(pawns):
    num=0
    for i in pawns:
        a=list(i)
        #b=a[0]+chr((ord(a[1])-1))
        c=chr(ord(a[0])-1)+chr((ord(a[1])-1))
        d=chr(ord(a[0])+1)+chr((ord(a[1])-1))
        if c in pawns or d in pawns:
            num+=1
    return num

def safe_pawns(pawns):
    def is_safe(p):
        file, rank = ord(p[0]), int(p[-1])
        return (chr(file-1)+str(rank-1) in pawns or 
                chr(file+1)+str(rank-1) in pawns)
        
    return sum(is_safe(p) for p in pawns)
""" 


def safe_pawns(pawns):
    answer = 0
    for pawn in pawns :
        if chr(ord(pawn[0])-1)+str(int(pawn[1])-1) in pawns or chr(ord(pawn[0])+1)+str(int(pawn[1])-1) in pawns : answer +=1
    return answer
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
