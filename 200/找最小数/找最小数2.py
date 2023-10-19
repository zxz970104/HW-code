
s = input()

n = int(input())

def solve(s, n):
    stack = []
    for c in s:
        # 弹出所有比当前元素大的栈顶元素
        while n > 0 and stack and stack[-1] > c:
            stack.pop()
            n -= 1
        
        stack.append(c)
    return ''.join(stack)

print(solve(s, n))