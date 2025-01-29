# Function to encrypt text using Vigenère Cipher
def vigenere_encrypt(plaintext, key):
    encrypted_text = []
    key_len = len(key)
    j = 0
    for i in range(len(plaintext)):
        p_char = plaintext[i]
        if p_char.isalpha():
            offset = ord('A') if p_char.isupper() else ord('a')
            encrypted_text.append(chr(((ord(p_char) - offset + ord(key[j % key_len]) - ord('A')) % 26) + offset))
            j += 1
        else:
            encrypted_text.append(p_char)  # Non-alphabet characters are added without change
    return ''.join(encrypted_text)


# Function to decrypt text using Vigenère Cipher
def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_len = len(key)
    j = 0
    for i in range(len(ciphertext)):
        c_char = ciphertext[i]
        if c_char.isalpha():
            offset = ord('A') if c_char.isupper() else ord('a')
            decrypted_text.append(chr(((ord(c_char) - offset - (ord(key[j % key_len]) - ord('A')) + 26) % 26) + offset))
            j += 1
        else:
            decrypted_text.append(c_char)  # Non-alphabet characters are added without change
    return ''.join(decrypted_text)


def main():
    # Take input text and key from the user
    text = input("Enter the text to encrypt (uppercase letters only): ").upper()  # Ensure the text is in uppercase
    key = input("Enter the key (uppercase letters only): ").upper()  # Ensure the key is in uppercase

    # Encrypt the message
    encrypted_text = vigenere_encrypt(text, key)
    print("Encrypted Text:", encrypted_text)

    # Decrypt the message
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)


if _name_ == "_main_":
    main()



# Enter the text to encrypt (uppercase letters only): ABCD
# Enter the key (uppercase letters only): 5
# Encrypted Text: OPQR
# Decrypted Text: ABCD