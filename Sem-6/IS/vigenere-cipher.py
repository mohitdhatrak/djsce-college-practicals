plain = input("Enter plain text: ")
key = input("Enter key value: ")

cipher = ""
decipher = ""

if len(plain) - len(key) > 0:
    for i in range(0, len(plain) - len(key)):
        key += key[i]
        
    print("Modified key:", key)
            
for i in range(0, len(plain)):
    encrypt = (ord(plain[i]) + ord(key[i])) % 128
    cipher += chr(encrypt)
    
print("Ciphered text:", cipher)

for i in range(0, len(plain)):
    decrypt = (ord(cipher[i]) - ord(key[i])) % 128
    decipher += chr(decrypt)      
    
print("Deciphered text:", decipher)