# 输入获取
s1 = input()
s2 = input()
 
'''
4A3B2C
2C3B4A
转变为
[[4, 'A'], [3, 'B'], [2, 'C']] 
[[2, 'C'], [3, 'B'], [4, 'A']]
'''
def getZipStrLink(s):
    link = []
    num = []

    # 将数字存入列表，遇到字母时再讲数字列表拼接
    for i in range(len(s)):
        c = s[i]
        if c.isdigit():
            num.append(c)
        else:
            link.append([int("".join(num)), c])
            num.clear()
    return link
 
 
# 算法入口
def getResult():
    link1 = getZipStrLink(s1)
    link2 = getZipStrLink(s2)

    print(link1, link2)
 
    diff = 0
    same = 0
    
    idx1 = 0
    idx2 = 0
    while idx1 < len(link1) and idx2 < len(link2):
        num1, c1 = link1[idx1]
        num2, c2 = link2[idx2]

        compareCount = min(num1, num2) 
 
        if c1 != c2:
            diff += compareCount
        else:
            same += compareCount
 
        if num1 > num2: 
            link1[idx1][0] -= num2
            idx2 += 1
        elif num1 < num2:
            link2[idx2][0] -= num1
            idx1 += 1
        elif num1 == num2:
            idx1 += 1
            idx2 += 1
 
    return f"{diff}/{diff + same}"
 
 
# 算法调用
print(getResult())