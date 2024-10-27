def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    return gcd, y1 - (b // a) * x1, x1

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    return x % m if gcd == 1 else None

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

def rsa_key_generation(p, q, e):
    if not (is_prime(p) and is_prime(q)) or gcd(e, (p - 1) * (q - 1)) != 1:
        raise ValueError("Invalid inputs.")
    n = p * q
    d = mod_inverse(e, (p - 1) * (q - 1))
    return (e, n), (d, n)

def rsa_sign(message, d, n):
    return pow(message, d, n)

def rsa_verify(signature, e, n, message):
    return message == pow(signature, e, n)

def main():
    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))
    e = int(input("Enter public exponent e: "))
    
    try:
        public_key, private_key = rsa_key_generation(p, q, e)
        print(f"Public Key: {public_key}\nPrivate Key: {private_key}")
        
        message = int(input("Message to sign: "))
        signature = rsa_sign(message, private_key[0], private_key[1])
        print(f"Signature: {signature}")
        
        signature_input = int(input("Signature to verify: "))
        message_input = int(input("Message to verify: "))
        print("Authenticated" if rsa_verify(signature_input, public_key[0], public_key[1], message_input) else "Altered")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
