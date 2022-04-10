# 唯一摩尔斯密码词
# https://leetcode-cn.com/problems/unique-morse-code-words/
class Solution:
    table = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
             "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    def uniqueMorseRepresentations(self, words):
        res = set()
        for word in words:
            temp = ""
            for i in word:
                temp += self.table[ord(i) - ord('a')]
            res.add(temp)
        return len(res)


s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])) # 2
print(s.uniqueMorseRepresentations(["a"])) # 1