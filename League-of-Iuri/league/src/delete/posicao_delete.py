import sqlite3
conexao = sqlite3.connect('leagueofiuri.db')
cursor = conexao.cursor()   


cursor.execute("DELETE FROM posicao WHERE role='mid'" )

resultados = cursor.fetchall()
 
for posicao in resultados:
    print(posicao)


conexao.commit()
conexao.close()