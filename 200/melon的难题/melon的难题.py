n = int(input())
weight = [int(x) for x in input().split()]



res = 32

class Solution:
    def __init__(self) -> None:
        self.res = 32

    def solve(self):
        weight.sort(reverse=True)
        total = sum(weight)

        if total % 2 != 0:
            return -1
        
        target = total // 2
        
        def dfs(num, path, start):
            if num == target:
                self.res = min(path, self.res)
            
            for i in range(start, n):
                if num + weight[i] > target:
                    continue
                if path + 1 >= res:
                    break
                num += weight[i]
                path += 1
                dfs(num, path, i+1)
                path -= 1
                num -= weight[i]
        dfs(0, 0, 0)
s = Solution()
s.solve()
print(s.res)