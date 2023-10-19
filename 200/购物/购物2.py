import queue
 
# 输入获取
n, m = map(int, input().split())
nums = list(map(int, input().split()))
 
 
# 组合模型
class CombineModel:
    def __init__(self, curSum, nextIdx):
        self.curSum = curSum  # 当前组合之和
        self.nextIdx = nextIdx  # 将要被加入当前组合的新元素索引位置
 
    # 用于定义对象的小于（<）比较操作的行为。
    def __lt__(self, other):  
        # 对于一个组合模型，其"将要产生的新组合"之和越小，则优先级越高
        # curSum + nums[nextIdx] 为 ”将要产生的新组合“之和
        return self.curSum + nums[self.nextIdx] < (other.curSum + nums[other.nextIdx])
 
 
# 算法入口
def getResult():
    nums.sort()
 
    pq = queue.PriorityQueue()
 
    # 空组合的和为0, 将要加入的新元素是nums[0], 即索引0的元素，其将要产生的新组合之和为 0 + nums[0]
    c = CombineModel(0, 0)
 
    for _ in range(0, m):
        # 打印第 i 小组合
        print(c.curSum + nums[c.nextIdx])
 
        # c是当前最小组合模型，最小的组合模型指的是将要产生的新组合之和在对应轮次中最小
        # 如果当前组合模型c还有可合入的下一个元素，即c.nextIdx + 1 < n, 则说明可以基于当前组合模型产生一个新组合
        if c.nextIdx + 1 < n:
            # 基于当前组合模型产生的新组合，也是本轮最小的组合，即第 i 小组合
            pq.put(CombineModel(c.curSum + nums[c.nextIdx], c.nextIdx + 1))
 
            # 当前组合需要更新nextIdx后，重新加入优先队列
            c.nextIdx += 1
            pq.put(c)
 
        # 取出优先队列中最小组合（注意这里的最小，指的是基于当前组合，将要产生的新组合之和最小）
        c = pq.get()
 
 
# 算法调用
getResult()