from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import os

def encrypt_file(file_bytes, public_key_path="keys/public.pem"):
    # Load RSA Public Key
    public_key = RSA.import_key(open(public_key_path).read())
    rsa_cipher = PKCS1_OAEP.new(public_key)

    # AES Key
    aes_key = get_random_bytes(16)

    # Encrypt AES key with RSA Public Key
    encrypted_aes_key = rsa_cipher.encrypt(aes_key)

    # AES Encryption
    aes_cipher = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = aes_cipher.encrypt_and_digest(file_bytes)

    return encrypted_aes_key, aes_cipher.nonce, tag, ciphertext


def decrypt_file(encrypted_aes_key, nonce, tag, ciphertext,
                 private_key_path="keys/private.pem"):

    # Load RSA Private Key
    private_key = RSA.import_key(open(private_key_path).read())
    rsa_cipher = PKCS1_OAEP.new(private_key)

    # Decrypt AES Key
    aes_key = rsa_cipher.decrypt(encrypted_aes_key)

    # AES Decryption
    aes_cipher = AES.new(aes_key, AES.MODE_EAX, nonce)
    plaintext = aes_cipher.decrypt_and_verify(ciphertext, tag)

    return plaintext
