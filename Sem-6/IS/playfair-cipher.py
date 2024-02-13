import random

import numpy as np

# J not included
char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# make a random 5x5 matrix
mask = np.random.choice(char, size=(5, 5), replace=False)
print("Mask: \n", mask)

text = input("Enter plain text: ")

# if plain text has J replace it with I
text = text.upper().replace(" ", "")
modified_text = text.replace("J", "I")

unused_char = list(filter(lambda x: x.upper() not in modified_text, char))
print("Unused characters list: ", unused_char)

# to avoid same letter pairs - we add bogus char
# we remove the random char from list to avoid case like ['LR', 'LR'] pairs to be repeated
for i in range(len(text) - 1):
    pos = i
    if text[i] == text[i + 1]:
        random_char = random.choice(unused_char)
        modified_text = text[: pos + 1] + random_char + text[pos + 1 :]
        unused_char.remove(random_char)
    i += 1

# if string has odd length, add one char at end
if len(modified_text) % 2 != 0:
    random_char = random.choice(unused_char)
    modified_text = modified_text + random_char
    unused_char.remove(random_char)

print("Modified text:", modified_text)

# array of pair of 2 letters from text
result = [modified_text[i : i + 2] for i in range(0, len(modified_text), 2)]
print("Required pairs of text:", result)


# returns position of letter in 2d mask matrix as tuple
def get_element_position(arr, target):
    for i, row in enumerate(arr):
        for j, value in enumerate(row):
            if value == target:
                return (i, j)


cipher = ""

for pair in result:
    char1 = get_element_position(mask, pair[0])
    char2 = get_element_position(mask, pair[1])

    # same row case
    if char1[0] == char2[0]:
        common_row = char1[0]
        column1 = (char1[1] + 1) % 5
        column2 = (char2[1] + 1) % 5
        cipher += mask[common_row][column1] + mask[common_row][column2]

    # same column case
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

print("Ciphered text:", cipher)
