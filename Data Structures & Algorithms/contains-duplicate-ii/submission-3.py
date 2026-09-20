class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}
        for i, num in enumerate(nums):
            # Have we seen this number before?
            # And was that sighting close enough (within k positions)?
            if num in last_seen and i - last_seen[num] <=k:
                return True
            # Either it's new, or the old copy was too far away.
            # Overwrite with the current index, because for any
            # future duplicate, the NEAREST copy is the only one
            # that can possibly satisfy the distance rule.
            last_seen[num] = i
        return False