def modular_exponentiation(base, exponent, modulus):
    #Perform modular exponentiation.
    return pow(base, exponent, modulus)

# Prompt the user for input values
q = int(input("Enter the prime number q: "))          # Prime number q, which should be a large prime
alpha = int(input("Enter the base (generator) α: "))  # Base (generator) α, which should be a primitive root modulo q

XA = int(input("Enter Alice's private key XA: "))     # Alice's private key XA, a secret integer known only to Alice
XB = int(input("Enter Bob's private key XB: "))       # Bob's private key XB, a secret integer known only to Bob

# Compute the public keys using modular exponentiation
YA = modular_exponentiation(alpha, XA, q)  # Alice's public key YA = α^XA mod q
YB = modular_exponentiation(alpha, XB, q)  # Bob's public key YB = α^XB mod q

print("\nOUTPUT:")
print(f"Alice's public key YA: {YA}")  # Output Alice's public key
print(f"Bob's public key YB: {YB}")    # Output Bob's public key

# Compute the shared secret using the public keys and private keys
SA = modular_exponentiation(YB, XA, q)  # Alice computes the shared secret SA = YB^XA mod q
SB = modular_exponentiation(YA, XB, q)  # Bob computes the shared secret SB = YA^XB mod q

print(f"Alice's shared secret SA: {SA}")  # Output Alice's computed shared secret
print(f"Bob's shared secret SB: {SB}")    # Output Bob's computed shared secret

# Verify that both Alice and Bob have computed the same shared secret
if SA == SB:
    print("Key exchange successful. Shared secret is the same for both parties.")
else:
    print("Key exchange failed. Shared secrets do not match.")
