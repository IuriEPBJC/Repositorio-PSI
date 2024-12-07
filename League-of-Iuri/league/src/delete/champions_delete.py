import sqlite3
conexao = sqlite3.connect('leagueofiuri.db')
cursor = conexao.cursor()   

deleted_name = cursor.execute("DELETE FROM champions WHERE nome='Aatrox'" )
deleted_name = cursor.execute("DELETE FROM champions WHERE nome='Ahri'" )

resultados = cursor.fetchall()
 
for champions in resultados:
    print(champions)

print(deleted_name)
conexao.commit()
conexao.close()