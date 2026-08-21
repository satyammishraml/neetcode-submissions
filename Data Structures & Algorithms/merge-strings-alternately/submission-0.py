class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        min_length = min(len(word1), len(word2))
        res = ""
        for i in range(min_length) :
            res = res + word1[i]+ word2[i]
       
        res = res+ word1[min_length:]+word2[min_length:]
        return res
        