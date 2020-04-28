class LRUCache:
    def __init__(self, capacity: int):
        self.max_cap = capacity
        self.key_cache = []
        self.key_dict = {}

    def get(self, key: int) -> int:
        if key in self.key_dict:
            self.key_cache.remove(key)
            self.key_cache.append(key)
            return self.key_dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_dict:
            self.key_cache.remove(key)
            del self.key_dict[key]
        if len(self.key_cache) == self.max_cap:
            del self.key_dict[self.key_cache[0]]
            del self.key_cache[0]
        self.key_cache.append(key)
        self.key_dict[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)