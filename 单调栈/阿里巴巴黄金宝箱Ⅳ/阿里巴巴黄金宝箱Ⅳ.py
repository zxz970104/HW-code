# 暴力解法

nums = [int(x) for x in input().split(',')]
n = len(nums)

res = [-1 for _ in range(n)]
for i in range(n):
    idx = i + 1
    while idx != i:
        if idx == n:
            idx = 0
            continue
        if nums[idx] > nums[i]:
            res[i] = nums[idx]
            break
        else:
            idx += 1
    if idx == i:
        res[i] = -1

print(res)


