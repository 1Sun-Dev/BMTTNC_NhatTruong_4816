class TranspositionCipher:
    def __init__(self):
        pass
    
    def encrypt(self, text, key):
        encyrpted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text): 
                encyrpted_text += text[pointer]
                pointer += key
        return encyrpted_text
    
    def decrypt(self, text, key):
        decrypted_text = [''] * key
        row, col = 0,0
        for sybol in text:
            decrypted_text[col] += sybol
            col += 1
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0
                row += 1
        return ''.join(decrypted_text)