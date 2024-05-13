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

# key = input("Enter key: ")
key = "Analyst"
print("Key:", key)
key_size = len(key)
sorted_key = sorted(key.lower()) # remember to do key.lower() else it sorts as per ascii values of upper and lower case
key_copy = key.lower() # here also do .lower(), as we use this copy for comparison below
print("Sorted key:", sorted_key)

# initialize array with zeroes
key_order = [0] * key_size

for i in range(key_size):
    for j in range(key_size):
        if sorted_key[i] == key_copy[j]:
            key_order[j] = i + 1
            # to replace letter with '-' once it is matched (to handle case where key has duplicate letters)
            key_copy = key_copy[0 : j] + "-" + key_copy[j + 1 :]
            break

print("Key order:", key_order)

# message = input("\nEnter plain text: ")
message = "Single columnar transposition cipher!"
message_size = len(message)
message = message.replace(" ", "_") # replace ' ' with '_'

padding = ["#", "*", "@", "$", "^", "%"]
padding_size = key_size - (message_size % key_size)
for i in range(padding_size):
    message += random.choice(padding)

message_size = len(message) # update message size
print("Padded text:", message)

rows = int(message_size / key_size)

matrix = []
for i in range(rows):
    arr = []
    start = key_size * i

    for j in range(key_size):
        arr.append(message[start + j])

    matrix.append(arr)

print("\nMatrix: ")
for row in matrix:
    for letter in row:
        print(letter, end=" ")
    print()

cipher = encrypt(matrix, key_order, key_size, rows)
print("\nCiphered text:", cipher)

# little complex - 
deciphered_arr = decrypt(cipher, key_order, key_size, rows)

# remove the padding symbols
for i in range(len(deciphered_arr)):
    if deciphered_arr[i] in padding:
        # either make new array and use .remove() method or replace the char by '' if done in same array (as size will reduce)
        deciphered_arr[i] = ''

# join all char in array to get a single string, then replace '_' with ' '
decipher = "".join(deciphered_arr).replace("_", " ")

print("\nDeciphered text:", decipher)