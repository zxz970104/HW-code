# 输入获取
a = input()
b = input()
v = int(input())
 
 
# 算法入口
def getResult():
    n = len(a)
 
    # a,b字符串的各位字符的ascii绝对值差距数组
    diff = [0] * n
    for i in range(n):
        diff[i] = abs(ord(a[i]) - ord(b[i]))
 
    # 记录题解
    ans = 0
 
    # 滑窗左右边界
    l = 0
    r = 0
 
    # 初始滑窗的内部和
    total = diff[r]
 
    while r < n:
        if total > v:
            # 如果滑窗内部和超过了v，则我们需要先记录上一个滑窗[l, r-1]的长度
            if total - diff[r] <= v:
                ans = max(ans, r - l)
            # 然后由于当前滑窗内部和已经超过了v，因此需要减少滑窗内部和，只能让滑窗左边界+1，内部和减去失去的diff[l]
            total -= diff[l]
            l += 1
            if r < l:
                # 注意左边界右移不能超过右边界，如果超过了，则右边界也需要+1，即变为左边界位置，此时内部和需要加入新右边界值diff[r]
                r = l
                if r < n:
                    total += diff[r]
        else:
            # 如果滑窗内部和没有超过v
            if total == v:
                # 如果滑窗内部和==v,那么当前滑窗就是一个符合要求的，需要记录此时滑窗[l,r]的长度
                ans = max(ans, r - l + 1)
            # 接下来只做滑窗右边界+1，注意右边界不能越界，滑窗需要纳入新右边界值
            # 这里没有做左边界+1 动作，是因为后续的diff有可能都为0，
            # 比如diff = [0, 5, 0, 0, 0], v=5, 当L=0，R=1时，符合当前条件，如果此处做了l++,r++,那么将得不到最大长度
            r += 1
            if r < n:
                total += diff[r]
 
    # 注意收尾处理，即最后必然是r越界，结束循环，因此最后一轮滑窗范围是[l, r-1]
    return max(ans, r-l)
 
 
# 调用算法
print(getResult())