# 最常见单词
# https://leetcode-cn.com/problems/most-common-word/
class Solution:
    def mostCommonWord(self, paragraph, banned):
        res = None
        map = dict()
        i = 0
        length = len(paragraph)
        while i < length:
            while i < length and not paragraph[i].isalpha():
                i += 1
            j = i + 1
            while j < length and paragraph[j].isalpha():
                j += 1
            word = paragraph[i:j].lower()
            if word in banned:
                i = j + 1
                continue
            if word not in map:
                map[word] = 1
            else:
                map[word] = map[word] + 1
            if res is None or map[res] < map[word]:
                res = word
            i = j + 1
        return res


s = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(s.mostCommonWord(paragraph, banned)) # ball

paragraph = "bob. "
banned = ["hit"]
print(s.mostCommonWord(paragraph, banned)) # bob

paragraph = "a, a, b,b,b,b a"
banned = ["hit"]
print(s.mostCommonWord(paragraph, banned)) # b