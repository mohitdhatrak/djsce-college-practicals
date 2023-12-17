import time

from BTrees._IIBTree import IIBTree

# btree = IIBTree(order=2) --> order means number of child nodes tree can have
btree = IIBTree()

start_time = time.perf_counter()
for i in range(100000):
    btree.update({i: 2 * i})
    # btree[i] = 2 * i --> can use like a dictionary
end_time = time.perf_counter()

# print(f"The insertion time for the BTree is {round((end_time - start_time) * 1000, 3)} milliseconds")


def print_menu():
    print("\n*** B Tree ***")
    print("1. Search")
    print("2. Insert")
    print("3. Delete")
    print("4. Exit")
    return input("Enter your choice: ")


while True:
    choice = print_menu()

    if choice == "1":
        key = int(input("Enter the search key: "))

        start_time = time.perf_counter()
        if key in btree:
            print(f"Data for search key found: {btree[key]}")
        else:
            print("Data for search key not found")
        end_time = time.perf_counter()

        print(
            f"The search time for the BTree is {round((end_time - start_time) * 1000, 3)} milliseconds"
        )

    elif choice == "2":
        key = int(input("Enter the key: "))
        data = int(input("Enter the data: "))

        start_time = time.perf_counter()
        if key in btree:
            btree.update({key: data})
            print("Key already exists, data value updated!")
        else:
            btree.update({key: data})
            print(f"Inserted data: {data} at key: {key}")
        end_time = time.perf_counter()

        print(
            f"The insertion time for the BTree is {round((end_time - start_time) * 1000, 3)} milliseconds"
        )

    elif choice == "3":
        key = int(input("Enter the key: "))

        start_time = time.perf_counter()
        if key in btree:
            print(f"Deleted key {key} with data: {btree[key]}")
            btree.__delitem__(key)
        else:
            print("Key does not exist!")
        end_time = time.perf_counter()

        print(
            f"The deletion time for the BTree is {round((end_time - start_time) * 1000, 3)} milliseconds"
        )

    elif choice == "4":
        break

    else:
        print("Please enter valid choice!")
