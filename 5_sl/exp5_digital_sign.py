def gcd(a, b):
    # Compute the Greatest Common Divisor (GCD) using the Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    # Extended Euclidean Algorithm to find gcd(a, b) and coefficients x and y
    if a == 0:
        return (b, 0, 1)  # Base case: gcd(a, b) = b, coefficients are 0 and 1
    gcd, x1, y1 = extended_gcd(b % a, a)  # Recursive call
    x = y1 - (b // a) * x1  # Update x using results of recursive call
    y = x1  # Update y
    return (gcd, x, y)

def mod_inverse(a, m):
    # Compute the modular inverse of a under modulo m
    gcd, x, _ = extended_gcd(a, m)  # Find gcd and coefficients
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")  # Inverse exists only if gcd is 1
    return x % m  # Ensure the result is positive

def rsa_key_generation(p, q, e):
    # Generate RSA public and private keys
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both p and q should be prime numbers.")  # Check if p and q are prime
    
    n = p * q  # Compute n = p * q
    phi = (p - 1) * (q - 1)  # Compute Euler's totient function φ(n)
    
    if gcd(e, phi) != 1:
        raise ValueError("e must be coprime with φ(n).")  # Check if e and φ(n) are coprime
    
    d = mod_inverse(e, phi)  # Compute the modular inverse of e mod φ(n), which is the private key exponent
    
    return (e, n), (d, n)  # Return the public and private key pairs

def is_prime(num):
    # Check if a number is prime
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if num <= 3:
        return True  # 2 and 3 are prime
    if num % 2 == 0 or num % 3 == 0:
        return False  # Divisible by 2 or 3 is not prime
    i = 5
    while i * i <= num:  # Check divisibility up to the square root of num
        if num % i == 0 or num % (i + 2) == 0:
            return False  # Found a divisor, so not prime
        i += 6
    return True

def rsa_sign(message, d, n):
    # Sign a message using the RSA private key
    return pow(message, d, n)  # Compute the signature: message^d mod n

def rsa_verify(signature, e, n, message):
    # Verify an RSA signature
    message_prime = pow(signature, e, n)  # Decrypt the signature: signature^e mod n
    return message == message_prime  # Check if the decrypted signature matches the original message

# Main execution logic
p = int(input("Enter the prime number p: "))  # Input prime number p
q = int(input("Enter the prime number q: "))  # Input prime number q
e = int(input("Enter the public exponent e: "))  # Input public exponent e

try:
    (e, n), (d, n) = rsa_key_generation(p, q, e)  # Generate RSA keys
    print(f"Public Key: ({e}, {n})")  # Display public key
    print(f"Private Key: ({d}, {n})")  # Display private key
    
    print("\n****SENDER****\n")
    message = int(input("Enter the message to be signed: "))  # Input message to sign
    signature = rsa_sign(message, d, n)  # Generate digital signature
    print(f"Digital Signature of message: {signature}")  # Display the signature
    
    print("\n****VERIFIER****\n")
    signature_input = int(input("Enter the signature to verify: "))  # Input signature for verification
    message_input = int(input("Enter the message to verify against the signature: "))  # Input message for verification
    verification = rsa_verify(signature_input, e, n, message_input)  # Verify the signature
    
    print("\n****RESULT****\n")
    if verification:
        print("The message is authenticated, Accept.")  # Signature is valid
    else:
        print("Message is altered. Discard.")  # Signature is invalid
except ValueError as ve:
    print(f"Error: {ve}")  # Handle any errors that occur
