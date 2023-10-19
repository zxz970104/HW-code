
nums = [int(x) for x in input().split(',')]
n = len(nums)

res = [-1 for _ in range(n)]
stack = []
for i in range((n << 1) - 1):
    while stack and nums[stack[-1]] < nums[i % n]:
        idx = stack.pop()
        res[idx] = nums[i % n]
    stack.append(i % n)

print(res)


