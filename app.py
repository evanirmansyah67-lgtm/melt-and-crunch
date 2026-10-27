
from flask import Flask, render_template

app = Flask(__name__)

produk = {
    "nama": "Tiramisu ",
    "harga": 12000,
    "deskripsi": "Tiramisu lembut dan manis.",
    "rasa": ["Tiramisu", "Cokelat"]
}

@app.route("/")
def beranda():
    return render_template("index.html", produk=produk)

if __name__ == "__main__":
    app.run(debug=True)
