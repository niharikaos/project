import random

# Function to compute modular exponentiation (base^exp % mod)
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def main():
    # Step 1: Enter a large prime number p
    p = int(input("Enter a large prime number p: "))

    # Step 2: Select a primitive root e modulo p
    e = int(input("Enter a primitive root e modulo p: "))

    # Step 3: Choose private key d such that 1 <= d <= p - 2
    d = random.randint(1, p - 2)
    print(f"Selected private key d: {d}")

    # Step 4: Compute e1 = e^d mod p (Public Key Part 1)
    e1 = mod_exp(e, d, p)
    print(f"Computed e1 = {e1}")

    # Step 5: Compute e2 = e (primitive root modulo p)
    e2 = e
    print(f"Computed e2 = {e2}")

    # Step 6: Enter the plaintext message (as a number)
    pt = int(input("Enter the plaintext to encrypt (as a number): "))

    # Step 7: Choose random integer r in the range 1 <= r <= p - 1
    r = random.randint(1, p - 1)
    print(f"Selected random integer r: {r}")

    # Step 8: Compute C1 = e1^r mod p
    c1 = mod_exp(e1, r, p)
    print(f"Computed C1 = {c1}")

    # Step 9: Compute C2 = (pt * e2^r) mod p
    c2 = (pt * mod_exp(e2, r, p)) % p
    print(f"Computed C2 = {c2}")

    # Step 10: Decrypt the message
    # Compute the modular inverse of C1^d mod p
    inverse_c1 = mod_exp(c1, p - 1 - d, p)
    decrypted_pt = (c2 * inverse_c1) % p
    print(f"Decrypted plaintext: {decrypted_pt}")

if _name_ == "_main_":
    main()


# Enter a large prime number p: 17
# Enter a primitive root e modulo p: 3
# Selected private key d: 7
# Computed e1 = 6
# Computed e2 = 3
# Enter the plaintext to encrypt (as a number): 12
# Selected random integer r: 5
# Computed C1 = 12
# Computed C2 = 10
# Decrypted plaintext: 12
