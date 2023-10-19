# 输入获取
a = input()
b = input()
v = int(input())
 
# 算法入口
def getResult():
    n = len(a)
    diff = [0] * n
    #构建差值列表
    for i in range(n):
        diff[i] = abs(ord(a[i]) - ord(b[i]))

    left = 0
    right = 0
    total = diff[0]
    res = 0
    
    # 滑动串口找最大
    while right < n:
        if total > v:
            # 此时的total是包含了当前right处的差值的，将其去除后判断并更新结果
            if total - diff[right] <= v:
                res = max(res, right - left)

            # 差值和去除左边界差值并使左边界右移
            total -= diff[left] 
            left += 1

            # 左边界右移可能发生左指针大于右指针，此时将右指针指向右边界并total清0，相当于从当前位置重新开始滑动
            if right < left:
                right = left
                total = 0
                if right < n:
                    total += diff[right]
        else:
            # 如果滑窗内部和没有超过v
            if total == v:
                res = max(res, right - left + 1)
                # 这里没有左边界+1是因为后续差值可能为0
            
            # right右移并新增差值，注意右边界不能越界；
            right += 1
            if right < n:
                total += diff[right]

    return res
    
 
 
# 调用算法
print(getResult())