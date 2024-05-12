def encrypt(text, shift):
    cipher = ""

    for i in range(len(text)):
        char = text[i]

        if ord(char) >= 97: # lower case letter
            position = (ord(char) - 97 + shift) % 26 # -97 to get a range of 26 only, so we can use % 26
            cipher += chr(position + 97) # +97 to again get the shifted letter in lower case

        else: # upper case letter
            position = (ord(char) - 65 + shift) % 26 # -65 to get a range of 26 only, so we can use % 26
            cipher += chr(position + 65) # +65 to again get the shifted letter in upper case

    return cipher

def decrypt(text, shift):
    decipher = ""

    for i in range(len(text)):
        char = text[i]

        if ord(char) >= 97: # lower case letter
            position = (ord(char) - 97 - shift) % 26 # -97 to get a range of 26 only, so we can use % 26
            decipher += chr(position + 97) # +97 to again get the shifted letter in lower case

        else: # upper case letter
            position = (ord(char) - 65 - shift) % 26 # -65 to get a range of 26 only, so we can use % 26
            decipher += chr(position + 65) # +65 to again get the shifted letter in upper case

    return decipher

# message = input("Enter plain text: ")
message = "helloworld"

# shift = input("Enter shift value: ")
shift = 3

cipher = encrypt(message, shift)
print("Ciphered text:", cipher) 

decipher = decrypt(cipher, shift)
print("Deciphered text:", decipher) 