import sys
"""
This post is targeted towards aspiring "python programmers".

Code in python usually looks elegant and clear. "High-readability" is one of the reasons behind its growing popularity. Though, at times, you'll find python-version of code looking worse. This mostly happens if the code is written by inexperienced python programmer (usually coming from other languages). For such times, I encourage you to find the "pythonic way" of coding it instead of using "plain translation from other languages". It will surely benefit you in the long run.

Just to give an example, a pythonista would always use while queue: instead of while queue != None :, former being far clear and concise. I hope this post gives some tips regarding "python-way" of coding and encourages you to find better ways to code.
"""
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        queue = [root] if root else []
        while queue:
            node = queue.pop()
            print(node.data, end=" ")
            if node.left: queue.insert(0,node.left)
            if node.right: queue.insert(0,node.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)