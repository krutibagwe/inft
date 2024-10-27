def find_prime_factors(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return None, None

def calculate_phi(p, q):
    return (p - 1) * (q - 1)

def mod_inverse(e, phi_n):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        return gcd, y1 - (b // a) * x1, x1

    gcd, x, _ = extended_gcd(e, phi_n)
    return x % phi_n

def encrypt_decrypt(message, key, n, encrypt=True):
    return pow(message, key, n)

def setup_party(name):
    print(f"Party {name}:")
    e = int(input(f"Enter Party {name}'s public exponent e: "))
    n = int(input(f"Enter Party {name}'s modulus n: "))
    p, q = find_prime_factors(n)
    phi = calculate_phi(p, q)
    d = mod_inverse(e, phi)
    print(f"Prime factors of n: p = {p}, q = {q}")
    print(f"φ(n) = {phi}")
    print(f"Party {name}'s Private Key: d = {d}\n")
    return e, n, d

def main():
    e_A, n_A, d_A = setup_party("A (Alice)")
    e_B, n_B, d_B = setup_party("B (Bob)")

    M_A_to_B = int(input("Enter the message M that Party A wants to send to Party B: "))
    cipher_A_to_B = encrypt_decrypt(M_A_to_B, e_B, n_B)
    print(f"Cipher-text sent by A to B: {cipher_A_to_B}")
    decrypted_A_to_B = encrypt_decrypt(cipher_A_to_B, d_B, n_B, encrypt=False)
    print(f"B decrypts the cipher-text: {decrypted_A_to_B}\n")

    M_B_to_A = int(input("Enter the message M that Party B wants to send to Party A: "))
    cipher_B_to_A = encrypt_decrypt(M_B_to_A, e_A, n_A)
    print(f"Cipher-text sent by B to A: {cipher_B_to_A}")
    decrypted_B_to_A = encrypt_decrypt(cipher_B_to_A, d_A, n_A, encrypt=False)
    print(f"A decrypts the cipher-text: {decrypted_B_to_A}\n")

if __name__ == "__main__":
    main()
