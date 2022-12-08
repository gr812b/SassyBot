import itertools
import random
import string

n = 5

# Generate all possible keys of length 100 by combining all lowercase letters and digits
all_keys = [''.join(key) for key in itertools.product(string.ascii_lowercase + string.digits, repeat=n)]

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
    key = generate_random_string(n)
    # Encrypt the message "Hello, World!" using the random key
    encryptor_decryptor = XOREncryptorDecryptor(key)
    encrypted_message = encryptor_decryptor.encrypt("Hello, World!")
    print("encrypted_message:", encrypted_message)
    
    # Try all possible keys to see if any of them decrypt the message
    for key in all_keys:
        encryptor_decryptor = XOREncryptorDecryptor(key)
        decrypted_message = encryptor_decryptor.decrypt(encrypted_message)
        #print(decrypted_message)
        if decrypted_message == "Hello":
            # If a key is found that decrypts the message, print  it and return
            print(f"Key found: {key}")
            r = random.random()
            if r < 0.5:
                print(decrypted_message)
            else:
                print(decrypted_message)
            return
    
    # If no key is found that decrypts the message, print an error message
    print("No key found that decrypts the message")

if __name__ == "__main__":
    main()