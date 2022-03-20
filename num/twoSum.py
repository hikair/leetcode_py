# https://leetcode-cn.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target) :
        map = dict()
        for index, value in enumerate(nums):
            if target - value in map:
                return [map[target - value], index]
            map[value] = index
        return []

s = Solution()
result = s.twoSum([2, 7, 11, 15], 9)
print(list(result))
result = s.twoSum([3, 2, 4], 6)
print(list(result))
result = s.twoSum([3, 3], 6)
print(list(result))