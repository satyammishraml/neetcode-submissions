class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        L = 0
        subset = set()
        for R in range(len(s)):
            while s[R] in subset: 



                subset.remove(s[L])
                L+=1

            subset.add(s[R])
            length = max(length, R-L+1)
        return length

"""Because the duplicate isn't necessarily sitting at the left edge — it can be anywhere inside the window, so one removal usually isn't enough. You have to keep removing until you've removed that specific character.

Trace "abcb":

R=0 'a' → window {a},     L=0
R=1 'b' → window {a,b},   L=0
R=2 'c' → window {a,b,c}, L=0
R=3 'b' → duplicate! but 'b' lives at index 1, and L=0 points at 'a'

With while: remove 'a' (L=1), check again — 'b' still in window — remove 'b' (L=2), now it's gone. Add 'b', window {c,b} = "cb", length 2. Correct.

With if: remove 'a' once, L=1, exit. Then subset.add('b') — but 'b' was never removed, so the set is unchanged at {b,c} while your window indices claim [1,3] = "bcb". Length computes as 3. Wrong answer, and worse, the set has silently stopped describing the window."""