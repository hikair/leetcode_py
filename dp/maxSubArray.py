# 最大子数组和
# https://leetcode-cn.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums):
        result = nums[0]
        dp = [result]
        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp.append(dp[i - 1] + nums[i])
            else:
                dp.append(nums[i])
            result = max(result, dp[i])
        return result


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(s.maxSubArray([1]))  # 1
print(s.maxSubArray([5, 4, -1, 7, 8]))  # 23
