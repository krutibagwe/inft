import re

def preprocess_message(msg):
    return re.sub(r'[^A-Z]', '', msg.upper()).replace('J', 'I')

def create_key_matrix(key_phrase):
    key_phrase = re.sub(r'[^A-Z]', '', key_phrase.upper()) + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    seen, matrix = set(), []
    for char in key_phrase:
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return matrix

def locate_position(matrix, char):
    return divmod(matrix.index(char), 5)

def playfair_process(text, key_phrase, encrypt=True):
    text = preprocess_message(text)
    matrix = create_key_matrix(key_phrase)
    result = []
    i = 0
    while i < len(text):
        a, b = text[i], text[i + 1] if i + 1 < len(text) else 'X'
        if a == b: b = 'X'; i += 1
        else: i += 2
        row1, col1 = locate_position(matrix, a)
        row2, col2 = locate_position(matrix, b)
        
        if row1 == row2:
            result.extend([matrix[row1 * 5 + (col1 + (1 if encrypt else -1)) % 5],
                           matrix[row2 * 5 + (col2 + (1 if encrypt else -1)) % 5]])
        elif col1 == col2:
            result.extend([matrix[((row1 + (1 if encrypt else -1)) % 5) * 5 + col1],
                           matrix[((row2 + (1 if encrypt else -1)) % 5) * 5 + col2]])
        else:
            result.extend([matrix[row1 * 5 + col2], matrix[row2 * 5 + col1]])
    return ''.join(result).replace('X', '')

def show_key_matrix(matrix):
    for i in range(0, 25, 5):
        print(' '.join(matrix[i:i + 5]))

def main():
    while True:
        choice = input("\n1. Encrypt\n2. Decrypt\n3. Exit\nChoose: ")
        if choice in {'1', '2'}:
            text = input("Enter text: ")
            key_phrase = input("Enter key: ")
            operation = playfair_process(text, key_phrase, encrypt=(choice == '1'))
            print(f"\n{'Encrypted' if choice == '1' else 'Decrypted'} Message: {operation}")
            show_key_matrix(create_key_matrix(key_phrase))
        elif choice == '3':
            break
        else:
            print("Invalid option!")

if __name__ == '__main__':
    main()
