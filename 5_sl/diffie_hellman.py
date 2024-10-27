def modular_exponentiation(base, exponent, modulus):
    return pow(base, exponent, modulus)

q = int(input("Enter the prime number q: "))
alpha = int(input("Enter the base (generator) α: "))
XA = int(input("Enter Alice's private key XA: "))
XB = int(input("Enter Bob's private key XB: "))

YA = modular_exponentiation(alpha, XA, q)
YB = modular_exponentiation(alpha, XB, q)

print("\nOUTPUT:")
print(f"Alice's public key YA: {YA}")
print(f"Bob's public key YB: {YB}")

SA = modular_exponentiation(YB, XA, q)
SB = modular_exponentiation(YA, XB, q)

print(f"Alice's shared secret SA: {SA}")
print(f"Bob's shared secret SB: {SB}")

if SA == SB:
    print("Key exchange successful. Shared secret is the same for both parties.")
else:
    print("Key exchange failed. Shared secrets do not match.")
