import random
import string

class Cipher:
    def __init__(self):
        self.characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
        self.key = self.generate_key()

    def generate_key(self):
        shuffled_characters = random.sample(self.characters, len(self.characters))
        return dict(zip(self.characters, shuffled_characters))

    def encrypt(self, message):
        encrypted_message = ''.join(self.key.get(char, char) for char in message)
        return encrypted_message

    def decrypt(self, encrypted_message):
        reverse_key = {v: k for k, v in self.key.items()}
        decrypted_message = ''.join(reverse_key.get(char, char) for char in encrypted_message)
        return decrypted_message

def main():
    print("=== Encryption and Decryption ===")

    cipher = Cipher()

    message = input("Enter a message: ")

    encrypted_message = cipher.encrypt(message)

    print("\nEncryption Result:")
    print(f"Original message: {message}")
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = cipher.decrypt(encrypted_message)

    print("\nDecryption Result:")
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
