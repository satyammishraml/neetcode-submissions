class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # ------------------------------------------------------------
        # PART 1: Basic impossible case
        # ------------------------------------------------------------
        # We want to know:
        # "Does s2 contain ANY permutation/anagram of s1?"
        #
        # Example:
        # s1 = "ab"
        # s2 = "eidbaooo"
        #
        # Permutations of "ab":
        # "ab", "ba"
        #
        # We DON'T actually generate permutations.
        # We only check whether some window of length len(s1)
        # contains exactly the same character frequencies.
        #
        # If s1 is longer than s2, there is no way s2 can contain
        # a window large enough to hold all characters of s1.
        #
        # Example:
        # s1 = "abcd"  -> length 4
        # s2 = "abc"   -> length 3
        #
        # Impossible.
        if len(s1) > len(s2):
            return False


        # ------------------------------------------------------------
        # PART 2: Build frequency arrays for s1 and first window of s2
        # ------------------------------------------------------------
        #
        # Instead of checking permutations directly,
        # we compare how many times every letter appears.
        #
        # Example:
        #
        # s1 = "ab"
        #
        # Counts:
        # a -> 1
        # b -> 1
        # c -> 0
        # d -> 0
        # ...
        #
        # There are only 26 lowercase English letters,
        # so we create arrays of size 26.
        #
        # Index meaning:
        #
        # 0  -> a
        # 1  -> b
        # 2  -> c
        # ...
        # 25 -> z

        s1Count = [0] * 26
        s2Count = [0] * 26


        # ------------------------------------------------------------
        # We first create a window in s2 having the SAME SIZE as s1.
        #
        # Example:
        #
        # s1 = "ab"
        # s2 = "eidbaooo"
        #
        # len(s1) = 2
        #
        # Initial window:
        #
        # s2 = e i d b a o o o
        #      -----
        #      "ei"
        #
        # So initially:
        #
        # s1Count -> counts characters in "ab"
        # s2Count -> counts characters in "ei"
        # ------------------------------------------------------------

        for i in range(len(s1)):

            # Convert character into array index.
            #
            # ord('a') = 97
            # ord('b') = 98
            # ord('c') = 99
            #
            # Therefore:
            #
            # ord('a') - ord('a') = 0
            # ord('b') - ord('a') = 1
            # ord('c') - ord('a') = 2
            #
            # This lets us store character counts in array positions.

            index1 = ord(s1[i]) - ord('a')

            # Increase count of this character in s1.
            #
            # Example:
            # s1 = "ab"
            #
            # first iteration:
            # a -> index 0
            #
            # s1Count[0] becomes 1

            s1Count[index1] += 1


            # Do exactly the same thing for the initial window of s2.

            index2 = ord(s2[i]) - ord('a')
            s2Count[index2] += 1


        # ------------------------------------------------------------
        # PART 3: Instead of comparing all 26 counts every time,
        # calculate how many positions already match.
        # ------------------------------------------------------------
        #
        # Naive approach:
        #
        # Every time the window moves:
        #
        #     if s1Count == s2Count:
        #
        # Python would compare up to 26 positions.
        #
        # That's already fine because 26 is small.
        #
        # But this optimized solution does something clever:
        #
        # "Let's remember how many of the 26 letters currently match."
        #
        # Example:
        #
        # s1 = "ab"
        # first s2 window = "ei"
        #
        # Compare:
        #
        #        s1Count    s2Count
        #
        # a         1          0     ❌
        # b         1          0     ❌
        # c         0          0     ✅
        # d         0          0     ✅
        # e         0          1     ❌
        # f         0          0     ✅
        # ...
        #
        # Most zero-count letters still match!
        #
        # If ALL 26 positions match:
        #
        # matches == 26
        #
        # then both frequency arrays are identical.
        #
        # Meaning:
        #
        # current window is a permutation of s1.
        # ------------------------------------------------------------

        matches = 0

        for i in range(26):

            # If count of this character is identical
            # in s1 and current s2 window,
            # this letter is considered "matching".

            if s1Count[i] == s2Count[i]:
                matches += 1


        # ------------------------------------------------------------
        # PART 4: Start sliding the window
        # ------------------------------------------------------------
        #
        # l = left boundary of our window.
        #
        # Example:
        #
        # s1 = "ab"
        # s2 = "eidbaooo"
        #
        # Initially:
        #
        #        l
        #        ↓
        #        e i d b a o o o
        #        ---
        #        window = "ei"
        #
        # We want the window to ALWAYS have length len(s1).
        #
        # Since first len(s1) characters are already inside the window,
        # r starts from len(s1).
        #
        # len(s1) = 2
        #
        #            r
        #            ↓
        # s2 = e i d b a o o o
        #      ---
        #
        # r points to the NEXT character that will ENTER.
        # ------------------------------------------------------------

        l = 0

        for r in range(len(s1), len(s2)):


            # --------------------------------------------------------
            # PART 5: Before moving the window, check current window
            # --------------------------------------------------------
            #
            # If all 26 character frequencies match,
            # then current window is a permutation of s1.
            #
            # Example:
            #
            # s1 = "ab"
            #
            # current window = "ba"
            #
            # counts:
            #
            # a -> 1 vs 1
            # b -> 1 vs 1
            # every other letter -> 0 vs 0
            #
            # matches = 26
            #
            # So return True immediately.

            if matches == 26:
                return True


            # ========================================================
            # PART 6A: ADD the new RIGHT character into the window
            # ========================================================
            #
            # Example:
            #
            # Current:
            #
            # s2 = e i d b a o o o
            #      ---
            #      e i
            #
            # r points to d.
            #
            # We temporarily add d:
            #
            # e i d
            #
            # Then shortly after we will remove e from the left.
            #
            # This is how the fixed-size window moves right.
            # ========================================================

            index = ord(s2[r]) - ord('a')

            # Increase frequency because this character has ENTERED
            # the current window.

            s2Count[index] += 1


            # --------------------------------------------------------
            # Now something important happened:
            #
            # ONLY ONE character count changed.
            #
            # Therefore, instead of recalculating matches for all
            # 26 characters, we only update the match-state
            # for this ONE character.
            # --------------------------------------------------------


            # CASE 1:
            # After adding the character,
            # the frequency became exactly equal.
            #
            # Example:
            #
            # s1 needs:
            # d = 1
            #
            # before adding:
            # s2 window had d = 0
            #
            # after adding:
            # s2 window has d = 1
            #
            # Now this character changed from:
            #
            # mismatch -> match
            #
            # Therefore:
            # matches += 1

            if s1Count[index] == s2Count[index]:
                matches += 1


            # CASE 2:
            # What if adding the character made us go TOO FAR?
            #
            # Example:
            #
            # s1 needs:
            # a = 1
            #
            # before adding:
            # s2 window had:
            # a = 1
            #
            # They were matching.
            #
            # Then another 'a' enters:
            #
            # s2Count[a] becomes 2
            #
            # Now:
            #
            # s1Count[a] = 1
            # s2Count[a] = 2
            #
            # We changed:
            #
            # match -> mismatch
            #
            # Therefore:
            # matches -= 1
            #
            #
            # Why this condition?
            #
            #     s1Count[index] + 1 == s2Count[index]
            #
            # Suppose:
            #
            # s1Count = 1
            #
            # after adding:
            # s2Count = 2
            #
            # 1 + 1 == 2
            #
            # This tells us:
            # "Before we incremented s2Count, it was exactly equal."
            #
            # So we just destroyed a previous match.

            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1


            # --------------------------------------------------------
            # IMPORTANT:
            #
            # Why don't we do anything otherwise?
            #
            # Example:
            #
            # s1Count[a] = 5
            # s2Count[a] changes:
            #
            # 1 -> 2
            #
            # Before: mismatch
            # After : mismatch
            #
            # Nothing changed regarding matches.
            #
            # So we do nothing.
            # --------------------------------------------------------



            # ========================================================
            # PART 6B: REMOVE the LEFT character from the window
            # ========================================================
            #
            # We added one character from the right,
            # so the window temporarily became one character too big.
            #
            # To keep window size == len(s1),
            # remove the oldest/leftmost character.
            #
            # Example:
            #
            # Before:
            #
            # [e i]
            #
            # Add d:
            #
            # [e i d]
            #
            # Remove e:
            #
            #   [i d]
            #
            # Now the window has moved one position right.
            # ========================================================

            index = ord(s2[l]) - ord('a')

            # This character is leaving the window,
            # therefore decrease its frequency.

            s2Count[index] -= 1


            # --------------------------------------------------------
            # Again, only ONE character changed.
            # So update matches only for this character.
            # --------------------------------------------------------


            # CASE 1:
            # After removing the character,
            # its count becomes equal to s1's required count.
            #
            # Example:
            #
            # s1Count[a] = 1
            #
            # Before removal:
            # s2Count[a] = 2
            #
            # mismatch.
            #
            # Remove one 'a':
            #
            # s2Count[a] = 1
            #
            # Now:
            #
            # 1 == 1
            #
            # mismatch -> match
            #
            # Therefore:
            # matches += 1

            if s1Count[index] == s2Count[index]:
                matches += 1


            # CASE 2:
            #
            # Removing the character may also DESTROY a match.
            #
            # Example:
            #
            # s1Count[a] = 1
            # s2Count[a] = 1
            #
            # They are currently matching.
            #
            # Remove one 'a':
            #
            # s2Count[a] becomes 0
            #
            # Now mismatch.
            #
            # Therefore:
            # matches -= 1
            #
            #
            # After decrement:
            #
            # s1Count[a] - 1 == s2Count[a]
            #
            # Example:
            #
            # 1 - 1 == 0
            #
            # This tells us that BEFORE decrement,
            # the two counts were equal.

            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1


            # --------------------------------------------------------
            # Finally move left pointer one step right.
            #
            # Example:
            #
            # Before:
            #
            # l
            # ↓
            # e i d b a...
            #
            # After removing e:
            #
            #   l
            #   ↓
            # e i d b a...
            #
            # So our next window begins at i.
            # --------------------------------------------------------

            l += 1


        # ------------------------------------------------------------
        # PART 7: Why do we need this final check?
        # ------------------------------------------------------------
        #
        # Inside the loop, we check:
        #
        #     if matches == 26
        #
        # BEFORE sliding.
        #
        # But on the LAST loop iteration, we slide into the final window
        # and then the loop ends.
        #
        # That final window has not yet been checked.
        #
        # Example:
        #
        # s1 = "ab"
        # s2 = "eidba"
        #
        # The final window could be:
        #
        # "ba"
        #
        # which is valid.
        #
        # Therefore we must check once more after the loop ends.

        return matches == 26