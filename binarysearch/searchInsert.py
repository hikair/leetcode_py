# 搜索插入位置
class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

s = Solution()
print(s.searchInsert([1, 3], 0)) # 0
print(s.searchInsert([1, 3, 5], 3)) # 1
print(s.searchInsert([1, 3, 5, 6], 5)) # 2
print(s.searchInsert([1, 3, 5, 6], 2)) # 1
print(s.searchInsert([1, 3, 5, 6], 7)) # 4