N = int(input())
nums = [int(x) for x in input().split()]
def twoSum(nums, target, used):
    dic = set()
    for i in range(len(nums)):
        if i == used:
            continue
        dic.add(target-nums[i])
    
    for i in range(len(nums)):
        if i == used:
            continue
        if (nums[i] << 1) in dic:
            return target-(nums[i] << 1), nums[i]
    return None, None

def solve(nums, N):
    res = [None] * 3
    for i in range(N):
        res[1], res[2]= twoSum(nums, nums[i], i)
        if res[1] is not None:
            res[0] = nums[i]
            break
    
    return res

res = solve(nums, N)
if res[0] == None:
    print(0)
else:
    print(res[0], res[1], res[2])

'''
4
2 7 3 0

3
1 1 1
'''