def shift_char(char, shift):
    return chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))

def vigenere(text, keyword, encrypt=True):
    keyword = keyword.upper()
    text = text.upper()
    result = ""
    keyword_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(keyword[keyword_index]) - ord('A')
            result += shift_char(char, shift if encrypt else -shift)
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            result += char
    
    return result

def main():
    while True:
        print("\nVIGENERE CIPHER \n1. Encrypt \n2. Decrypt \n3. Exit ")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            text = input("Enter the plaintext: ")
            keyword = input("Enter the keyword: ")
            print(f"Encrypted Text: {vigenere(text, keyword, encrypt=True)}")
        
        elif choice == 2:
            text = input("Enter the ciphertext: ")
            keyword = input("Enter the keyword: ")
            print(f"Decrypted Text: {vigenere(text, keyword, encrypt=False)}")
        
        elif choice == 3:
            break
        
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
