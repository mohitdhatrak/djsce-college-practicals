import random


# returns position of letter in 5x5 mask matrix as tuple
def get_element_position(arr, target):
    for i, row in enumerate(arr):
        for j, value in enumerate(row):
            if value == target:
                return (i, j)

def encrypt(mask, digraph_arr):
    cipher = ""

    for pair in digraph_arr:
        # char 1 and char 2 are like coordinates (x, y)
        char1 = get_element_position(mask, pair[0])
        char2 = get_element_position(mask, pair[1])

        # same row case (x coordinate is same)
        if char1[0] == char2[0]:
            common_row = char1[0]
            column1 = (char1[1] + 1) % 5
            column2 = (char2[1] + 1) % 5
            cipher += mask[common_row][column1] + mask[common_row][column2]

        # same column case (y coordinate is same)
        elif char1[1] == char2[1]:
            common_column = char1[1]
            row1 = (char1[0] + 1) % 5
            row2 = (char2[0] + 1) % 5
            cipher += mask[row1][common_column] + mask[row2][common_column]

        # both row and column different case
        # row remains same, column becomes column of other char
        else:
            row1 = char1[0]
            column1 = char2[1]
            row2 = char2[0]
            column2 = char1[1]
            cipher += mask[row1][column1] + mask[row2][column2]

    return cipher
    
def decrypt(mask, digraph_arr):
    decipher = ""

    for pair in digraph_arr:
        # char 1 and char 2 are like coordinates (x, y)
        char1 = get_element_position(mask, pair[0])
        char2 = get_element_position(mask, pair[1])

        # same row case (x coordinate is same)
        if char1[0] == char2[0]:
            common_row = char1[0]
            column1 = (char1[1] - 1) % 5
            column2 = (char2[1] - 1) % 5
            decipher += mask[common_row][column1] + mask[common_row][column2]

        # same column case (y coordinate is same)
        elif char1[1] == char2[1]:
            common_column = char1[1]
            row1 = (char1[0] - 1) % 5
            row2 = (char2[0] - 1) % 5
            decipher += mask[row1][common_column] + mask[row2][common_column]

        # both row and column different case
        # row remains same, column becomes column of other char
        else:
            row1 = char1[0]
            column1 = char2[1]
            row2 = char2[0]
            column2 = char1[1]
            decipher += mask[row1][column1] + mask[row2][column2]

    return decipher

# J not included
char = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

# key = input("Enter key: ")
key = "monarchyyy"

# if key has J replace it with I
key = key.upper().replace(" ", "") # remove space char
modified_key = key.replace("J", "I")
print("Key:", modified_key)

# removing duplicate char from modified_key
unique_char_in_key = []
for letter in modified_key:
  if (letter not in unique_char_in_key):
    unique_char_in_key.append(letter)

char_not_in_key = list(filter(lambda x: x not in unique_char_in_key, char))
mask_char = unique_char_in_key + char_not_in_key

# make a random 5x5 matrix
mask = []
for i in range(5):
    arr = []
    index = 5 * i

    for j in range(5):
        arr.append(mask_char[index + j])

    mask.append(arr)

print("\nMask:", end="")
for row in mask:
    print("\t", end="")
    for letter in row:
        print(letter, end=" ")
    print()

# text = input("Enter plain text: ")
text = "hello world"

# if plain text has J replace it with I
text = text.upper().replace(" ", "") # remove space char
modified_text = text.replace("J", "I")
print("\nPlain text:", modified_text)

char_not_in_text = list(filter(lambda x: x not in modified_text, char))
print("List of characters not used in plain text:", char_not_in_text)

# to avoid same letter pairs - we add bogus char
# we remove the used bogus char from the above list to avoid case like ['LR', 'LR'] i.e. pairs to be repeated
for i in range(len(text) - 1):
    position = i
    if text[i] == text[i + 1]:
        random_char = random.choice(char_not_in_text)
        modified_text = modified_text[: position + 1] + random_char + modified_text[position + 1 :]
        char_not_in_text.remove(random_char)

# if string has odd length, add one char at end
if len(modified_text) % 2 != 0:
    random_char = random.choice(char_not_in_text)
    modified_text = modified_text + random_char
    char_not_in_text.remove(random_char)

print("\nText after adding bogus letters:", modified_text)

# array of pair of 2 letters from text (array of digraphs)
digraph_arr = [modified_text[i : i + 2] for i in range(0, len(modified_text), 2)] # 3rd param in range is 'step', so i increments by 2
print("Digraphs of text:", digraph_arr)

cipher = encrypt(mask, digraph_arr)
print("\nCiphered text:", cipher)

cipher_digraph_arr = [cipher[i : i + 2] for i in range(0, len(cipher), 2)] # 3rd param in range is 'step', so i increments by 2

decipher = decrypt(mask, cipher_digraph_arr)
print("\nDeciphered text:", decipher)