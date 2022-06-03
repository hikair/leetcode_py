# 独特的电子邮件地址
# https://leetcode.cn/problems/unique-email-addresses/
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            i = email.find('@')
            local = email[0:i]
            j = local.find('+')
            if j > 0:
                local = local[0:j]
            s.add('{}{}'.format(local.replace('.', ''), email[i:]))
        return len(s)


s = Solution()
assert s.numUniqueEmails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]) == 2
assert s.numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]) == 3
