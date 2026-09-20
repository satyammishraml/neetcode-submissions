class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """ Sorting people weights to so that I can apply two pointer for greedy selection in minimum boats, for     example one person weight has 110 kg, whereas other person available weight are 46, 47, 20, 10,   
And lets say maximum weight limit in boat is 120 weight limit, then it is better to merge 110 and 10 weight person, rather 10, 20 or 20, 47, intiiaally as it would it lead gettting lot of boats, that is why we are clubbing height weight first with least or no, any  
"""

        people.sort()
        boats = 0
        l = 0
        r = len(people) - 1
        while l <=r: # include = as last final elements need to included 
            if people[l]+people[r] <= limit: # if both pointer are in limit, then only we can move left pointers
                l+=1
            # Any way we would need to move r pointer (as it has max weight)
            r-=1
            boats+=1
        return boats