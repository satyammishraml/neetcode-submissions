class Solution:
    def minSubArrayLen(self, target, nums):

        left = 0                       # Left edge of the sliding window
        min_length = len(nums) + 1     # Placeholder: longer than any real window, so it means "no valid window found yet"
        window_sum = 0                 # Running sum of nums[left..right] (all numbers are positive)

        for right in range(len(nums)):
            window_sum += nums[right]  # Expand: add the new right number to the window

            # Shrink: while the window meets the target, keep trying shorter windows
            # until the sum drops below target
            while window_sum >= target:
                curr_length = right - left + 1
                min_length = min(min_length, curr_length)  # Record the length BEFORE removing: this window is still valid
                window_sum -= nums[left]                   # Drop the leftmost number
                left += 1                                  # Move the left edge forward

        # If the placeholder is untouched, no window worked, so return 0 as required
        return 0 if min_length == len(nums) + 1 else min_length