import random

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text, key):
    cipher = ""

    for char1, char2 in zip(text, key):
        position = (alphabets.index(char1) ^ alphabets.index(char2)) % 26
        cipher += alphabets[position]

    return cipher

def decrypt(text, key):
    decipher = ""

    for char1, char2 in zip(text, key):
        position = (alphabets.index(char1) ^ alphabets.index(char2)) % 26
        decipher += alphabets[position]

    return decipher

# message = input("Enter plain text: ")
message = "HelloWorld"
print("Length of plain text is", len(message))
message = message.upper()

key = ""
for i in range(len(message)):
    key += random.choice(alphabets)
print("Random key (length same as plain text):", key)
key = key.upper()

cipher = encrypt(message, key)
print("Ciphered text:", cipher)

# this won't be accurate as we do mod 26 when we create cipher text, we can't reverse that?
decipher = decrypt(cipher, key)
print("Deciphered text:", decipher)