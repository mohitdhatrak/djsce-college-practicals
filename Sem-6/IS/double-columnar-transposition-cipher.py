import random


def encrypt(matrix, key_order, key_size, rows):
    cipher = ""

    for i in range(key_size):
        column = key_order.index(i + 1) # get column number as per key order

        for row in range(rows):
            cipher += matrix[row][column]

    return cipher

def decrypt(text, key_order, key_size, rows):
    deciphered_matrix = [[''] * key_size for _ in range(rows)] # initialize matrix with empty arrays of key size

    for i in range(key_size):
        column = key_order.index(i + 1) # get column number as per key order
        start = rows * i

        for row in range(rows):
            deciphered_matrix[row][column] = text[start + row]

    deciphered_arr = [] # join all the rows to make a single array
    print("\nDeciphered matrix:")
    for row in deciphered_matrix:
        deciphered_arr += row
        print(row)

    return deciphered_arr

# KEY 1
# key1 = input("Enter key 1: ")
key1 = "Potato"
print("Key 1:", key1)
key_size = len(key1) 
sorted_key1 = sorted(key1.lower()) # remember to do key.lower() else it sorts as per ascii values of upper and lower case
key1_copy = key1.lower() # here also do .lower(), as we use this copy for comparison below
print("Sorted key 1:", sorted_key1)

# initialize array with zeroes
key1_order = [0] * key_size

for i in range(key_size):
    for j in range(key_size):
        if sorted_key1[i] == key1_copy[j]:
            key1_order[j] = i + 1
            # to replace letter with '-' once it is matched (to handle case where key has duplicate letters)
            key1_copy = key1_copy[0 : j] + "-" + key1_copy[j + 1 :]
            break

print("Key 1 order:", key1_order)

# KEY 2
# key2 = input("Enter key 2 (same size as key 1): ")
key2 = "Sparta"
print("\nKey 2:", key2)
sorted_key2 = sorted(key2.lower()) # remember to do key.lower() else it sorts as per ascii values of upper and lower case
key2_copy = key2.lower() # here also do .lower(), as we use this copy for comparison below
print("Sorted key 2:", sorted_key2)

# initialize array with zeroes
key2_order = [0] * key_size

for i in range(key_size):
    for j in range(key_size):
        if sorted_key2[i] == key2_copy[j]:
            key2_order[j] = i + 1
            # to replace letter with '-' once it is matched (to handle case where key has duplicate letters)
            key2_copy = key2_copy[0 : j] + "-" + key2_copy[j + 1 :]
            break

print("Key 2 order:", key2_order)

# message = input("\nEnter plain text: ")
message = "Spartans are coming. Hide your wife and kids."
message_size = len(message)
message = message.replace(" ", "_") # replace ' ' with '_'

padding = ["#", "*", "@", "$", "^", "%"]
padding_size = key_size - (message_size % key_size)
for i in range(padding_size):
    message += random.choice(padding)

message_size = len(message) # update message size
print("\nPadded text:", message)

rows = int(message_size / key_size)

matrix1 = []
for i in range(rows):
    arr = []
    start = key_size * i

    for j in range(key_size):
        arr.append(message[start + j])

    matrix1.append(arr)

print("\nMatrix 1: ")
for row in matrix1:
    for letter in row:
        print(letter, end=" ")
    print()

cipher1 = encrypt(matrix1, key1_order, key_size, rows)
print("\nCiphered text (step 1):", cipher1)

matrix2 = []
for i in range(rows):
    arr = []
    start = key_size * i

    for j in range(key_size):
        arr.append(cipher1[start + j])

    matrix2.append(arr)

print("\nMatrix 2: ")
for row in matrix2:
    for letter in row:
        print(letter, end=" ")
    print()

cipher2 = encrypt(matrix2, key2_order, key_size, rows)
print("\nCiphered text (step 2):", cipher2)

# deciphering little complex - 
deciphered_arr1 = decrypt(cipher2, key2_order, key_size, rows)
decipher1 = "".join(deciphered_arr1)
print("\nDeciphered text (step 1):", decipher1)

deciphered_arr2 = decrypt(decipher1, key1_order, key_size, rows)

# remove the padding symbols
for i in range(len(deciphered_arr2)):
    if deciphered_arr2[i] in padding:
        # either make new array and use .remove() method or replace the char by '' if done in same array (as size will reduce)
        deciphered_arr2[i] = '' 

# join all char in array to get a single string, then replace '_' with ' '
decipher2 = "".join(deciphered_arr2).replace("_", " ")

print("\nDeciphered text (step 2):", decipher2)