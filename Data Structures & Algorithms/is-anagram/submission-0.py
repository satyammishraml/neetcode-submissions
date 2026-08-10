class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_result = {}
        t_result = {}
        for i in s:
            s_result[i] = s_result.get(i, 0) + 1
        for j in t:
            t_result[j] = t_result.get(j, 0) + 1

        for k in s_result:
            if s_result[k] != t_result.get(k, 0):
                return False
        return True
        