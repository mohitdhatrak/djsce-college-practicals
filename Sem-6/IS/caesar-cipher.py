uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

def encrypt(text, shift):
    cipher = ""

    for char in text:
        if char in uppercase: # upper case letter
            position = (uppercase.index(char) + shift) % 26 # get index of char, then shift it to get new index
            cipher += uppercase[position]

        else: # lower case letter
            position = (lowercase.index(char) + shift) % 26
            cipher += lowercase[position]

    return cipher

def decrypt(text, shift):
    decipher = ""

    for char in text:
        if char in uppercase: # upper case letter
            position = (uppercase.index(char) - shift) % 26
            decipher += uppercase[position]

        else: # lower case letter
            position = (lowercase.index(char) - shift) % 26
            decipher += lowercase[position]

    return decipher

# message = input("Enter plain text: ")
message = "HelloWorld"

# shift = input("Enter shift value: ")
shift = 3

cipher = encrypt(message, shift)
print("Ciphered text:", cipher) 

decipher = decrypt(cipher, shift)
print("Deciphered text:", decipher)