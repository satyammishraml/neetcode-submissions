class Solution:
    def minSubArrayLen(self, target, nums):
        l = total = 0
        ans = float('inf')

        for r in range(len(nums)):
            total += nums[r]              # grow
            while total >= target:        # valid? then shrink
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if ans == float('inf') else ans