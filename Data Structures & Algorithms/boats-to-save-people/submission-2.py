class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Sort the people's weights so that I can apply two pointers for greedy selection
        of the minimum number of boats.

        Example: suppose one person weighs 110 kg, and the other available weights are
        46, 47, 20, 10, and the boat limit is 120 kg.

        It is better to pair 110 with 10, rather than pairing 10 with 20 or 20 with 47
        first, because if we club the small weights together early, the heavy person
        (110) is left alone and we end up using more boats.

        Sorted: [10, 20, 46, 47, 110]
        Pairs : (10, 110) -> 120 OK, (20, 47) -> 67 OK, (46) alone  =>  3 boats

        That is why we always try to club the heaviest person with the lightest one,
        and if even that pair does not fit, the heaviest person goes alone.
        """

        people.sort()
        boats = 0
        l = 0
        r = len(people) - 1

        # '=' is included so that the last remaining single person is also counted
        while l <= r:
            # Only if the lightest and the heaviest fit together can we move the left pointer
            if people[l] + people[r] <= limit:
                l += 1

            # The heaviest person always leaves in this boat, either paired or alone,
            # so the right pointer moves in every iteration
            r -= 1
            boats += 1

        return boats