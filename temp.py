import random
import string

class XOREncryptorDecryptor:
    def __init__(self, key: str):
        self.key = key

    def encrypt(self, message: str) -> str:
        """Encrypt the message using the key by XOR-ing each character with its corresponding key character
        and converting the result to a complex number.
        """
        encrypted_chars = [chr(ord(c) ^ ord(k)) for c, k in zip(message, self.key)]
        return [complex(ord(c)) for c in encrypted_chars]

    def decrypt(self, message: str) -> str:
        """Decrypt the message by converting the complex numbers back to characters and XOR-ing them with the key."""
        decrypted_chars = [chr(int(c.real)) for c in message]
        return "".join(chr(ord(c) ^ ord(k)) for c, k in zip(decrypted_chars, self.key))

def generate_random_string(length: int) -> str:
    """Generate a random string of the specified length using lowercase letters and digits."""
    letters_and_digits = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters_and_digits) for _ in range(length))

def main():
    # Generate a random key of length 100
    key = generate_random_string(100)
    
    # Create an encryptor/decryptor using the key
    encryptor_decryptor = XOREncryptorDecryptor(key)
    
    # Encrypt the message "Hello, World!" using the encryptor/decryptor
    encrypted_message = encryptor_decryptor.encrypt("Hello, World!")
    
    # Decrypt the encrypted message using the encryptor/decryptor
    decrypted_message = encryptor_decryptor.decrypt(encrypted_message)
    
    # Generate a random number between 0 and 1
    r = random.random()
    
    # If the random number is less than 0.5, print the encrypted message
    # otherwise, print the decrypted message again
    if r < 0.5:
        print(encrypted_message)
    else:
        print(decrypted_message)

if __name__ == "__main__":
    main()