Cadastro de Usuários com Flask e MySQL

Este projeto é uma API simples de cadastro de usuários utilizando Flask e MySQL. Ele recebe dados de um formulário HTML, armazena no banco de dados e protege as senhas com criptografia usando bcrypt.

🚀 Tecnologias Utilizadas

Python (Flask)

MySQL

Bcrypt (para criptografia de senhas)

HTML e CSS (para interface do formulário)

📌 Como Instalar e Rodar o Projeto

1. Clonar o repositório

  git clone https://github.com/seu-usuario/seu-repositorio.git
  cd seu-repositorio

2. Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)

# No Windows
python -m venv venv
venv\Scripts\activate

# No Linux/Mac
python3 -m venv venv
source venv/bin/activate

3. Instalar as Dependências

pip install -r requirements.txt

4. Configurar o Banco de Dados

Certifique-se de ter um banco de dados MySQL rodando e crie a base de dados:

CREATE DATABASE login_database;
USE login_database;
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

5. Rodar o Servidor Flask

python app.py

O servidor estará rodando em http://127.0.0.1:5000

🔥 Como Testar

Via Formulário HTML

Abra o arquivo cadastro.html no navegador e preencha os campos para testar o cadastro.

Via Postman ou cURL

Envie uma requisição POST para http://127.0.0.1:5000/cadastrar com os seguintes parâmetros:

{
    "email": "exemplo@email.com",
    "senha": "minhaSenhaSegura"
}

📜 Licença

Este projeto é de código aberto. Sinta-se à vontade para contribuir!

