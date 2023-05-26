class TimeMap:

    def __init__(self):
        self.store = {} # key : list of [value, timestamp]
    
    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
    
    def get(self, key, timestamp):
        result = ""
        values = self.store.get(key, [])

        # binary search
        left, right = 0, len(values) - 1
        while left <= right:
            medium = (right + left) // 2
            if values[medium][1] <= timestamp:
                result = values[medium][0]
                left = medium + 1
            else:
                right = medium - 1
        return result
        