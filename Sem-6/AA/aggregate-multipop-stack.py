def aggregate_multipop(n):
    array = []
    cost = 1  # cost to push or pop any element (cost of 1 operation)
    total = 0

    print("Element\tOperation Cost")

    # push n elements in array
    for i in range(1, n + 1):
        total += cost
        array.append(i)
        print(i, "\t", cost)

    print("Current stack:", array)

    # multipop
    k = int(input("\nEnter number of elements to multipop: "))
    print(f"Performing multipop({k}):")
    if len(array) < k:
        print(f"No. of elements in array < {k}, so all elements get popped")
    for j in range(min(k, len(array))):
        if array:
            array.pop()
            total += cost
        print(f"Stack after pop {j + 1}:", array)

    # amortized cost = total operations cost / n
    return total / n


n = int(input("Enter number of elements to push in array: "))
a = aggregate_multipop(n)
print("\nAmortized cost for pushing elements and performing multipop =", a)
