plain = input("Enter plain text: ")
print("Length of plain text is", len(plain))

cipher = ""
decipher = ""

# issue - maybe key needs to be generated randomly of same size, not to ask user key
# key has to be random and not to be reused
key = input("Enter key value (length same as plain text): ")
print("Length of key is", len(key))

if len(key) != len(plain):
    print("Error! Length of key is not same as plain text!")
else:
    for i in range(0, len(plain)):
        encrypt = ord(plain[i]) ^ ord(key[i])
        cipher += chr(encrypt)

    print("Ciphered text:", cipher)

    for i in range(0, len(plain)):
        decrypt = ord(cipher[i]) ^ ord(key[i])
        decipher += chr(decrypt)

    print("Deciphered text:", decipher)
