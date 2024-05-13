alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text, key):
    cipher = ""

    for char1, char2 in zip(text, key):  
        position = (alphabets.index(char1) + alphabets.index(char2)) % 26
        cipher += alphabets[position]

    return cipher

def decrypt(text, key):
    decipher = ""

    for char1, char2 in zip(text, key):  
        position = (alphabets.index(char1) - alphabets.index(char2)) % 26
        decipher += alphabets[position] 

    return decipher

# message = input("Enter plain text: ")
message = "helloworld"
message = message.upper()

# key = input("Enter key value: ")
key = "son"
key = key.upper()

modified_key = key
if len(message) - len(key) > 0:
    for i in range(0, len(message) - len(key)):
        modified_key += modified_key[i]

    print("Modified key:", modified_key)
            
cipher = encrypt(message, modified_key)
print("Ciphered text:", cipher)

decipher = decrypt(cipher, modified_key)    
print("Deciphered text:", decipher)