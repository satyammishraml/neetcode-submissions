class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string = encoded_string + str(len(i)) + "#" +i
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] !="#":
                j +=1 
            length = int(s[i:j])
            i = j+1+length
            decoded_strs.append(s[j+1: i])
        return decoded_strs