class Solution:
    def minSubArrayLen(self, target, nums):

        left = 0
        min_length  = len(nums)+1 # I am taking the biggest length out of scope to for refeernce comparison
        window_sum = 0 # For tracking the actual sum for window  i,e. cosectuive postive numbers

        for right in range(len(nums)):
            window_sum+= nums[right]

            while window_sum>= target:
                curr_length = right-left+1
                min_length = min(min_length, curr_length)
                window_sum-=nums[left]
                left+=1
            
        return 0 if min_length== len(nums)+1 else min_length

