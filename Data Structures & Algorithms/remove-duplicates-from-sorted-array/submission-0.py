class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        while l <=len(nums)-1 and r<=len(nums)-1:
            print("l is {} and r and is {} ".format(l, r))
            if nums[l] ==nums[r]:
                print("equal removing at r")
                nums.pop(r)
            else:
                print("incrementing ")
                l+=1
                r+=1
            print(nums)
        return len(nums)
            
             