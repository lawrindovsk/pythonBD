import mysql.connector
from mysql.connector import errorcode #Trata as exceções que pode aparecer.

def conectar():
    try:
        db_connection = mysql.connector.connect(host='localhost',
                                                 user='root',
                                                 password='',
                                                 database='bdgl')
        print('Conectado com sucesso!')
        return db_connection
    except mysql.connector.Error as erro: #Guardando as possíveis exceções na variáveis.
        if erro.errno == errorcode.ER_BAD_DB_ERROR: #Caso o banco de dados não exista , terá tratamento.
            print('Banco de Dados não existe!, {}'.format(erro))
        elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR: #Tratamento para acesso negado ao BD.
            print('Usuário ou senha invalidos!, {}'.format(erro))
        else:
            print(erro)
    else:
        db_connection.close()