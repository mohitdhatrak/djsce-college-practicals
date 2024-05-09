flag = 1
n = 20 # or can take user input

while flag != 0:
    flag = 0
    insertCost = 1
    arrSize = 0

    amortized = int(input("\nEnter estimate cost: "))
    bank = 0

    arr = []

    print("Element Size  Insert  Double  Total  Amortized Bank")

    for i in range(n):
        doublingCost = 0

        if arrSize == 0:
            arr.append(i + 1)
            arrSize = arrSize + 1

        else:
            if arrSize - arr[i - 1] == 0:
                doublingCost = arrSize
                arrSize = arrSize * 2

            arr.append(i + 1)

        totalCost = insertCost + doublingCost

        # underestimate
        if amortized - totalCost + bank < 0:
            bank = bank + (amortized - totalCost)
            print(
                f"{arr[i]}\t{arrSize}\t{insertCost}\t{doublingCost}\t{totalCost}\t{amortized}\t{bank}"
            )
            print("This is an underestimate")
            flag = -1
            break

        # overestimate logic -- we can keep whatever we want, there is no logic to determine overestimate, here i assume totalcost 5 times more in bank is overestimate (only when bank is needed to be used)
        elif amortized - totalCost < 0 and bank > 5 * totalCost:
            bank = bank + (amortized - totalCost)
            print(
                f"{arr[i]}\t{arrSize}\t{insertCost}\t{doublingCost}\t{totalCost}\t{amortized}\t{bank}"
            )
            print("This is an overestimate")
            flag = -1
            break

        bank = bank + (amortized - totalCost)
        print(
            f"{arr[i]}\t{arrSize}\t{insertCost}\t{doublingCost}\t{totalCost}\t{amortized}\t{bank}"
        )

print(f"For {n} elements, above amortized cost is a good estimate!")