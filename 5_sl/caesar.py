def shift_char(ch, s):
    if ch.isupper():
        return chr((ord(ch) + s - 65) % 26 + 65)
    elif ch.islower():
        return chr((ord(ch) + s - 97) % 26 + 97)
    return ch

def process_text(text, s, encrypt=True):
    shifted_text = ""
    shift = s if encrypt else -s
    for ch in text:
        shifted_text += shift_char(ch, shift)
    return shifted_text

def bruteforce(text):
    for key in range(26):
        decrypted = process_text(text, key, encrypt=False)
        print(f'For shift key {key}: {decrypted}')

def main():
    print("Enter: \n1. Encrypt plaintext \n2. Decrypt ciphertext \n3. Brute force")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        text = input("Enter the plaintext: ")
        s = int(input("Enter the shift: "))
        print("Ciphertext:", process_text(text, s, encrypt=True))
    elif choice == 2:
        text = input("Enter the ciphertext: ")
        s = int(input("Enter the shift: "))
        print("Plaintext:", process_text(text, s, encrypt=False))
    elif choice == 3:
        c = input("Enter the ciphertext: ")
        bruteforce(c)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
