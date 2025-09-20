class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        for word in strs:
            N = len(word)
            encode_string = encode_string + str(N) + "$" + word
        return encode_string     


    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j+=1
            length = int(s[i:j])    
            decode_list.append(s[j+1:j+1+length])
            i = j+1+length      
        return decode_list
