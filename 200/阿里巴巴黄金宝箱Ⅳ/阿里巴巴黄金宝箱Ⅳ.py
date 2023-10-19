
nums = [int(x) for x in input().split(',')]
n = len(nums)

res = [-1 for _ in range(n)]
stack = [] # 单调栈
for i in range((n << 1) - 1): # 总共需要遍历2n-1个数

    # 栈顶元素小于当前元素则出栈，即对应位置处后面第一个比他大的值
    while stack and nums[stack[-1]] < nums[i % n]:
        idx = stack.pop()
        res[idx] = nums[i % n]

    # 小于栈顶元素的入栈   
    stack.append(i % n)

print(res)


