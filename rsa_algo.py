
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generate RSA Key Pair
def generate_keys():
    key = RSA.generate(2048)  # 2048-bit key size
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Encrypt a message using the public key
def encrypt_message(public_key, message):
    rsa_public_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_public_key)
    encrypted_message = cipher.encrypt(message.encode('utf-8'))
    return base64.b64encode(encrypted_message).decode('utf-8')

# Decrypt a message using the private key
def decrypt_message(private_key, encrypted_message):
    rsa_private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_private_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode('utf-8')

# Main code
if __name__ == "__main__":
    # Generate keys
    private_key, public_key = generate_keys()

    # Original message
    message = "Network Security Assignment RSA Implementation"

    print(f"Original Message: {message}")

    # Encrypt the message
    encrypted_msg = encrypt_message(public_key, message)
    print(f"Encrypted Message (Base64 Encoded): {encrypted_msg}")

    # Decrypt the message
    decrypted_msg = decrypt_message(private_key, encrypted_msg)
    print(f"Decrypted Message: {decrypted_msg}")
