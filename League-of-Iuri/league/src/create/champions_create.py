import sqlite3
conexao = sqlite3.connect('leagueofiuri.db')
cursor = conexao.cursor()   

cursor.execute('''
CREATE TABLE IF NOT EXISTS champions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    reino TEXT NOT NULL
)
''')

champions_data = [
    ("Aatrox", "Runeterra"),
    ("Ahri", "Ionia"),
    ("Akali", "Ionia"),
    ("Alistar", "Runeterra"),
    ("Amumu", "Shurima"),
    ("Anivia", "Freljord"),
    ("Annie", "Noxus"),
    ("Aphelios", "Targon"),
    ("Ashe", "Freljord"),
    ("Aurelion Sol", "Targon"),
    ("Azir", "Shurima"),
    ("Bard", "Runeterra"),
    ("Blitzcrank", "Zaun"),
    ("Brand", "Runeterra"),
    ("Braum", "Freljord"),
    ("Caitlyn", "Piltover"),
    ("Camille", "Piltover"),
    ("Cassiopeia", "Noxus"),
    ("Cho'Gath", "Void"),
    ("Corki", "Bandle City"),
    ("Darius", "Noxus"),
    ("Diana", "Targon"),
    ("Draven", "Noxus"),
    ("Dr. Mundo", "Zaun"),
    ("Ekko", "Zaun"),
    ("Elise", "Shadow Isles"),
    ("Evelynn", "Runeterra"),
    ("Ezreal", "Piltover"),
    ("Fiddlesticks", "Runeterra"),
    ("Fiora", "Demacia"),
    ("Fizz", "Bilgewater"),
    ("Galio", "Demacia"),
    ("Gangplank", "Bilgewater"),
    ("Garen", "Demacia"),
    ("Gnar", "Freljord"),
    ("Gragas", "Freljord"),
    ("Graves", "Bilgewater"),
    ("Gwen", "Shadow Isles"),
    ("Hecarim", "Shadow Isles"),
    ("Heimerdinger", "Piltover"),
    ("Illaoi", "Bilgewater"),
    ("Irelia", "Ionia"),
    ("Ivern", "Runeterra"),
    ("Janna", "Zaun"),
    ("Jarvan IV", "Demacia"),
    ("Jax", "Runeterra"),
    ("Jayce", "Piltover"),
    ("Jhin", "Ionia"),
    ("Jinx", "Zaun"),
    ("Kai'Sa", "Void")
]

cursor.executemany('INSERT INTO champions (nome, reino) VALUES (?, ?)', champions_data)

conexao.commit()

conexao.close()