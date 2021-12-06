class Bucket:
    """ This is the bucket at each location in the underlying array, to handle collisions """

    def __init__(self):
        self.__bucket = []

    def get(self, key):
        for (k, v) in self.__bucket:
            if key == k:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.__bucket):
            if key == kv[0]:
                self.__bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.__bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.__bucket):
            if key == kv[0]:
                del self.__bucket[i]


class HashMap:

    def __init__(self):
        self.__key_space = 599
        self.__hash_table = [Bucket() for i in range(self.__key_space)]

    def put(self, key, value):
        hash_key = self.__calculate_hash_key(key)
        self.__hash_table[hash_key].update(key, value)

    def get(self, key):
        hash_key = self.__calculate_hash_key(key)
        value = self.__hash_table[hash_key].get(key)
        return value

    def remove(self, key):
        hash_key = self.__calculate_hash_key(key)
        self.__hash_table[hash_key].remove(key)

    def __calculate_hash_key(self, key):
        hash_key = key % self.__key_space
        return hash_key


if __name__ == "__main__":

    hash_map = HashMap()
    hash_map.put(1, 100)
    hash_map.put(2, 200)

    print(hash_map.get(2))

    hash_map.remove(1)

    print(hash_map.get(1))
    print(hash_map.get(2))

    print("Checking the mods.")
    print(1 % 599)
    print(10 % 599)
    print(15 % 599)
    print(2070 % 599)
    print(10 ** 6 % 599)
