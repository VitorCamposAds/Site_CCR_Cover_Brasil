from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
import logging
from logging import StreamHandler

app = Flask(__name__)

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'vitorcamposmouracosta@gmail.com'  # Seu e-mail
app.config['MAIL_PASSWORD'] = 'vndqzacowyovoifw'  # Sua senha
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'vitorcamposmouracosta@gmail.com'  # Defina um remetente padrão
mail = Mail(app)

# Configuração de logging
handler = StreamHandler()
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

@app.route('/')
def index():
    return render_template('index.html')  # Certifique-se de que index.html está na pasta templates

@app.route('/enviar-email', methods=['POST'])
def enviar_email():
    print("Função enviar_email chamada")  # Para verificar se a função é chamada

    # Recebe os dados do formulário
    nome = request.form['name']
    email = request.form['email']
    telefone = request.form['phone']
    mensagem = request.form['message']
    
    # Imprime os dados recebidos para depuração
    print(f"Nome: {nome}, Email: {email}, Telefone: {telefone}, Mensagem: {mensagem}")

    # Cria a mensagem
    msg = Message(f'Mensagem de {nome}', recipients=['vitorbeatle@gmail.com'])
    msg.body = f'Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nMensagem: {mensagem}\n\nEmail enviado do site CCR_Cover_Brasil.'
    
    # Envia o e-mail
    try:
        mail.send(msg)
        print('E-mail enviado com sucesso!')  # Mensagem de sucesso
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')  # Mensagem de erro
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)