import sqlite3
conexao = sqlite3.connect('leagueofiuri.db')
cursor = conexao.cursor()   

cursor.execute('SELECT * FROM posicao')
 
resultados = cursor.fetchall()
 
for posicao in resultados:
    print(posicao)


conexao.commit()
conexao.close()