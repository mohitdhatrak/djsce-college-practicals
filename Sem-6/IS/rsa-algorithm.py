p = 1013
q = 1019
# p = 3
# q = 11

# msg = 31
msg = int(input('Enter any number as message: '))

n = p * q
phi = (p - 1) * (q - 1)

# later get e value randomly?
# also add one more condition, e must not be equal to p or q generally
e = 13

d = 1
while True:
    if (d * e) % phi == 1:
        break
    else:
        d += 1     

public = (e, n)
private = (d, n)

print('Public key:', public)
print('Private key:', private)

cipher = pow(msg, e) % n
decipher = pow(cipher, d) % n

print('Ciphered text:', cipher)
print('Deciphered text:', decipher)