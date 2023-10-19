
s = input()

n = int(input())

def solve(s, n):
    stack = []
    for c in s:
        while n > 0 and stack and stack[-1] > c:
            stack.pop()
            n -= 1

        stack.append(c)
    return ''.join(stack)

print(solve(s, n))