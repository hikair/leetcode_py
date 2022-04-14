# 最富有客户的资产总量
# https://leetcode-cn.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts):
        result = 0
        for i in accounts:
            temp = 0
            for j in i:
                temp += j
            result = max(result, temp)
        return result


s = Solution()
accounts = [[1, 2, 3], [3, 2, 1]]
print(s.maximumWealth(accounts)) # 6
accounts = [[1, 5], [7, 3], [3, 5]]
print(s.maximumWealth(accounts)) # 10
accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
print(s.maximumWealth(accounts)) # 17