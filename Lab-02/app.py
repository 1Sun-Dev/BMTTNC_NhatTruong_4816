from flask import Flask, render_template, request, flash, redirect, url_for
from cipher.caesar import CaesarCipher

app = Flask(__name__)
app.secret_key = "giatri_bi_mat_de_dung_flash" # Bắt buộc phải có secret_key

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlaintext']
    key = int(request.form['inputKeyPlain'])
    
    caesar_tool = CaesarCipher()
    encrypted_text = caesar_tool.encrypt_text(text, key)
    
    # Gửi thông tin qua flash message
    flash(f"Mã hóa thành công!", "success")
    flash(encrypted_text, "result") # Dùng category riêng cho kết quả
    return redirect(url_for('caesar'))

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCiphertext']
    key = int(request.form['inputKeyCipher'])
    
    caesar_tool = CaesarCipher()
    decrypted_text = caesar_tool.decrypt_text(text, key)
    
    flash(f"Giải mã thành công!", "info")
    flash(decrypted_text, "result")
    return redirect(url_for('caesar'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)