class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2, cnt1, cnt2 = None, None, 0, 0
        for num in nums:
            if num == c1:
                cnt1 += 1
            elif num == c2:
                cnt2 += 1
            elif cnt1 == 0:
                c1, cnt1 = num, 1
            elif cnt2 == 0:
                c2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        return [c for c in (c1, c2) if c is not None and nums.count(c) > len(nums) // 3]