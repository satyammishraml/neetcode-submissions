class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for R in range(len(nums)):
            if R > k:
                window.remove(nums[R-k-1])
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
"""Socho k=3, matlab window mein sirf last 3 index rehne chahiye.

```
R par pahunche, to window mein hona chahiye:
R-1, R-2, R-3   (ye 3 hain, k=3)
```

Ab R-4 wala index bahut purana ho gaya, usko nikalna hai.

```
R - k = R - 3  → sabse purana jo allowed hai
R - k - 1 = R - 4  → isse purana, isliye ye nikalna hai
```

Bas itna hi. "-1" isliye kyunki k numbers rakhne hain, to ek se pehle wala hata do.

Chhota example, k=3:

```
R=3 → nikaalo index (3-3-1)= -1  → koi nahi (valid index nahi)
R=4 → nikaalo index (4-3-1)= 0   → index 0 hata do ✓
```

Yaad rakhne ka tarika: **"R-k" = window ka sabse purana member jo rakhna hai. Ek pehle wala (-1 aur) hata do.**"""