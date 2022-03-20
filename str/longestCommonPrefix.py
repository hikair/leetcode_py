class Solution:
    def longestCommonPrefix(self, strs):
        size = len(strs)
        if size == 1:
            return strs[0]
        prefix = strs[0]
        while(len(prefix) > 0):
            flag = True
            for i in range(1, size):
                flag &= strs[i].startswith(prefix)
            if flag:
                return prefix
            prefix = prefix[:-1]
        return prefix
s = Solution()
strs = ["flower","flow","flight"]
result = s.longestCommonPrefix(strs) # fl
print(result)
strs = ["dog","racecar","car"]
result = s.longestCommonPrefix(strs) # ""
print(result)