import sqlite3
conexao = sqlite3.connect('leagueofiuri.db')
cursor = conexao.cursor()   

cursor.execute('SELECT * FROM build')
 
resultados = cursor.fetchall()
 
for build in resultados:
    print(build)


conexao.commit()
conexao.close()