import time

from bplustree import BPlusTree

tree = BPlusTree("C:b+tree.db", order=50)

# entering data in a BPlusTree
start_time = time.perf_counter()
for i in range(1000):
    data = (2 * i).to_bytes(10, "big")
    tree[i] = data
end_time = time.perf_counter()
print("Time taken for inserting data:", (end_time - start_time))

# searching for data in a BPlusTree
key = int(input("Enter the search key: "))
start_time = time.perf_counter()
byte_data = tree.get(key)
end_time = time.perf_counter()

if byte_data is not None:
    int_data = int.from_bytes(byte_data, "big")
    print("Value for search key:", int_data)
    print("Time taken for searching data:", (end_time - start_time))
else:
    print("Key not found in the BPlusTree.")
