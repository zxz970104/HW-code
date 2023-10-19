from typing import *
from collections import deque
class Node:
    def __init__(self, comment : str = "", children: List["Node"] = None) -> None:
        self.comment = comment
        self.children = children if children else []

inp = input().split(",")
root = Node()


class Solution:
    def __init__(self, inp) -> None:
        self.comments = inp
        self.idx = 0
        self.root = Node()

    def trace(self, cur):
        self.idx += 1
        n = int(self.comments[self.idx])
        # 处理当前评论的n个子评论
        for _ in range(n):
            self.idx += 1
            cur.children.append(Node(self.comments[self.idx]))
            self.trace(cur.children[-1])

    def solve(self):
        # 由于根评论不清楚有几条，需要通过idx来获取
        while self.idx < len(self.comments):
            self.root.children.append(Node(self.comments[self.idx]))
            self.trace(self.root.children[-1])
            self.idx += 1


s = Solution(inp)
s.solve()

print(s.root)
def levelOrder(root):

    q = deque()
    q.append(root)
    res = []
    while q:
        n = len(q)
        tmp = []
        for _ in range(n):
            node = q.popleft()
            for item in node.children:
                tmp.append(item.comment)
                q.append(item)
        if tmp:
            res.append(tmp)

    return res
res = levelOrder(s.root)
print(len(res))
for item in res:
    print(" ".join(item))
            

# A,3,B,2,C,0,D,1,E,0,F,1,G,0,H,1,I,1,J,0,K,1,L,0,M,2,N,0,O,1,P,0