class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        for idx, val in enumerate(strs[0]):
            for j in strs[1:len(strs)]:
                if idx >= len(j) or val != j[idx] :
                   return strs[0][:idx]
        return strs[0]

        