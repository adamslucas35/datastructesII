class HashTable:

    # initializes hashtable based of 10 buckets
    def __init__(self, capacity=10):
        self.buckets = [[] for _ in range(capacity)]

    # inserts key value pair into table based on the length of the table
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

    # retrieves the value of the key entered into the parameters
    def get(self, key):
        bucket = hash(key) % len(self.buckets)
        bucket_list = self.buckets[bucket]

        for keyValue in bucket_list:
            if keyValue[0] == key:
                return keyValue[1]
        return None

