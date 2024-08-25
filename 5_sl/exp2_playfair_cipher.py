print("\n1. Encrypt using Playfair Cipher \n2. Decrypt using Playfair Cipher")

# Get user's choice for encryption or decryption
choice = int(input("Enter your choice: "))

# Convert text to lowercase
def toLowerCase(text):
    return text.lower()

# Remove all spaces from the text
def removeSpaces(text):
    return text.replace(" ", "")

# Prepare text for encryption/decryption by formatting it into digraphs
def prepareText(text):
    text = removeSpaces(toLowerCase(text))  # Remove spaces and convert to lowercase
    prepared_text = []
    i = 0
    while i < len(text):
        # Add a letter to the prepared text
        prepared_text.append(text[i])
        if i + 1 < len(text):
            # If the next letter is the same, add a bogus letter 'x' between them
            if text[i] == text[i + 1]:
                prepared_text.append('x')
            else:
                # Add the next letter if it's different
                prepared_text.append(text[i + 1])
            i += 2  # Move to the next pair of letters
        else:
            i += 1
    # Handle odd length by adding a bogus letter at the end
    if len(prepared_text) % 2 != 0:
        prepared_text.append('x')
    return ''.join(prepared_text)

# Generate the key table used for encryption/decryption
def generateKeyTable(key):
    key = toLowerCase(key).replace('j', 'i')  # Treat 'j' as 'i'
    key = ''.join(sorted(set(key), key=key.index))  # Remove duplicates, preserve order
    list1 = 'abcdefghiklmnopqrstuvwxyz'
    table = ''.join(sorted(set(list1) - set(key)))  # Add missing letters
    return [list(key + table)[i:i + 5] for i in range(0, 25, 5)]  # Create a 5x5 matrix

# Print the key table matrix
def printMatrix(matrix):
    print("Key Table Matrix:")
    for row in matrix:
        print(' '.join(row))
    print()

# Find the position of a character in the matrix
def search(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    raise ValueError(f"Character {char} not found in the matrix.")

# Encrypt the text using the Playfair cipher
def encrypt(matrix, text):
    def getPair(x1, y1, x2, y2):
        # Find the encrypted pair based on their positions
        if x1 == x2:
            return matrix[x1][(y1 + 1) % 5] + matrix[x2][(y2 + 1) % 5]
        elif y1 == y2:
            return matrix[(x1 + 1) % 5][y1] + matrix[(x2 + 1) % 5][y2]
        else:
            return matrix[x1][y2] + matrix[x2][y1]
    
    # Split the text into digraphs (pairs of letters)
    digraphs = [text[i:i + 2] for i in range(0, len(text), 2)]
    cipher_text = ""
    for digraph in digraphs:
        x1, y1 = search(matrix, digraph[0])
        x2, y2 = search(matrix, digraph[1])
        cipher_text += getPair(x1, y1, x2, y2)  # Encrypt each pair
    return cipher_text

# Decrypt the text using the Playfair cipher
def decrypt(matrix, text):
    def getPair(x1, y1, x2, y2):
        # Find the decrypted pair based on their positions
        if x1 == x2:
            return matrix[x1][(y1 - 1) % 5] + matrix[x2][(y2 - 1) % 5]
        elif y1 == y2:
            return matrix[(x1 - 1) % 5][y1] + matrix[(x2 - 1) % 5][y2]
        else:
            return matrix[x1][y2] + matrix[x2][y1]
    
    # Split the text into digraphs (pairs of letters)
    digraphs = [text[i:i + 2] for i in range(0, len(text), 2)]
    plain_text = ""
    for digraph in digraphs:
        x1, y1 = search(matrix, digraph[0])
        x2, y2 = search(matrix, digraph[1])
        plain_text += getPair(x1, y1, x2, y2)  # Decrypt each pair
    
    # Handle the removal of bogus letters
    final_plain_text = []
    i = 0
    while i < len(plain_text):
        final_plain_text.append(plain_text[i])
        if i + 1 < len(plain_text) and plain_text[i] == plain_text[i + 1]:
            if plain_text[i + 1] == 'x':
                final_plain_text.pop()  # Remove the bogus letter
            else:
                final_plain_text.append(plain_text[i + 1])
            i += 1
        i += 1
    return ''.join(final_plain_text).rstrip('x')

# Based on the user's choice, either encrypt or decrypt the text
if choice == 1:
    text_plain = input("Enter the plain text: ")
    key = input("Enter the key: ")
    matrix = generateKeyTable(key)  # Generate key table matrix
    printMatrix(matrix)  # Print the matrix
    prepared_text = prepareText(text_plain)
    cipher_text = encrypt(matrix, prepared_text)  # Encrypt the text
    # Display results
    print("Key text:", key)
    print("Plain Text:", text_plain)
    print("Cipher Text:", cipher_text)
elif choice == 2:
    text_cipher = input("Enter the cipher text: ")
    key = input("Enter the key: ")
    matrix = generateKeyTable(key)  # Generate key table matrix
    printMatrix(matrix)  # Print the matrix
    prepared_text = removeSpaces(toLowerCase(text_cipher))
    plain_text = decrypt(matrix, prepared_text)  # Decrypt the text
    # Display results
    print("Key text:", key)
    print("Cipher Text:", text_cipher)
    print("Plain Text:", plain_text)
else:
    print("Invalid choice.")  # Handle invalid choices
