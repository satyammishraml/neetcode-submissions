class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        longest_substring = set()
        for R in range(len(s)):
            # if s[R] in longest_substring:
            #     L = R
            #     longest_substring = set()
            while s[R] in longest_substring:
                longest_substring.remove(s[L])
                L+=1
            longest_substring.add(s[R])
            length = max(length, R - L+1)
        
        return length