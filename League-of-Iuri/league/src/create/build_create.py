import sqlite3
conexao = sqlite3.connect('leagueofiuri.db')
cursor = conexao.cursor()   
cursor.execute('DROP TABLE IF EXISTS build')

# Criar a tabela build
cursor.execute('''
CREATE TABLE IF NOT EXISTS build (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    build TEXT NOT NULL,
    champ INTEGER NOT NULL,
    roles INTEGER NOT NULL,
    FOREIGN KEY(champ) REFERENCES champions (id),
    FOREIGN KEY(roles) REFERENCES roles (id)
)
''')

# Preencher a tabela build com 20 registros
build_data = [
    ("attack speed", 1, 1), 
    ("lethality", 2, 2),    
    ("tank", 3, 3),         
    ("attack speed", 4, 4), 
    ("tank", 5, 5),         
    ("lethality", 6, 1),    
    ("attack speed", 7, 2), 
    ("tank", 8, 3),         
    ("attack speed", 9, 4), 
    ("lethality", 10, 5),   
    ("tank", 11, 1),        
    ("attack speed", 12, 2),
    ("lethality", 13, 3),   
    ("tank", 14, 4),        
    ("attack speed", 15, 5),
    ("lethality", 16, 1),   
    ("tank", 17, 2),        
    ("attack speed", 18, 3),
    ("lethality", 19, 4),   
    ("tank", 20, 5),        
]

cursor.executemany('INSERT INTO build (build, champ, roles) VALUES (?, ?, ?)', build_data)

conexao.commit()

conexao.close()