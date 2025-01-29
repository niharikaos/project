rom Crypto.Util import number
import random
import binascii

def rsa():
    # Generate prime numbers p and q
    p = number.getPrime(1024)
    q = number.getPrime(1024)
    
    # Calculate N and phi
    N = p * q
    phi = (p - 1) * (q - 1)
    
    # Generate e such that e and phi are coprime and 0 < e < phi
    e = number.getPrime(512)
    while phi % e == 0 or e >= phi:
        e = number.getPrime(512)
    
    # Calculate d (private key) such that (d * e) % phi == 1
    d = pow(e, -1, phi)
    
    print("Prime number p:", p)
    print("Prime number q:", q)
    print("Public key is:", e)
    print("Private key is:", d)
    
    # User input for plain text
    plain_text = input("Enter the plain text: ")
    print("Encrypting String:", plain_text)

    # Convert the plain text to bytes and encrypt it using public key
    plain_bytes = plain_text.encode('utf-8')
    plain_int = int(binascii.hexlify(plain_bytes), 16)
    
    encrypted = pow(plain_int, e, N)

    # Decrypt the encrypted message using the private key
    decrypted_int = pow(encrypted, d, N)
    decrypted_bytes = hex(decrypted_int)[2:].encode('utf-8')
    
    # Convert the decrypted bytes back to string
    decrypted_text = bytes.fromhex(decrypted_bytes.decode('utf-8')).decode('utf-8')
    
    print("Encrypted Bytes:", list(str(encrypted)))
    print("Decrypted Bytes:", list(decrypted_bytes))
    print("Decrypted String:", decrypted_text)

if __name__ == "__main__":
    rsa()


# Prime number p: 257
# Prime number q: 263
# Public key is: 17
# Private key is: 19825
# Enter the plain text: Hello  
# Encrypting String: Hello
# Encrypted Bytes:[41959]
# Decrypted Bytes:[72,101,108,108,111]
# Decrypted String: Hello
