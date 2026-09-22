class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s1 is longer than s2, no substring of s2 can be a permutation of s1.
        if len(s1) > len(s2):
            return False

        # Frequency arrays for the 26 lowercase English letters.
        #
        # s1_count -> frequency of characters in the entire s1.
        # s2_count -> frequency of characters in the CURRENT sliding window of s2.
        s1_count = [0] * 26
        s2_count = [0] * 26

        # Build:
        # 1. Character frequency of s1.
        # 2. Character frequency of the FIRST window of s2.
        #
        # The window size must always be len(s1).
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        # If the first window already has exactly the same character
        # frequencies as s1, then it is a permutation of s1.
        if s1_count == s2_count:
            return True

        # Now slide the window through the rest of s2.
        #
        # Example:
        # s1 length = 3
        # s2 = "lecabee"
        #
        # First window:
        #     [l e c] a b e e
        #
        # Next window:
        #      l [e c a] b e e
        #
        # To move from "lec" -> "eca":
        # - remove 'l' from the window
        # - add 'a' to the window

        # 'left' points to the character that must leave the window.
        left = 0

        # The first len(s1) characters are already inside s2_count.
        # Therefore, 'right' starts at len(s1), which is the first
        # new character that needs to enter the window.
        for right in range(len(s1), len(s2)):

            # Add the new character entering from the right side.
            s2_count[ord(s2[right]) - ord("a")] += 1

            # Remove the old character leaving from the left side.
            s2_count[ord(s2[left]) - ord("a")] -= 1

            # Move the left pointer forward for the next window.
            left += 1

            # If the current window has exactly the same character
            # frequencies as s1, then this window is a permutation of s1.
            if s1_count == s2_count:
                return True

        # No permutation of s1 was found inside s2.
        return False