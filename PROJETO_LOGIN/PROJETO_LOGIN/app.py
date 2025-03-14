import mysql.connector
from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    email = request.form.get("email")
    senha = request.form.get("senha")

    if not email or not senha:
        return jsonify({"erro": "Campos obrigatórios não preenchidos"}), 400

    # Criptografar a senha antes de armazenar
    senha_hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="login_database"
        )
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO usuarios (email, senha) VALUES (%s, %s)", (email, senha_hash))
        conexao.commit()

        cursor.close()
        conexao.close()

        return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
