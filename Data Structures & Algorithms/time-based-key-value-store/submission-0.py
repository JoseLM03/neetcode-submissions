class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.store:
            return ""
        # The timestamp/value pairs for this key
        key_search = self.store[key]
        left = 0
        right = len(key_search) - 1
        current_best = '' # Best valid value found so far

        while left <= right:
            mid = (left + right) // 2

            if key_search[mid][0] <= timestamp:
                current_best = key_search[mid][1]
                left = mid + 1
            else:
                right = mid - 1
    
        return current_best