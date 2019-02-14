# -*- coding: utf-8 -*-
"""
状态机是关于设计程序来控制应用程序中的流程。 它是一个有向图，由一组节点和一组过渡函数组成。 处理文本文件通常包括顺序读取文本文件的每个块并执行某些操作以响应每个块读取。 块的含义取决于它之前存在的块的类型以及它之后的块。 该机器是关于设计程序来控制应用程序中的流程。 它是一个有向图，由一组节点和一组过渡函数组成。 处理文本文件通常包括顺序读取文本文件的每个块并执行某些操作以响应每个块读取。 块的含义取决于它之前存在的块的类型以及它之后的块。考虑有一种情况，其中文本放置必须是AGC序列的重复连续串(用于蛋白质分析)。 如果在输入字符串中保持此特定序列，则机器的状态保持为TRUE，但是一旦序列偏离，机器的状态将变为FALSE并且在之后保持为FALSE。 这确保了即使稍后可能存在更多正确序列的块，也停止进一步处理。下面的程序定义了一个状态机，它具有启动机器的功能，获取处理文本的输入并逐步完成处理。
"""


class StateMachine:
    def start(self):
        self.state = self.startState

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    def feeder(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]


class TextSeq(StateMachine):
    startState = 0

    def getNextValues(self, state, inp):
        if state == 0 and inp == 'A':
            return (1, True)
        elif state == 1 and inp == 'G':
            return (2, True)
        elif state == 2 and inp == 'C':
            return (0, True)
        else:
            return (3, False)


Inseq = TextSeq()
x = Inseq.feeder(['A', 'A', 'A'])
print(x)
y = Inseq.feeder(['A', 'G', 'C', 'A', 'C', 'A', 'G'])
print(y)
