# 有效的字母异或词
# https://leetcode.cn/problems/valid-anagram/
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = dict()
        for i in s:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        for i in t:
            if i not in temp:
                temp[i] = -1
            else:
                temp[i] -= 1
            if temp[i] < 0:
                return False
        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram")) # True
print(s.isAnagram("rat", "car")) # False
print(s.isAnagram2("anagram", "nagaram")) # True
print(s.isAnagram2("rat", "car")) # False