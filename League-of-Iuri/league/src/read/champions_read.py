import sqlite3
conexao = sqlite3.connect('leagueofiuri.db')
cursor = conexao.cursor()   

cursor.execute('SELECT * FROM champions')
 
resultados = cursor.fetchall()
 
for champions in resultados:
    print(champions)


conexao.commit()
conexao.close()