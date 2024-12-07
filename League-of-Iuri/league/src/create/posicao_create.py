import sqlite3
conexao = sqlite3.connect('leagueofiuri.db')
cursor = conexao.cursor()   
cursor.execute('DROP TABLE IF EXISTS posicao')


cursor.execute('''
CREATE TABLE IF NOT EXISTS posicao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roles TEXT NOT NULL,
    champ INTEGER NOT NULL,
    FOREIGN KEY (champ) REFERENCES champions (id)
)
''')

posicao_data = [
    ("mid", 1), 
    ("top", 2), 
    ("jungle", 3), 
    ("adc", 4),  
    ("support", 5), 
    ("mid", 6),  
    ("top", 7),  
    ("jungle", 8), 
    ("adc", 9),  
    ("support", 10),  
    ("mid", 11),  
    ("top", 12),  
    ("jungle", 13),  
    ("adc", 14),  
    ("support", 15),  
    ("mid", 16),  
    ("top", 17),  
    ("jungle", 18),  
    ("adc", 19),  
    ("support", 20),  
]

# Inserir dados na tabela posicao
cursor.executemany('INSERT INTO posicao (roles, champ) VALUES (?, ?)', posicao_data)


conexao.commit()

conexao.close()