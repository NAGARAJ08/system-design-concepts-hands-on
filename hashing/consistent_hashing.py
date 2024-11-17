
# keep teh hash func independent of the no of servers/ storage nodes


# "Consistent hashing is a special kind of hashing such that when a
# hash table is re-sized and consistent hashing is used, only k/n keys need to be remapped on
# average, where k is the number of keys, and n is the number of slots. In contrast, in most
# traditional hash tables, a change in the number of array slots causes nearly all keys to be
# remapped


import bisect


class ConsistentHash:

    def __init__(self, servers, replica=3) -> None:

        # these are virtual nodes
        self.replica = replica
        self.ring = {}

        self.sorted_keys = []

        for server in servers:
            self.add_server(server)

    def add_server(self, server):
        for i in range(self.replica):
            key = hash(f"{server}:{i}")
            self.ring[key] = server
            bisect.insort(self.sorted_keys, key)

    def remove_server(self, server):

        for i in range(self.replica):
            key = hash(f"{server}:{i}")
            self.ring.pop(key)
            self.sorted_keys.remove(key)

    def get_server(self, key):

        if not self.ring:
            return None

        hashed_key = hash(key)
        idx = bisect.bisect(self.sorted_keys, hashed_key) % len(
            self.sorted_keys)
        closest_key = self.sorted_keys[idx]
        return self.ring[closest_key]


servers = ['Server1', 'Server2', 'Server3']
hashing = ConsistentHash(servers)

keys = ['User1', 'User2', 'User3', 'User4']

print("\nConsistent Hashing:")
for key in keys:
    print(f"Key {key} is mapped to {hashing.get_server(key)}")

hashing.add_server('Server4')
print("\nAfter Adding a Server:")
for key in keys:
    print(f"Key {key} is mapped to {hashing.get_server(key)}")

hashing.remove_server('Server2')
print("\nAfter Removing a Server:")
for key in keys:
    print(f"Key {key} is mapped to {hashing.get_server(key)}")
