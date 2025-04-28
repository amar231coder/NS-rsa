# NS-rsa
1. Introduction
RSA (Rivest–Shamir–Adleman) is a widely used public-key cryptographic algorithm that uses two different keys: a public key for encryption and a private key for decryption. It is based on the mathematical difficulty of factoring the product of two large prime numbers.

RSA is extensively used in securing data transmissions, digital signatures, and certificate-based authentication


The encrypted message will be different every time because RSA keys are freshly generated each time the program runs.

However, the decrypted message will always match the original message.

Explanation of the Implementation
Key Generation:

A 2048-bit RSA key pair is generated using the Crypto.PublicKey module.

The private key and public key are exported in PEM format.

Encryption:

The message is encrypted using the public key and PKCS1_OAEP cipher.

The encrypted binary is base64 encoded for easier readability and display.

Decryption:

The base64 encoded encrypted text is decoded back to binary.

It is decrypted using the private key to retrieve the original plaintext message.

Library Used:

pycryptodome — a self-contained Python package of low-level cryptographic primitives.

Security Note:

In practice, RSA is generally used to encrypt small pieces of data (like symmetric AES keys), not large data files, because RSA encryption is computationally expensive.
