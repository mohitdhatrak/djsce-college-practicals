import hashlib
import math


def generate_rsa_keys(p, q, phi):
    e = 2
    while e > 1 and e < phi and e != p and e != q:
        if math.gcd(e, phi) == 1:
            break
        else:
            e += 1

    d = 1
    while d < phi:
        if (d * e) % phi == 1:
            break
        else:
            d += 1     

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def sign_message(message, private_key):
    d, n = private_key
    md1 = int(hashlib.md5(message.encode()).hexdigest(), 16) % n
    print("\nMD1 Hash:", md1)
    signature = pow(md1, d) % n # encrypt with private key
    return signature, md1

def verify_sign(message, signature, public_key):
    e, n = public_key
    md2 = int(hashlib.md5(message.encode()).hexdigest(), 16) % n
    print("MD2 Hash:", md2)
    recovered_hash = pow(signature, e) % n # decrypt with public key
    print("Recovered Hash:", recovered_hash)
    return recovered_hash, md2

# perform RSA algorithm to get e and d OR directly assume e and d values
p = 1013
q = 1019

n = p * q
phi = (p - 1) * (q - 1)

# generate RSA keys
public_key, private_key = generate_rsa_keys(p, q, phi)
print("Public key (e, n):", public_key)
print("Private key (d, n):", private_key)

# in rsa signature scheme, creating digital signature is the important part as any random person should not be able to create a valid digital signature
# so here, we encrypt the message with private key to get signature (and decrypt with public key)

# sign the message
original_message = "Send 500 rupees" 
altered_message = "Send 50000 rupees 😝"
print("\nMessage 1:", original_message)
print("Message 2:", altered_message)
signature, md1 = sign_message(original_message, private_key)
print("Signature:", signature)

# verify the signature for both messages
print("\nVerifying authenticity of message:", original_message)
recovered_hash, md2 = verify_sign(original_message, signature, public_key)
if recovered_hash == md2:
    print("Signature is valid, message is valid and from trusted source")
else:
    print("Signature is not valid, message might be altered")

print("\nVerifying authenticity of message:", altered_message)
recovered_hash, md2 = verify_sign(altered_message, signature, public_key)
if recovered_hash == md2:
    print("Signature is valid, message is valid and from trusted source")
else:
    print("Signature is not valid, message might be altered")