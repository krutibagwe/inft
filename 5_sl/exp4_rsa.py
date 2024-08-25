# RSA Encryption and Decryption Program with User Interaction

# Function to find the prime factors of n
def find_prime_factors(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return None, None

# Function to calculate Euler's Totient function, phi(n)
def calculate_phi(p, q):
    return (p - 1) * (q - 1)

# Function to calculate the modular inverse using Extended Euclidean Algorithm
def mod_inverse(e, phi_n):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, _ = extended_gcd(e, phi_n)
    return x % phi_n

# Function to encrypt a message
def encrypt_message(M, e, n):
    return pow(M, e, n)

# Function to decrypt a message
def decrypt_message(C, d, n):
    return pow(C, d, n)

# Main Function
def main():
    # Step 1: Setup for Party A
    print("Party A: Alice")
    e_A = int(input("Enter Party A's public exponent e: "))
    n_A = int(input("Enter Party A's modulus n: "))
    p_A, q_A = find_prime_factors(n_A)
    phi_A = calculate_phi(p_A, q_A)
    d_A = mod_inverse(e_A, phi_A)
    print(f" Prime factors of n: p = {p_A}, q = {q_A}")
    print(f" φ(n) = {phi_A}")
    print(f" Party A's Private Key: d = {d_A}\n")

    # Step 2: Setup for Party B
    print("Party B: Bob")
    e_B = int(input("Enter Party B's public exponent e: "))
    n_B = int(input("Enter Party B's modulus n: "))
    p_B, q_B = find_prime_factors(n_B)
    phi_B = calculate_phi(p_B, q_B)
    d_B = mod_inverse(e_B, phi_B)
    print(f" Prime factors of n: p = {p_B}, q = {q_B}")
    print(f" φ(n) = {phi_B}")
    print(f" Party B's Private Key: d = {d_B}\n")

    # Step 3: A sends a message to B
    M_A_to_B = int(input("Enter the message M that Party A wants to send to Party B: "))
    cipher_A_to_B = encrypt_message(M_A_to_B, e_B, n_B)
    print(f" Cipher-text sent by A to B: {cipher_A_to_B}")
    decrypted_A_to_B = decrypt_message(cipher_A_to_B, d_B, n_B)
    print(f" B decrypts the cipher-text: {decrypted_A_to_B}\n")

    # Step 4: B sends a message to A
    M_B_to_A = int(input("Enter the message M that Party B wants to send to Party A: "))
    cipher_B_to_A = encrypt_message(M_B_to_A, e_A, n_A)
    print(f" Cipher-text sent by B to A: {cipher_B_to_A}")
    decrypted_B_to_A = decrypt_message(cipher_B_to_A, d_A, n_A)
    print(f" A decrypts the cipher-text: {decrypted_B_to_A}\n")

# Call the main function directly
main()
