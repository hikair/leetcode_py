# 字符的最短距离
# https://leetcode-cn.com/problems/shortest-distance-to-a-character/
class Solution:
    def shortestToChar(self, s, c):
        size = len(s)
        ans = []
        index = -1
        # 先从左往右遍历，假设当前字符与左侧的c最近
        for i in range(size):
            if s[i] == c:
                index = i
            if index == -1:
                ans.append(None)
            else:
                ans.append(i - index)
        # 从右往左遍历，假设当前字符与右侧的c最近，然后与之前的"答案"作比较取最小值
        index = -1
        for i in range(size - 1, -1, -1):
            if s[i] == c:
                index = i
            if index != -1:
                if ans[i] is None:
                    ans[i] = index - i
                else:
                    ans[i] = min(index - i, ans[i])
        return ans


s = Solution()
print(s.shortestToChar('loveleetcode', 'e')) # [3,2,1,0,1,0,0,1,2,2,1,0]