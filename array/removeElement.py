# 移除元素
class Solution:
    def removeElement2(self, nums, val):
        if not nums:
            return 0
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[j] == val:
                j -= 1
                continue
            if nums[i] != val:
                i += 1
                continue
            nums[i] = nums[j]
            i += 1
            j -= 1
        return i

    def removeElement(self, nums, val):
        i = j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

s = Solution()
nums = [1, 1, 2]
result = s.removeElement(nums, 1)
print("result: {}, nums: {}".format(result, nums))
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result = s.removeElement(nums, 2)
print("result: {}, nums: {}".format(result, nums))
nums = []
result = s.removeElement(nums, 1)
print("result: {}, nums: {}".format(result, nums))
nums = [0, 1, 2, 2, 3, 0, 4, 2]
result = s.removeElement(nums, 2)
print("result: {}, nums: {}".format(result, nums))
