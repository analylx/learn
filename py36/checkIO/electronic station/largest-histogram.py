"""
参考codeganker的解法，首先，我们知道，在计算矩形时，对于索引i所对应的的柱状图，它一定是由它“生成的”矩形中最小的柱状图。那么我们在计算时，假设现在从i出发往左右搜索，找到左边第一个比heights[i]小的索引l，和右边第一个比heights[i]小的索引r，那么r和l之间就是我们要找的由索引i对应的柱状图生成的矩形区域。
现在对heights进行遍历，将柱状图的大小从小到大的顺序，将索引压栈，那么对于栈顶元素来说（假设其索引为cur），他对应的r即为当前遍历的位置，他对应的l则时他的上一个进栈的索引（有可能栈为空，则这个索引为-1），这样，计算过的索引弹栈，最终得到结果，最后为了计算最后一个元素的生成矩阵，我们在heights的末尾插入0，方便计算。
"""

def largest_histogram(histogram):
    result, width = 0, len(histogram) + 1
    for i in range(1, width):
        for j in range(width - i):
            rect = i * min(histogram[j:][:i])
            result = max(result, rect)
    return result
    
if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
