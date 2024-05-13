import math

# take 2 large prime numbers p and q
p = 1013
q = 1019

# message = int(input('Enter any number as message: '))
message = 31

n = p * q
phi = (p - 1) * (q - 1)

print("Value of p:", p)
print("Value of q:", q)
print("Value of n:", n)
print("Value of phi:", phi)

# conditions for e:
# e > 1 and e < phi
# e is coprime with phi (i.e. gcd of e and phi is 1)
# e != p and e != q preferably
e = 2
while e > 1 and e < phi and e != p and e != q:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1

# conditions for d:
# (d * e) mod phi = 1
# d < phi
d = 1
while d < phi:
    if (d * e) % phi == 1:
        break
    else:
        d += 1     

public = (e, n)
private = (d, n)

print('\nPublic key (e, n):', public)
print('Private key (d, n):', private)

cipher = pow(message, e) % n
decipher = pow(cipher, d) % n

print('\nCiphered text:', cipher)
print('Deciphered text:', decipher)