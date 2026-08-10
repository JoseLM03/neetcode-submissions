class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] = dictionary[num] + 1
        sorted_list = sorted(dictionary.items(), key = lambda x: x[1], reverse = True)
        top_k = sorted_list[:k]
        result = [num for num, freq in top_k]
        return result