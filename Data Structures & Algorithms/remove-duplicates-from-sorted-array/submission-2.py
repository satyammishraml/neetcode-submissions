class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l = 0: let's start the deduplicated region at l = 0, meaning only unique values live at
        # this position and everything before it. nums[0] is trivially unique — a single element
        # can't have a duplicate behind it — so the region starts off already correct with size 1.
        # l is the pointer which divides the deduplicated region from the yet-to-be-processed part:
        #   nums[0 .. l]      -> the answer we are building, strictly increasing, no repeats
        #   nums[l+1 .. r-1]  -> garbage/stale values we are free to overwrite
        #   nums[r .. end]    -> untouched input still waiting to be scanned
        l = 0

        # Now let's check the remaining part (1 to rest). r is the scanner: it visits every element
        # exactly once and never moves backwards, which is what makes this O(n) with O(1) extra space.
        for r in range(1, len(nums)):

            # I care only about elements which are not equal, don't care about equals, i.e. we can
            # expand the window. nums[l] is always the largest distinct value seen so far, and since
            # the array is sorted all copies of a value sit next to each other — so comparing against
            # just nums[l] is enough to know whether nums[r] is a repeat. No need to look further back.
            if nums[l] != nums[r]:

                # We found another element to be added to the deduplicated region, i.e. we expanded it.
                # We increment *before* writing because nums[l] currently holds a value we want to keep;
                # l+1 is the first slot we're allowed to clobber (it's stale or it's r itself).
                l += 1

                # Now fill in the value that has to be there. When l == r this is a harmless self-copy
                # (no duplicates seen yet); when l < r we're pulling the new distinct value back into
                # the compacted prefix, overwriting a duplicate we already skipped past.
                nums[l] = nums[r]

            # Implicit else: nums[l] == nums[r], so nums[r] is a duplicate of the region's last value.
            # We simply don't advance l and don't write anything — r moves on and the duplicate is
            # left behind to be overwritten later.

        # l is the last *index* of the unique region, not its length, so the count is l + 1.
        # (Empty input never enters the loop and would return 1 — LeetCode guarantees n >= 1,
        # otherwise you'd guard with `if not nums: return 0`.)
        return l + 1