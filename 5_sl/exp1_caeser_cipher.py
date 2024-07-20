print("Enter: \n1. Encrypt plaintext \n2. Decrypt ciphertext \n3. Brute force")

choice = int(input("Enter your choice: "))

def encrypt(text, s):
    print("\nPlaintext:", text)
    print("Shift key:", s)
    ans = ""

    for ch in text:
        #if the character is uppercase
        if ch.isupper():
            # Convert the character to its ASCII code, shift it by 's' positions,
            # subtract 65 to map it into the range 0-25 (where 'A' starts at 65 in ASCII),
            # take modulo 26 to use circular list of alphabets
            # add 65 back to convert it back to ASCII code of uppercase letters.
            ans += chr((ord(ch) + s - 65) % 26 + 65)
        #if the character is lowercase
        elif ch.islower():
            # Convert the character to its ASCII code, shift it by 's' positions,
            # subtract 97 to map it into the range 0-25 (where 'a' starts at 97 in ASCII),
            # take modulo 26 to use circular list of alphabets
            # add 97 back to convert it back to ASCII code of lowercase letters.
            ans += chr((ord(ch) + s - 97) % 26 + 97)
        #to keep symbols unchanged
        else:
             # For symbols and spaces, simply append them to the result unchanged.
            ans += ch
    
    print("Ciphertext:", ans.upper())

def decrypt(text, s):
    print("\nCiphertext:", text)
    print("Shift key:", s)
    ans = ""

    for ch in text:
        #if the character is uppercase
        if ch.isupper():
            # Convert character to ASCII, shift 'ch' back by 's' positions,
            # use modulo 26 for circular list of alphabets, convert back to ASCII
            ans += chr((ord(ch) - s - 65) % 26 + 65)
        #if the character is lowercase
        elif ch.islower():
            # Convert character to ASCII, shift 'ch' back by 's' positions,
            # use modulo 26 for circular list of alphabets, convert back to ASCII
            ans += chr((ord(ch) - s - 97) % 26 + 97)
        #to keep symbols unchanged
        else:
            # For symbols and spaces, simply append them to the result unchanged.
            ans += ch
    
    print("Plaintext:", ans.lower())

def brutef(text):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #to convert text to uppercase for simplicity
    text = text.upper()
    
    # Iterate through all possible shift keys (0 to 25)
    for key in range(26):
        translated = ''
        for ch in text:
            if ch in letters:
                # Find the position (index) of the character 'ch' in the alphabet
                num = letters.find(ch)
                # Apply the reverse shift using the current key
                # Shift the character back by 'key' positions
                # use modulo 26 for circular list of alphabets
                num = (num - key) % 26
                # Append the decrypted character to the answer string
                translated += letters[num]
            else:
                # Append symbols and spaces unchanged
                translated += ch
        print('For shift key %d: %s' % (key, translated))


if choice == 1:
    text = input("Enter the plaintext: ")
    s = int(input("Enter the shift: "))
    encrypt(text, s)
elif choice == 2:
    text = input("Enter the ciphertext: ")
    s = int(input("Enter the shift: "))
    decrypt(text, s)
elif choice == 3:
    c = input("Enter the ciphertext: ")
    brutef(c)
else:
    print("Invalid choice!")
