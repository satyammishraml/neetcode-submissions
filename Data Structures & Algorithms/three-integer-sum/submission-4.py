class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            l = idx + 1
            r = len(nums) - 1
            target = -nums[idx]
            while l < r:
                s = nums[l]+nums[r]
                if s < target:
                    l+=1
                elif s > target:
                    r-=1
                else:
                    result.append([nums[idx], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l]==nums[l-1]:
                        l+=1
                    # while l < r and nums[r]==nums[r-1]:
                    #     l+=1
        return result
