import string

class Cipher:
    def __init__(self):
        self.ALPHABET = list(string.printable)
        self.ALPHA_SIZE = len(self.ALPHABET)

    def validate(self, text):
        return ''.join([char for char in text if char in self.ALPHABET])

    def get_positions(self, key):
        return [self.ALPHABET.index(char) for char in key]

    def encrypt(self, text, key):
        text = self.validate(text)
        key = self.validate(key)

        if not key:
            raise ValueError("Key must not be empty.")

        shift = self.get_positions(key)
        result = []

        for i, char in enumerate(text):
            index = self.ALPHABET.index(char)
            shift_value = shift[i % len(key)]
            encrypted_char = self.ALPHABET[(index + shift_value) % self.ALPHA_SIZE]
            result.append(encrypted_char)

        return ''.join(result)

    def decrypt(self, text, key):
        text = self.validate(text)
        key = self.validate(key)

        if not key:
            raise ValueError("Key must not be empty.")

        shift = self.get_positions(key)
        result = []

        for i, char in enumerate(text):
            index = self.ALPHABET.index(char)
            shift_value = shift[i % len(key)]
            decrypted_char = self.ALPHABET[(index - shift_value) % self.ALPHA_SIZE]
            result.append(decrypted_char)

        return ''.join(result)


# Example usage
if __name__ == "__main__":
    cipher = Cipher()

    plaintext = input("Input your plaintext: ")
    key = input("Input your key: ")

    encrypted_text = cipher.encrypt(plaintext, key)
    print(f"Encrypted: {encrypted_text}")  

    decrypted_text = cipher.decrypt(plaintext, key)
    print(f"Decrypted: {decrypted_text}")
