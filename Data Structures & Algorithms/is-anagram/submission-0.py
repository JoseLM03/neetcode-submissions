class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionaryS = {}
        dictionaryT = {}
        for char in s:
            if char in dictionaryS:
                dictionaryS[char] = dictionaryS[char] + 1
            else:
                dictionaryS[char] = 1
        for char in t:
            if char in dictionaryT:
                dictionaryT[char] = dictionaryT[char] + 1
            else:
                dictionaryT[char] = 1
        if dictionaryS == dictionaryT:
            return True
        else:
            return False