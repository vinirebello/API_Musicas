import mysql.connector

class Database:
    
    
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="musicas"
    )
       
        
    status = print('Estado da conexão Banco de Dados: ' + str (connection.is_connected()))
        
        