class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key not in dictionary:
                dictionary[key] =[]
            dictionary[key].append(string)
        return list(dictionary.values())