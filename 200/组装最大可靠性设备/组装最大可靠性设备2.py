
import copy
S, N = 500, 3
total = 6
info = [
    [[80, 100], [90, 200], [70, 90]], 
    [[50, 50], [70, 210]], 
    [[50, 100], [60, 150], [80, 200]]
]


# 设备数据结构
class Device:
    def __init__(self, reliability, price) -> None:
        self.reliability = reliability
        self.price = price

rel = []  # 将所有设备的可靠性排序，不分类型
kinds = [] # 将同一类型的设备按可靠性排序

for i in range(len(info)):
    kind = []
    for j in range(len(info[i])):
        rel.append(info[i][j][0])
        kind.append(Device(info[i][j][0], info[i][j][1]))
    kind.sort(key = lambda x : x.reliability)
    kinds.append(copy.deepcopy(kind))
    kind.clear()

rel.sort()


# 在同一类型的设备中二分搜索可靠性大于目标值的设备中价格最低的
# 由于同一类型设备可靠性越高，价格越高，则搜索到的就是第一个比目标值大的
def binarySearch(target, kind):
    left = 0
    right = len(kind) - 1
    while left <= right:
        mid = int((right - left) / 2) + left
        if target > kind[mid].reliability:
            left = mid + 1
        elif target < kind[mid].reliability:
            right = mid - 1
        elif target == kind[mid].reliability:
            return mid
    if right < 0: # 全部比目标值大，返回第一个
        return 0
    if left >= len(kind): # 没有比目标值大的则返回-1
        return -1
    return right # 找不到相等的也要找一个比目标大的，right刚好是>= target的
    


# 检查能否满足目标可靠性且价格符合
def check(rel_val):
   
    sumPrice = 0
    for kind in kinds:
        idx = binarySearch(rel_val, kind)
        # print(idx)
        if idx < 0: # 可靠性能够满足
            return False
        else:
            sumPrice += kind[idx].price

    return sumPrice <= S  # 价格能否满足


def solve():
    res = -1
    left = 0
    right = total - 1

    # 二分搜索可靠性排序后的列表，找到满足条件下最大的
    while left <= right:
        mid = int((right - left) / 2) + left
        if check(rel[mid]):
            res = rel[mid]
            left = mid + 1
        else:
            right = mid - 1

    return res


print(solve())    

    
    
