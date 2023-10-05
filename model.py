import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='<your password>',
    database='<your database>'
)

def cadastrar_usuario(nome, email, senha):
    cursor = db.cursor()
    comando = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
    values = (nome, email, senha)
    cursor.execute(comando, values)
    db.commit()
    cursor.close()

def buscar_usuario(email, senha):
    cursor = db.cursor()
    sql = "SELECT * FROM usuario WHERE email = %s AND senha = %s"
    values = (email, senha)
    cursor.execute(sql, values)
    usuario = cursor.fetchone()
    cursor.close()
    return usuario

def buscar_nome(nome):
    cursor = db.cursor()
    msql = "SELECT * FROM usuario WHERE nome = %s"
    values = (nome)
    cursor.execute(msql, values)
    resultado = cursor.fetchone()
    cursor.close()
    
    if resultado:      
        return resultado[0]  # Retorna o primeiro campo da consulta (nome do usuário)

    return None # Retorna None se o usuário não for encontrado
