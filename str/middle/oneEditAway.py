# 一次编辑
# https://leetcode.cn/problems/one-away-lcci/

class Solution:

    def oneEditAway(self, first: str, second: str) -> bool:
        len1, len2 = len(first), len(second)
        if len1 < len2:
            first, second, len1, len2 = second, first, len2, len1
        count, j = 0, 0
        for i in range(len1):
            if count > 1:
                return False
            if j >= len2:
                count += 1
                continue
            if first[i] == second[j]:
                j += 1
            else:
                count += 1
                if len1 == len2:
                    j += 1
        return count < 2


s = Solution()
assert s.oneEditAway("a", "ab")
assert s.oneEditAway("abc", "ac")
assert s.oneEditAway("ac", "abc")
assert s.oneEditAway("abc", "adc")
assert not s.oneEditAway("abdc", "ab")
assert not s.oneEditAway("abcef", "ab")