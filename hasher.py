class HashTable:

    def __init__(self, capacity=10):
        self.buckets = [[] for _ in range(capacity)]
    def insert(self, key, value):
        bucket = hash(key) % len(self.buckets)
        bucket_list = self.buckets[bucket]

        for keyValue in bucket_list:
            if keyValue[0] == key:
                keyValue[1] = value
                return True
        keyValue = [key, value]
        bucket_list.append(keyValue)
        return True

    def get(self, key):
        bucket = hash(key) % len(self.buckets)
        bucket_list = self.buckets[bucket]

        for keyValue in bucket_list:
            if keyValue[0] == key:
                return keyValue[1]
        return None

    def remove(self, key):
        bucket = hash(key) % len(self.buckets)
        bucket_list = self.buckets[bucket]

        for i, keyValue in enumerate(bucket_list):
            if keyValue[0] == key:
                bucket_list.pop(i)
                return True
        return False
