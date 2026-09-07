class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        res = 0
        prefixSums = {0:1}
        for num in nums:
            currSum += num
            # prefix sums to remove to match the target
            diff  = currSum - k
            res+= prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
        return res