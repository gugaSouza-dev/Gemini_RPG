from server import close_cursor
from main import CONNECTION
import uuid

def delete(table, id):
	try:
		connection = CONNECTION
		cursor = connection.cursor()
		cursor.execute(f'''
			DELETE FROM {table}
			WHERE id = ?
		''', (id,))  # Pass as a tuple
		if input("[0] Cancelar\n[1] Confirmar\n") == "1":
			connection.commit()
			print("Deletado com sucesso!")
	except:
		print("Erro ao deletar")
	finally:
		close_cursor(cursor)

def get(table):
	try:
		connection = CONNECTION
		cursor = connection.cursor()
		cursor.execute(f"SELECT * FROM {table}")
		return cursor.fetchall()
	except:
		print("Erro ao listar")
	finally:
		close_cursor(cursor)
		
def post_personagem(personagem):
	try:
		connection = CONNECTION
		cursor = connection.cursor()
		id = str(uuid.uuid4())
		cursor.execute('''
			INSERT INTO tb_personagens (id, nome, genero, classe, raca)
			VALUES (?, ?, ?, ?, ?)
		''', (id, personagem._nome, personagem._genero, personagem._classe, personagem._raca))
		if input("[0] Cancelar\n[1] Confirmar\n") == "1":
			connection.commit()
	except:
		print("Erro ao criar personagem")
	finally:
		close_cursor(cursor)