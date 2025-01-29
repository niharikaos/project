def mod_inverse(a, m):
    """Function to compute modular inverse of 'a' mod 26."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1  # No modular inverse exists

def affine_encrypt(plaintext, k1, k2):
    """Function to encrypt plaintext using Affine Cipher."""
    ciphertext = []
    for ch in plaintext:
        if ch.isalpha():
            ch = ch.upper()  # Convert to uppercase if it's lowercase
            gamma = (k1 * (ord(ch) - ord('A')) + k2) % 26  # Gamma = (P*k1 + k2) mod 26
            ciphertext.append(chr(gamma + ord('A')))
        else:
            ciphertext.append(ch)  # Non-alphabetic characters are not encrypted
    return ''.join(ciphertext)

def affine_decrypt(ciphertext, k1, k2):
    """Function to decrypt ciphertext using Affine Cipher."""
    k1_inverse = mod_inverse(k1, 26)
    if k1_inverse == -1:
        return "Error: 'k1' and 26 are not coprime, decryption not possible."
    
    plaintext = []
    for ch in ciphertext:
        if ch.isalpha():
            ch = ch.upper()  # Convert to uppercase if it's lowercase
            gamma = (ord(ch) - ord('A') - k2 + 26) % 26  # Gamma = (C - k2) mod 26
            pt = (k1_inverse * gamma) % 26  # P = (Gamma * k1^-1) mod 26
            plaintext.append(chr(pt + ord('A')))
        else:
            plaintext.append(ch)  # Non-alphabetic characters are not decrypted
    return ''.join(plaintext)

def main():
    # Input plaintext
    text = input("Enter the text to encrypt (uppercase letters only): ")

    # Input keys
    k1 = int(input("Enter the value of 'k1' (multiplicative key): "))
    k2 = int(input("Enter the value of 'k2' (additive key): "))

    # Encrypting the text
    encrypted_text = affine_encrypt(text, k1, k2)
    print(f"Encrypted Text: {encrypted_text}")

    # Decrypting the text
    decrypted_text = affine_decrypt(encrypted_text, k1, k2)
    print(f"Decrypted Text: {decrypted_text}")

if _name_ == "_main_":
    main()



# Enter the text to encrypt (uppercase letters only): HELLO
# Enter the value of 'k1' (multiplicative key): 5
# Enter the value of 'k2' (additive key): 8
# Encrypted Text: XUBBE
# Decrypted Text: HELLO
