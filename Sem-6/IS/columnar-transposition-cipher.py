import random

key = "Analyst"
keyCopy = key
keySize = len(key)
sortedKey = sorted(key)
print("Key:", key)

keyOrder = []
# initialize array with zeroes
for i in range(keySize):
    keyOrder.append(0)

for i in range(keySize):
    for j in range(keySize):
        if sortedKey[i] == keyCopy[j]:
            keyOrder[j] = i + 1
            # to replace letter with '-' once it is matched
            keyCopy = keyCopy[0:j] + "-" + keyCopy[j + 1 :]
            break

print("Key order:", keyOrder)

plainText = input("Enter plain text: ")
textSize = len(plainText)

padding = ["#", "*", "@", "$", "^", "%"]
padSize = keySize - (textSize % keySize)

for i in range(padSize):
    plainText += random.choice(padding)

textSize = len(plainText)  # update text size
print("Padded text:", plainText)

matrix = []

for i in range(int(textSize / keySize)):
    arr = []
    start = i * keySize

    for j in range(keySize):
        arr.append(plainText[start + j])

    matrix.append(arr)

print("Matrix: ")
for i in range(len(matrix)):
    for letter in matrix[i]:
        print(letter, end=" ")
    print()

cipher = ""
for i in range(keySize):
    position = keyOrder.index(i + 1)

    for j in range(len(matrix)):
        cipher += matrix[j][position]

print("\nCiphered text:", cipher)
