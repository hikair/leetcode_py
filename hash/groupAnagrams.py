# 字母异位词分组
# https://leetcode.cn/problems/group-anagrams/
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = collections.defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            map[key].append(s)
        return list(map.values())



s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))