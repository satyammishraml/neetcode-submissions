class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        countdict = defaultdict(dict)
        for i in nums:
            countdict[i] = countdict.get(i, 0) + 1

        max_count = float("-inf")
        max_val = 0
        for key, value in countdict.items():
            if value > max_count:
                max_count = max(max_count, value)
                max_val = key
        return max_val
        