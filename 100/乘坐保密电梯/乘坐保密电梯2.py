target, N = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

nums.sort(reverse=True) # 按处理大值优先的原则
if N % 2 == 0:
    n = N // 2
else:
    n = N // 2 + 1

sum_nums = sum(nums)
import copy


class Solution:
    def __init__(self, nums, target, n, sum_nums) -> None:
        self.nums = nums
        self.total = (sum_nums + target) // 2
        self.n = n
        self.up = [] # 存放最终结果的上升操作数
        self.down = [] # 存放最终结果的下降操作数
        self.path = []
        self.find = False
        self.close = float("inf") # 标记与目标楼层的距离
    # count 记录这一轮是放入排列中的位置，cur为总共上升楼层数，nums为剩余序列
    def dfs(self, count, cur, nums): 
        # 找到刚好到达/指定楼层下一层的排列，后续不需要找了
        if self.find:
            return
        # 排列已满
        if count == self.n:
            if cur == self.total: # 刚好到达指定楼层/指定楼层的下一层
                self.up = copy.deepcopy(self.path)
                self.down = copy.deepcopy(nums)
                self.find = True

            elif cur > self.total: # 比指定楼层高不符合
                pass
            elif cur < self.total: # 小于指定楼层，比较谁更近
                if self.total - cur < self.close:
                    self.close = self.total - cur
                    self.up = copy.deepcopy(self.path)
                    self.down = copy.deepcopy(nums)

            return
        
        for i in range(len(nums)):
            cur += nums[i]
            self.path.append(nums[i])

            self.dfs(count+1, cur, nums[:i] + nums[i+1:])

            self.path.pop()
            cur -= nums[i]

    def solve(self):
        self.dfs(0, 0, self.nums)
        ret = []
        # 交替插入
        for i in range(N):
            if i % 2 == 0:
                ret.append(self.up.pop(0))
            else:
                ret.append(self.down.pop(0))
        return ret



s = Solution(nums, target, n, sum_nums)
print(s.solve())

'''
5 3
1 2 6

5 5
3 5 2 1 4

4 5
1 2 3 4 5
'''