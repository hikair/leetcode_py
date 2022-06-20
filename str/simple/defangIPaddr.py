# IP 地址无效化
# https://leetcode.cn/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')