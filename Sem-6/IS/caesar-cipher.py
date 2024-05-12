def encrypt(text, shift):
    cipher = ""

    for i in range(len(text)):
        char = text[i]

        if char in uppercase_alphabets: # upper case letter
            position = (uppercase_alphabets.index(char) + shift) % 26 # get index of char, then shift it to get new index
            cipher += uppercase_alphabets[position]

        else: # lower case letter
            position = (lowercase_alphabets.index(char) + shift) % 26
            cipher += lowercase_alphabets[position]

    return cipher

def decrypt(text, shift):
    decipher = ""

    for i in range(len(text)):
        char = text[i]

        if char in uppercase_alphabets: # upper case letter
            position = (uppercase_alphabets.index(char) - shift) % 26
            decipher += uppercase_alphabets[position]

        else: # lower case letter
            position = (lowercase_alphabets.index(char) - shift) % 26
            decipher += lowercase_alphabets[position]

    return decipher

uppercase_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_alphabets = "abcdefghijklmnopqrstuvwxyz"

# message = input("Enter plain text: ")
message = "helloworld"

# shift = input("Enter shift value: ")
shift = 3

cipher = encrypt(message, shift)
print("Ciphered text:", cipher) 

decipher = decrypt(cipher, shift)
print("Deciphered text:", decipher)