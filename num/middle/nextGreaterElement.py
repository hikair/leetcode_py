# 下一个更大元素 III
# https://leetcode.cn/problems/next-greater-element-iii/

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i < 0:
            return -1
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]
        ans = int(''.join(nums))
        return ans if ans < 2 ** 31 else -1


s = Solution()
assert s.nextGreaterElement(230241) == 230412
assert s.nextGreaterElement(12) == 21
assert s.nextGreaterElement(21) == -1