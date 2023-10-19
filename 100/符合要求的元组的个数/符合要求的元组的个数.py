nums = [int(x) for x in input().split()]
k = int(input())
target = int(input())

import copy

def solve(nums, k, target):
    nums.sort()
    n = len(nums)
    if n < k:
        return []
    res = []
    def dfs(start, path, total):
        nonlocal res # 代表res为函数外变量，需要一层层向上查找直至第一次找到
        if len(path) == k and total == target: # 终止条件
            res.append(copy.deepcopy(path))
            return
        
        for i in range(start, n):
            # 剪枝：重点nums[i] > 0
            if nums[i] > 0 and total + nums[i] > target:
                return
            
            if i > start and nums[i] == nums[i - 1]: # 去重
                continue
            
            total += nums[i]
            path.append(nums[i])

            dfs(i+1, path, total)

            # 恢复
            total -= nums[i]
            path.pop()

    dfs(0, [], 0)
    return res


print(solve(nums, k, target))


