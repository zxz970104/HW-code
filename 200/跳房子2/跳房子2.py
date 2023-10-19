arr = [int(x) for x in input().split()]
target = int(input())
n = len(arr)

def solve():
    res = [0, 0, 0]
    indexSum = float("inf")
    # 保留排序前元素的索引
    newarr = [(arr[i], i) for i in range(n)]
    # 排序
    newarr.sort(key=lambda x :(x[0], x[1]))
    for i in range(n):
        # 减枝优化，当遍历到的元素大于0，且目标值大于0小于遍历到的元素，那么后续任何两个元素与当前元素之和都大于target
        if newarr[i][0] > 0 and 0 < target < newarr[i][0]:
            break

        # 减枝优化，前后两数相同不用重复遍历
        if i > 0 and newarr[i][0] == newarr[i-1][0]:
            continue

        # 以当前遍历的元素作为三个数中的一个，其余两个可以使用滑动窗口找出和为target-当前元素
        left = i + 1
        right = n - 1
        while left < right:
            
            count = newarr[i][0] + newarr[left][0] + newarr[right][0]

            if count < target:
                left += 1
            elif count > target:
                right -= 1
            elif count == target:
                
                # 减枝优化，右指针指向的元素若和前一元素相同，则必然结果是前一元素（排序时，元素相同比较索引）
                while left < right and newarr[right][0] == newarr[right-1][0]:
                    right -= 1

                idxs = newarr[i][1] + newarr[left][1] + newarr[right][1]

                # 更新结果
                if idxs < indexSum:
                    res = [ newarr[i][1], newarr[left][1], newarr[right][1] ]
                    indexSum = idxs
                left += 1
                right -= 1
        res.sort()
        return arr[res[0]], arr[res[1]], arr[res[2]]



print(solve())