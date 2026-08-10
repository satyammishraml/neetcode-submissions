class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for i in nums:
            result[i] = result.get(i, 0) +1
        
        for i in result.values():
            if i > 1 :
                return True
        return False