class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        while index < len(s):
            delim_index = s.index("#", index)
            length = int(s[index:delim_index])
            string = s[delim_index+1:delim_index+1+length]
            decoded.append(string)
            index = delim_index + 1 + length
        return decoded