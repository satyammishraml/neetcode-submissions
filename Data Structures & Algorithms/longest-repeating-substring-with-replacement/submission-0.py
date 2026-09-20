class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        AAABABB, 1
        AAAAABB -> 5

        XYYX, 2
        XXXX ->5

        ABABAAAAA 2, ->5 
        """

        length = 0
        L = 0
        counts = collections.defaultdict(int)
        max_freq = 0
        for R in range(len(s)):
            counts[s[R]] += 1
            max_freq = max(max_freq, counts[s[R]])
            
            if (R - L + 1) - max_freq > k:
                counts[s[L]] -= 1
                L += 1
            
            length = max(length, R - L + 1)
        return length