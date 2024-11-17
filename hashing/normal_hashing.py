
# Normal hashing:
import hashlib


class NormalModuloHashing:

    def __init__(self, servers) -> None:
        self.servers = servers

    def get_server(self, key):

        # lets hash the key and find the server using modulo
        hashed_key = int(hashlib.md5(key.encode()).hexdigest(), 16)
        server_index = hashed_key % len(self.servers)
        return server_index


servers = ['server0', 'server1', 'server2']

mod_hashing = NormalModuloHashing(servers=servers)

keys = ['User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7', 'User8']

print("# using Normal Hash # ")

for key in keys:

    print(f"key {key} is mapped to {mod_hashing.get_server(key)}")


"""
output :

# using Normal Hash # 
# using Normal Hash # 
key User1 is mapped to 0
key User2 is mapped to 0
key User3 is mapped to 0
key User4 is mapped to 1
key User5 is mapped to 1
key User6 is mapped to 1
key User7 is mapped to 1
key User8 is mapped to 1
"""

# lets increase the servers and see what the impact is :


servers.append('server3')


print("\nAfter Adding a Server:")

mod_hashing = NormalModuloHashing(servers=servers)

for key in keys:

    print(f"key {key} is mapped to {mod_hashing.get_server(key)}")


"""
After Adding a Server:

key User1 is mapped to 1
key User2 is mapped to 2
key User3 is mapped to 1
key User4 is mapped to 3
key User5 is mapped to 2
key User6 is mapped to 2
key User7 is mapped to 2
key User8 is mapped to 2

"""


"""
- so in normal modulus hashing the assignment of the servers and keys drastically changes entirely
when we either remove teh servers/add servers i/e scale up and down , in that case we need to move teh data between them 
continuosly whenever this happens 



-> Every time you add or remove a server (scale up or down), most keys get reassigned.
-> This requires significant data movement between servers to maintain the new mapping, which can be costly in terms of time and resources.
->For large-scale systems, this approach is inefficient and not practical.

"""
