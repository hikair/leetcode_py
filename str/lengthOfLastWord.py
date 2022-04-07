# 最后一个单词的长度
# https://leetcode-cn.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s):
        result = 0
        for i in s[::-1]:
            if i == ' ':
                if result > 0:
                    return result
                continue
            result += 1
        return result


s = Solution()
print(s.lengthOfLastWord("Hello World")) # 5
print(s.lengthOfLastWord("   fly me   to   the moon  ")) # 4
print(s.lengthOfLastWord("luffy is still joyboy")) # 6
