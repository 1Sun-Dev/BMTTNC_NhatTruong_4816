from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()


@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data ['plain_text']
    key = int(data['key'])
    encrypted = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message' : encrypted})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data ['cipher_text']
    key = int(data['key'])
    decrypted = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'encrypted_message' : decrypted})

#main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)