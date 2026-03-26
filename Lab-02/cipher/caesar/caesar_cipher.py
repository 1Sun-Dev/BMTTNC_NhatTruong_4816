from cipher.caesar import Alphabet

class CaesarCipher:

    def __init__(self):
        self.alphabet = Alphabet

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_index = (letter_index + key) % alphabet_len
            output_letter = self.alphabet[output_index]
            encrypted.append(output_letter)
        return "".join(encrypted)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_index = (letter_index - key) % alphabet_len
            output_letter = self.alphabet[output_index]
            decrypted.append(output_letter)
        return "".join(decrypted) 