from types import *

M = int(input())

N = 100

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def solve(M:int) -> int:
    if M < 1 or M > N:
        return None
    
    # 构建循环链表
    head = Node(1)
    cur = head
    for i in range(2, N + 1):
        cur.next = Node(i)
        cur = cur.next
    cur.next = head

    # 从头节点开始报数
    cur = head
    while True:
        # 循环结束时cur则为需要报M-1的节点
        for i in range(M - 2):
            cur = cur.next

        # 断开第M个节点
        cur.next = cur.next.next
        cur = cur.next

        # 停止条件可以是第M-1次报数又回到了第一次报数的节点
        if cur == head:
            break
        else:
            head = cur

    # 构建结果列表
    res = []
    for i in range(M-1):
        res.append(cur.val)
        cur = cur.next
    return res
    

res = solve(M)
if res == None:
    print("ERROR!")
else:
    print(res)
