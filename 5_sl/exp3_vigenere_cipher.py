def vigenere_encrypt(plaintext, keyword):
    # Convert both keyword and plaintext to uppercase for case insensitivity
    keyword = keyword.upper()
    plaintext = plaintext.upper()
    
    # Initialize an empty string to store the encrypted text
    cipher_text = ""
    
    # Start at the beginning of the keyword
    keyword_index = 0

    # Iterate over each character in the plaintext
    for char in plaintext:
        # Check if the character is a letter (ignore non-alphabetic characters)
        if char.isalpha():
            # Calculate the shift value based on the current keyword character
            shift = ord(keyword[keyword_index]) - ord('A')
            
            # Encrypt the character using the Vigenère cipher formula
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            
            # Append the encrypted character to the cipher_text
            cipher_text += encrypted_char
            
            # Move to the next character in the keyword, wrapping around if necessary
            keyword_index = (keyword_index + 1) % len(keyword)
    
    # Return the fully encrypted text
    return cipher_text

def vigenere_decrypt(cipher_text, keyword):
    # Convert both keyword and cipher_text to uppercase for case insensitivity
    keyword = keyword.upper()
    cipher_text = cipher_text.upper()
    
    # Initialize an empty string to store the decrypted text
    plaintext = ""
    
    # Start at the beginning of the keyword
    keyword_index = 0

    # Iterate over each character in the cipher text
    for char in cipher_text:
        # Check if the character is a letter (ignore non-alphabetic characters)
        if char.isalpha():
            # Calculate the shift value based on the current keyword character
            shift = ord(keyword[keyword_index]) - ord('A')
            
            # Decrypt the character by shifting it backwards using the Vigenère cipher formula
            decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            
            # Append the decrypted character to the plaintext
            plaintext += decrypted_char
            
            # Move to the next character in the keyword, wrapping around if necessary
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            # If the character is not a letter, append it as is
            plaintext += char
    
    # Return the fully decrypted text
    return plaintext

while True:
    # Display menu options to the user
    print("\nVIGENERE CIPHER \n1. Encrypt \n2. Decrypt \n3. Exit ")
    
    # Get the user's choice
    choice = int(input("Enter Your Choice: "))
    
    # Check if the user chose to encrypt text
    if choice == 1:
        # Get plaintext and keyword from the user
        text = input("Enter the plaintext: ")
        keyword = input("Enter the keyword: ")
        
        # Encrypt the text using the Vigenère cipher
        encrypted_text = vigenere_encrypt(text, keyword)
        
        # Display the encrypted text
        print(f"Encrypted Text: {encrypted_text}")
    
    # Check if the user chose to decrypt text
    elif choice == 2:
        # Get ciphertext and keyword from the user
        text = input("Enter the ciphertext: ")
        keyword = input("Enter the keyword: ")
        
        # Decrypt the text using the Vigenère cipher
        decrypted_text = vigenere_decrypt(text, keyword)
        
        # Display the decrypted text
        print(f"Decrypted Text: {decrypted_text}")
    
    # Check if the user chose to exit the program
    elif choice == 3:
        break
    
    # Handle invalid choices
    else:
        print("Invalid Choice")
