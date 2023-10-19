# 最简单的方式就是解压后逐字符比较，但 n < 100000000, 无论是时间还是空间都难以接受


# 在压缩字符串上比较



def solve(str1, str2):
    n = len(str1)
    total = 0

    # 将 10A5B12C 字符串转化成 [10，"A", 5, "B", 12, "C"]的形式
    left = 0
    right = 0
    vec1 = []
    while right < n:
        if str1[right].isalpha():
            num = int(str1[left:right])
            total += num
            vec1.append(num)
            vec1.append(str1[right])
            left = right + 1
        right += 1

    left = 0
    right = 0
    vec2 = []
    while right < n:
        if str2[right].isalpha():
            vec2.append(int(str2[left:right]))
            vec2.append(str2[right])
            left = right + 1
        right += 1

    print(vec1)
    print(vec2)
    res = 0
    idx1 = 0
    idx2 = 0
    len1 = len(vec1)
    len2 = len(vec2)

    # 交替比较
    while idx1 < len1 and idx2 < len2:
        
        if vec1[idx1] == vec2[idx2] and vec1[idx1+1] == vec2[idx2+1]:
            idx1 += 2
            idx2 += 2

        elif vec1[idx1] > vec2[idx2] and vec1[idx1+1] == vec2[idx2+1]:
            vec1[idx1] -= vec2[idx2]
            idx2 += 2

        elif vec1[idx1] < vec2[idx2] and vec1[idx1+1] == vec2[idx2+1]:
            vec2[idx2] -= vec1[idx1]
            idx1 += 2

        elif vec1[idx1] >= vec2[idx2] and vec1[idx1+1] != vec2[idx2+1]:
            vec1[idx1] -= vec2[idx2]
            res += vec2[idx2]
            idx2 += 2
            
        elif vec1[idx1] < vec2[idx2] and vec1[idx1+1] != vec2[idx2+1]:
            vec2[idx2] -= vec1[idx1]
            res += vec1[idx1]
            idx1 += 2

    # 由于解压后的字符串确保一样长，这里可以省去     
    while idx1 < len1:
        res += vec1[idx1]
        idx1 += 2
    while idx2 < len2:
        res += vec2[idx2]
        idx2 += 2

    return str(res) + "/" + str(total)



s1 = input()
s2 = input()

print(solve(s1, s2))