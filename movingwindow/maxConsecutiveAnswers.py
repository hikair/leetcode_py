class Solution:
    def maxConsecutiveAnswers(self, answerKey, k):
        return max(self.mca(answerKey, 'T', k), self.mca(answerKey, 'F', k))

    def mca(self, answerKey, ch, k):
        j = count = result = 0
        for i, v in enumerate(answerKey):
            if v == ch:
                count += 1
            while count > k:
                if answerKey[j] == ch:
                    count -= 1
                j += 1
            result = max(result, i - j + 1)
        return result


s = Solution()
print(s.maxConsecutiveAnswers("TTFF", 2))  # 4
print(s.maxConsecutiveAnswers("TFFT", 1))  # 3
print(s.maxConsecutiveAnswers("TTFTTFTT", 1))  # 5
