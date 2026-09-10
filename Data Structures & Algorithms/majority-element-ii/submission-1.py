class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for key, value in count.items():
            if value > len(nums) // 3:
                res.append(key)

        return res