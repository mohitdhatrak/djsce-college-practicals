binaryStr = "0000"
binaryPrev = binaryStr

# cost to flip 0 -> 1 always = 1
setCost = 1
# cost to flip required 1s -> 0s
resetCost = 0
# total cost -> setCost + resetCost
totalCost = 0

potential = 0
potentialPrev = 0
amortized = 0

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
            if binaryPrev[j] == '1' and binaryStr[j] == '0':
                resetCost += 1
        totalCost = resetCost + setCost
        potentialPrev = potential
        potential = potentialPrev - resetCost + setCost
    
    amortized = totalCost + potential - potentialPrev
    print(f"{binaryStr}\t {setCost}\t{resetCost}\t{totalCost}\t{potential}\t{amortized}")
    