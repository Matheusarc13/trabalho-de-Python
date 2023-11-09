# Importando a biblioteca sqlite3 para lidar com o banco de dados SQLite
import sqlite3

# Função para conectar ao banco de dados ou criar um novo se não existir
def connect():
    conn = sqlite3.connect("tarefas.db")
    cur = conn.cursor()
    # Criando a tabela 'tarefas' se ela ainda não existir
    cur.execute("CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY, titulo text, data integer)")
    conn.commit()
    conn.close()

# Função para inserir uma nova tarefa no banco de dados
def insert(titulo, data):
    conn = sqlite3.connect("tarefas.db")
    cur = conn.cursor()
    # Inserindo dados na tabela 'tarefas'
    cur.execute("INSERT INTO tarefas VALUES (NULL,?,?)", (titulo, data))
    conn.commit()
    conn.close()
    # Atualizando a visualização após a inserção
    view()

# Função para obter todas as tarefas do banco de dados
def view():
    conn = sqlite3.connect("tarefas.db")
    cur = conn.cursor()
    # Selecionando todas as linhas da tabela 'tarefas'
    cur.execute("SELECT * FROM tarefas")
    rows = cur.fetchall()
    conn.close()
    return rows

# Função para buscar tarefas com base no título ou data
def search(titulo="", data=""):
    conn = sqlite3.connect("tarefas.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tarefas WHERE titulo=? OR data=?", (titulo, data))
    rows = cur.fetchall()
    conn.close()
    return rows

# Função para excluir uma tarefa com base no ID
def delete(id):
    conn = sqlite3.connect("tarefas.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM tarefas WHERE id=?", (id,))
    conn.commit()
    conn.close()

# Função para atualizar uma tarefa com base no ID
def update(id, titulo, data):
    conn = sqlite3.connect("tarefas.db")
    cur = conn.cursor()
    cur.execute("UPDATE tarefas SET titulo=?, data=? WHERE id=?", (titulo, data, id))
    conn.commit()
    conn.close()

# Chamando a função connect() para garantir que o banco de dados esteja criado ou conectado
connect()
