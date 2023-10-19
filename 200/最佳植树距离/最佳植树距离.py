# https://blog.csdn.net/qfc_128220/article/details/130633638
from typing import *

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        min_dis = 1  # 最小植树间隔就是相邻位置
        max_dis = position[-1] - position[0] # 最大植树间隔就是两端位置
        res = -1

        #检查选定的最小植树距离是否合法
        def check(x: int) -> bool:
            cnt = 1
            pre = position[0]
            
            # 间隔x放一个树，看一共能放几个
            for i in range(1, len(position)):
                if position[i] - pre >= x:
                    pre = position[i]
                    cnt += 1
            return cnt >= m

        # 二分查找从最小值到最大值中最大的能满足的
        while min_dis <= max_dis:
            mid = (max_dis - min_dis) // 2 + min_dis
            if check(mid):
                res = mid
                min_dis = mid + 1
            else:
                max_dis = mid - 1

        return res
            

