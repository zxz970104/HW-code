target, N = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

nums.sort(reverse=True) # 按处理大值优先的原则
import copy


class Solution:
    def __init__(self, nums, target) -> None:
        self.nums = nums
        self.target = target
        self.n = len(nums)
        self.path = []
        self.res = []
        self.find = False
        self.close = float("inf")
    # count 记录这一轮是放入排列中的位置，cur为当前楼层，nums为剩余序列
    def dfs(self, count, cur, nums): 
        # 找到刚好到达的排列，后续不需要找了
        if self.find:
            return
        # 排列已满
        if count == self.n:
            if cur == self.target: # 刚好到达指定楼层
                self.res = copy.deepcopy(self.path)
                self.find = True
                return 
            elif cur > self.target: # 比指定楼层高不符合
                return
            elif cur < self.target: # 小于指定楼层，比较谁更近
                if target - cur < self.close:
                    self.close = target - cur # 更新靠近结果
                    self.res = copy.deepcopy(self.path)

        
        for i in range(len(nums)):

            # 为偶加，为奇减
            if count % 2 == 0:
                cur += nums[i]
            else:
                cur -= nums[i]
            
            self.path.append(nums[i]) # 加入排列
            self.dfs(count+1, cur, nums[:i] + nums[i+1:])
            self.path.pop()
            if count % 2 == 0:
                cur -= nums[i]
            else:
                cur += nums[i]


s = Solution(nums, target)
s.dfs(0, 0, s.nums)
print(s.res)

'''
5 3
1 2 6

5 5
3 5 2 1 4

4 5
1 2 3 4 5
'''