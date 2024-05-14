# def left_shift(x,n):
#     return ((x<<n) | (x-32>>n))&0xFFFFFFFF

# def md5(message):
#     #step1 and step2: add padding and append length
#     padding_length=0

#     if(len(message)+64)%512:
#         message+="1"
#         padding_length=512-(len(message)+64)%512
#     message+="0"*padding_length
#     print("Padding length ",padding_length+1)
    
#     # step 3 divide the text into 512 bit blocks
#     message_worded=[int(message[i:i+32],2) for i in range(0,len(message),32)]
#     original_length=len(message)-64
#     message_worded.append(original_length)
    
#     # step 4 initializing chaining variables
#     a,b,c,d=[0x01234567,0x89ABCDEF,0xFEDCBA98,0x7654321]
#     print(f"Chainin variables are {a} {b} {c} {d}")
    
#     def F(x,y,z):
#         return (x&y)| (~x &z)
#     # step 5 process block
#     for i in range(0,len(message_worded),16):
#         f=F(b,c,d)
#         g=(i>>2)&0x03
#         for j in range(0,16):
#             if(i+j<len(message_worded)):
#                 temp=(a+f+g+message_worded[i+j])&0xFFFFFFFF
#                 a=d
#                 d=c
#                 c=b
#                 b+=left_shift(temp,7)
#     digest=format(a,"08x")
#     digest+=format(b,"08x")
#     digest+=format(c,"08x")
#     digest+=format(d,"08x")
    
#     return digest
        
# import random

# random_message="".join([random.choice(["0","1"]) for _ in range(1000)])
# print("random message of 1000 bits ",random_message)
# after_first_round=md5(random_message)
# print("after first round ",after_first_round)

import random


def text_to_binary(text):
    binary = ''
    for char in text:
        binary += ''.join(format(ord(char), '08b'))
    return binary

def add_padding(message):
    original_length = len(message)
    padding_bits = (64 - (original_length + 1) % 64) % 64 - 8
    padded_message = message + '1' + '0' * padding_bits
    padded_message += format(original_length, '08b')
    return padded_message

def get_16_sub_blocks(block):
    sub_blocks = []
    for i in range(0, len(block), 4):
        sub_blocks.append(block[i:i+4])
    return sub_blocks

def get_blocks(padded_message):
    blocks = []
    for i in range(0, len(padded_message), 64):
        blocks.append(padded_message[i:i+64])
    return blocks

def process_f(i, A, B, C, D):
    if i == 0:
        return str((int(A, 2) & int(B, 2)) | (~int(A, 2) & int(D, 2)))
    elif i == 1:
        return str((int(A, 2) & int(D, 2)) | (int(B, 2) & ~int(D, 2)))
    elif i == 2:
        return str(int(A, 2) ^ int(B, 2) ^ int(D, 2))
    else:
        return str(int(B, 2) ^ (int(A, 2) | ~int(D, 2)))

def circular_left_shift(binary_number, s):
    return binary_number[s:] + binary_number[:s]

def md5_hashing(padded_message):
    A = '1101'
    B = '1010'
    C = '0110'
    D = '1111'
    
    # Constants initialization
    K = [format(random.randint(0, 15), '04b') for _ in range(16)]
    
    blocks = get_blocks(padded_message)
    for block in blocks:
        sub_blocks = get_16_sub_blocks(block)
        for i in range(4):
            output_f = '' 
            output_f += process_f(i, A, B, C, D)
            output_f += A  
            for j in range(16):
                output_f += sub_blocks[j]
                output_f += K[j]
                output_f = circular_left_shift(output_f, 4)
                output_f += B  
                A, B, C, D = D, A, B, C
                
    hash_value = A + B + C + D
    return hash_value

# Example usage
message = "This is a test"
message_binary = text_to_binary(message)
print("Original binary message:", message_binary)
padded_message = add_padding(message_binary)  
print("Padded binary message:", padded_message)
print("Padded message length:", len(padded_message))

# Call md5_hashing with padded_message
hash_value = md5_hashing(padded_message)
print("Hash value:", hash_value)