# 1282. 用户分组
# https://leetcode.cn/problems/group-the-people-given-the-group-size-they-belong-to/
from typing import List


class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # k是组大小，v是用户下标集合。
        map = dict()
        for k, v in enumerate(groupSizes):
            if v in map:
                l = map[v]
                n = len(l)
                if len(l[n - 1]) < v:
                    l[n - 1].append(k)
                else:
                    map[v].append([k])
            else:
                map[v] = [[k]]
        ans = []
        for l in map.values():
            ans.extend(l)
        return ans


s = Solution()
print(s.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
print(s.groupThePeople([2, 1, 3, 3, 3, 2]))
