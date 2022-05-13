# 仅仅反转字母
# https://leetcode.cn/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        size = len(s)
        i, j = 0, size - 1
        while i < j:
            while i < j and not s[i].isalpha():
                i += 1
            while i < j and not s[j].isalpha():
                j -= 1
            ans[i], ans[j] = ans[j], ans[i]
            i += 1
            j -= 1
        return ''.join(ans)


s = Solution()
assert s.reverseOnlyLetters('ab-cd') == 'dc-ba'
assert s.reverseOnlyLetters('a-bC-dEf-ghIj') == 'j-Ih-gfE-dCba'
assert s.reverseOnlyLetters('Test1ng-Leet=code-Q!') == 'Qedo1ct-eeLg=ntse-T!'
