# 复原 IP 地址
# https://leetcode.cn/problems/restore-ip-addresses/
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n, ans, path = len(s), [], []

        def backtracking(idx: int, start: int):
            nonlocal path
            if len(path) == 4:
                ans.append('.'.join(path))
                return
            for i in [1, 2, 3]:
                leave = n - start - i
                if leave < 0:
                    break
                if (3 - idx) * 3 < leave:
                    continue
                temp = s[start:start + i]
                if temp[0] == '0' and len(temp) > 1:
                    break
                if int(temp) > 255:
                    continue
                path.append(temp)
                backtracking(idx + 1, start + i)
                path = path[0:len(path) - 1]
        backtracking(0, 0)
        return ans


s = Solution()
assert s.restoreIpAddresses('25525511135') == ["255.255.11.135", "255.255.111.35"]
assert s.restoreIpAddresses('0000') == ["0.0.0.0"]
assert s.restoreIpAddresses('101023') == ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
