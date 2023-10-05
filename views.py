from flask import render_template, request, redirect, session
from __init__ import app
import model

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('password1')
        confirm = request.form.get('password2')

        if senha != confirm:
            return render_template('cadastro.html', erro='As senhas não correspondem')
        else:
            model.cadastrar_usuario(nome, email, senha)
            return redirect('/login')

    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg_erro = ''
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')

        usuario = model.buscar_usuario(email, senha)

        if usuario:
            session['usuario_id'] = usuario[0]
            return redirect('/area_logada')
        else:
            msg_erro = 'Usuário e/ou senha inválidos'
            return render_template('login.html', erro=msg_erro)

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/area_logada')
def area_logada():
    return render_template('area_logada.html')
    

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
