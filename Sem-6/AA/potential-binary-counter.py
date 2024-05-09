binaryStr = "0000"
binaryPrev = binaryStr

# cost to flip '0' -> '1' (always = 1, observe that every next consecutive binary number has only one '0' bit which flips to '1')
setCost = 1
# cost to flip required '1's -> '0's
resetCost = 0
# total cost -> setCost + resetCost
totalCost = 0 # it is same as the number of bits that have flipped compared to previous element (i.e. set + reset bits only)

amortized = 0
potentialPrev = 0
potential = 0 # it is same as the number of '1's in the binary element, so we can directly get the potential by counting number of '1's
# but we need to show it by formula too, so we use below method to get potential 
# by using the formula: phi(n) -> phi(n - 1) - t + 1 (t is the reset cost)

print("Element Set   Reset   Total  Potential Amortized")

for i in range(8):
    if i == 0:
        setCost = 0
    else:
        setCost = 1
        resetCost = 0 
        binaryPrev = binaryStr 
        binaryStr = bin(i)[2:].zfill(4)   
        for j in range(len(binaryStr)):
            if binaryPrev[j] == '1' and binaryStr[j] == '0': # when bit flips from '1' to '0'
                resetCost += 1
        totalCost = resetCost + setCost
        potentialPrev = potential
        potential = potentialPrev - resetCost + setCost # phi(n) -> phi(n - 1) - t + 1

    amortized = totalCost + potential - potentialPrev # total cost + potential difference
    print(f"{binaryStr}\t {setCost}\t{resetCost}\t{totalCost}\t{potential}\t{amortized}")