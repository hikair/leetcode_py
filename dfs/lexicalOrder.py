# 字典序排序
# https://leetcode-cn.com/problems/lexicographical-numbers/

class Solution:
    __ans = None

    def lexicalOrder(self, n):
        self.__ans = []
        for i in range(1, 10):
            self.__dfs(i, n)
        return self.__ans

    def __dfs(self, cur, n):
        if cur > n:
            return
        self.__ans.append(cur)
        for i in range(10):
            num = cur * 10 + i
            if num > n:
                break
            self.__dfs(num, n)

s = Solution()
print(s.lexicalOrder(13)) # [1,10,11,12,13,2,3,4,5,6,7,8,9]