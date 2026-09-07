from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        count = 0
        prefix = 0
        for num in nums:
            prefix+= num 
            count += seen[prefix - k]
            seen[prefix] +=1
        return count 