import pysnooper
# 检查是否存在不成对的括号
@pysnooper.snoop()
def checkio(Expression):
    'Check expression for correct brackets order'
    # 过滤出所有的括号
    x = "".join(_ for _ in Expression if _ in "{}()[]")
    # 3种括号任意一种只要没有替换完的，就持续循环。替换成对出现的括号
    while ("()" in x) or ("[]" in x) or ("{}" in x):
        x = x.replace("()", "")
        x = x.replace("{}", "")
        x = x.replace("[]", "")
    return len(x) == 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
