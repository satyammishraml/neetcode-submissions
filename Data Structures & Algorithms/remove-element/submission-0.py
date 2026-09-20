class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[k] == val:
                nums.pop(k)
                nums.append("_")
            else:
                k+=1
        return k
