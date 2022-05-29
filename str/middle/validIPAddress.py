# 验证IP地址
# https://leetcode.cn/problems/validate-ip-address/

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.isIPv4(queryIP):
            return "IPv4"
        if self.isIPv6(queryIP):
            return "IPv6"
        return "Neither"

    def isIPv4(self, queryIP):
        v4 = queryIP.split(".")
        if len(v4) != 4:
            return False
        for s in v4:
            size = len(s)
            if size == 0 or size > 3 or (size > 1 and s[0] == '0'):
                return False
            if not s.isdigit() or int(s) > 255:
                return False
        return True

    def isIPv6(self, queryIP):
        v6 = queryIP.split(":")
        if len(v6) != 8:
            return False
        for s in v6:
            size = len(s)
            if size == 0 or size > 4:
                return False
            for i in s:
                if i.isdigit():
                    continue
                if ord(i) not in range(97, 103) and ord(i) not in range(65, 71):
                    return False
        return True


s = Solution()
assert s.validIPAddress("172.16.254.1") == "IPv4"
assert s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334") == "IPv6"
assert s.validIPAddress("256.256.256.256") == "Neither"