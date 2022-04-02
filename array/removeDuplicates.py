# 删除有序数组中的重复项
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates2(self, nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)

    # j指向与前一个元素不相同的元素，i只有交换完再前进
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = j = 1
        while j < len(nums):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


s = Solution()
nums = [1, 1, 2]
result = s.removeDuplicates(nums)
print("result: {}, nums: {}".format(result, nums))
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result = s.removeDuplicates(nums)
print("result: {}, nums: {}".format(result, nums))
nums = []
result = s.removeDuplicates(nums)
print("result: {}, nums: {}".format(result, nums))
nums = [1, 2]
result = s.removeDuplicates(nums)
print("result: {}, nums: {}".format(result, nums))