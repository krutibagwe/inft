import re

# Preprocess the message by removing non-letters and converting to uppercase
def preprocess_message(msg):
    msg = re.sub(r'[^A-Z]', '', msg.upper())
    msg = msg.replace('J', 'I')
    return msg

# Construct the key square (5x5 grid) from the key
def create_key_matrix(key_phrase):
    key_phrase = re.sub(r'[^A-Z]', '', key_phrase.upper())
    key_phrase += 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matrix = []
    seen = set()
    for char in key_phrase:
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return matrix

# Get the row and column of a character in the key square
def locate_position(matrix, char):
    index = matrix.index(char)
    return divmod(index, 5)

# Encrypt the plaintext using the Playfair cipher technique
def playfair_encrypt(plain_text, key_phrase):
    plain_text = preprocess_message(plain_text)
    matrix = create_key_matrix(key_phrase)
    
    encrypted_result = []
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        b = plain_text[i + 1] if i + 1 < len(plain_text) else 'X'
        
        if a == b:
            b = 'X'
            i += 1
        else:
            i += 2
        
        row1, col1 = locate_position(matrix, a)
        row2, col2 = locate_position(matrix, b)
        
        if row1 == row2:
            encrypted_result.append(matrix[row1 * 5 + (col1 + 1) % 5])
            encrypted_result.append(matrix[row2 * 5 + (col2 + 1) % 5])
        elif col1 == col2:
            encrypted_result.append(matrix[((row1 + 1) % 5) * 5 + col1])
            encrypted_result.append(matrix[((row2 + 1) % 5) * 5 + col2])
        else:
            encrypted_result.append(matrix[row1 * 5 + col2])
            encrypted_result.append(matrix[row2 * 5 + col1])
    
    return ''.join(encrypted_result)

# Decrypt the ciphertext using the Playfair cipher technique
def playfair_decrypt(cipher_text, key_phrase):
    matrix = create_key_matrix(key_phrase)
    
    decrypted_result = []
    for i in range(0, len(cipher_text), 2):
        a = cipher_text[i]
        b = cipher_text[i + 1]
        
        row1, col1 = locate_position(matrix, a)
        row2, col2 = locate_position(matrix, b)
        
        if row1 == row2:
            decrypted_result.append(matrix[row1 * 5 + (col1 - 1) % 5])
            decrypted_result.append(matrix[row2 * 5 + (col2 - 1) % 5])
        elif col1 == col2:
            decrypted_result.append(matrix[((row1 - 1) % 5) * 5 + col1])
            decrypted_result.append(matrix[((row2 - 1) % 5) * 5 + col2])
        else:
            decrypted_result.append(matrix[row1 * 5 + col2])
            decrypted_result.append(matrix[row2 * 5 + col1])
    
    return ''.join(decrypted_result)

# Display the key square matrix
def show_key_matrix(matrix):
    print("Key Square Matrix:")
    for i in range(5):
        print(' '.join(matrix[i * 5:(i + 1) * 5]))

# Main function to handle user interaction
def main():
    while True:
        print("\nMenu:")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            text = input("Enter the plaintext: ")
            key_phrase = input("Enter the key: ")
            
            processed_text = preprocess_message(text)
            key_matrix = create_key_matrix(key_phrase)
            
            print("\nProcessed Plaintext:", processed_text)
            show_key_matrix(key_matrix)
            
            encrypted_message = playfair_encrypt(processed_text, key_phrase)
            print("\nEncrypted Message:", encrypted_message)
        
        elif choice == '2':
            text = input("Enter the ciphertext: ")
            key_phrase = input("Enter the key: ")
            
            processed_text = preprocess_message(text)
            key_matrix = create_key_matrix(key_phrase)
            
            print("\nProcessed Ciphertext:", processed_text)
            show_key_matrix(key_matrix)
            
            decrypted_message = playfair_decrypt(processed_text, key_phrase)
            print("\nDecrypted Message:", decrypted_message)
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option! Please try again.")

if __name__ == '__main__':
    main()
