def twosComplement(num):
    onesComp = ""
    for i in num:
        if i == "0":
            onesComp += "1"
        else:
            onesComp += "0"

    return bin(int(onesComp, 2) + int("1", 2)).replace("0b", "")


# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

num1 = 13
num2 = 5

binNum1 = bin(abs(num1)).replace("0b", "")
binNum2 = bin(abs(num2)).replace("0b", "")

maxlen = len(binNum1)

binNum1 = binNum1.zfill(maxlen)
binNum2 = binNum2.zfill(maxlen + 1)

binCompNum2 = twosComplement(binNum2)
binCompNum2 = binCompNum2.zfill(maxlen)

count = maxlen
m = binNum2
minusm = binCompNum2
q = binNum1
a = "0"
a = a.zfill(maxlen + 1)
leftshift = ""

while count > 0:
    merged = a + q
    leftshift = merged[1:]  # drop left bit as left shift
    a = leftshift[: maxlen + 1]
    a = bin(int(a, 2) + int(minusm, 2)).replace("0b", "")

    if len(a) > maxlen + 1:
        a = a[1:]  # drop carry
    a = a.zfill(maxlen + 1)

    if a[0] == "0":
        leftshift = a + q[1:]  # drop left bit as left shift for q
        leftshift += "1"
    else:
        a = bin(int(a, 2) + int(m, 2)).replace("0b", "")
        if len(a) > maxlen + 1:
            a = a[1:]
        a = a.zfill(maxlen + 1)

        leftshift = a + q[1:]
        leftshift += "0"

    a = leftshift[: maxlen + 1]
    q = leftshift[maxlen + 1 :]
    count -= 1

if a[0] == "1":
    a = bin(int(a, 2) + int(m, 2)).replace("0b", "")
    if len(a) > maxlen + 1:
        a = a[1:]
    a = a.zfill(maxlen + 1)

print(f"Quotient: {int(q, 2)}")
print(f"Remainder: {int(a, 2)}")
