class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = [0]*len(nums)

        for i in range(n):
            temp[(i+k)%n] = nums[i]

        nums[:] = temp
        return nums