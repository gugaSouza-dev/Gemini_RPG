from main import clear
from mensagens import criar_personagem_mensagem
from server_connections import delete, get, post_personagem

class Personagem:
	def __init__(self, id, nome, genero, classe, raca):
		self._id = id
		self._nome = nome
		self._genero = genero
		self._classe = classe
		self._raca = raca

		@property
		def id(self):
			return self.id
		@id.setter
		def nome(self, value):
			self._id = value

		@property
		def nome(self):
			return self.nome
		@nome.setter
		def nome(self, value):
			self._nome = value

		@property
		def genero(self):
			return self.genero
		@genero.setter
		def nome(self, value):
			self._genero = value

		@property
		def classe(self):
			return self.classe
		@classe.setter
		def classe(self, value):
			self._classe = value

		@property
		def raca(self):
			return self.raca
		@raca.setter
		def raca(self, value):
			self._raca = value

	def __str__(self):
		print(f'\tNome: {self._nome}\n\tGenero: {self._genero}\n\tClasse: {self._classe}\n\tRaca: {self._raca}\n') 
		

def criar_nome():
	clear()
	criar_personagem_mensagem()
	nome = input('Nome: ')
	if not nome:
		nome = "Ninguem"
	clear()
	criar_personagem_mensagem()
	return nome

def criar_genero():
	genero_opcao = input('\nGeneros: \n [1] Masculino\n [2] Feminino\n [3] Anjo\n')
	match genero_opcao:
		case '1':
			genero = 'Masculino'
		case '2':
			genero = 'Feminino'
		case _:
			genero = 'Anjo'
	clear()
	criar_personagem_mensagem()
	return genero

def criar_classe():
	classe_opcao = input('Classes: \n [1] Guerreiro\n [2] Arqueiro\n [3] Mago\n')
	match classe_opcao:
		case '1':
			classe = 'Guerreiro'
		case '2':
			classe = 'Arqueiro'
		case '3':
			classe = 'Mago'
		case _:
			classe = 'Deprived'
	clear()
	criar_personagem_mensagem()
	return classe

def criar_raca():
	raca_opcao = input('Raca : \n [1] Nordico\n [2] Elfo\n [3] Khajiit\n')
	match raca_opcao:
		case '1':
			raca = 'Nordico'
		case '2':
			raca = 'Elfo'
		case '3':
			raca = 'Khajiit'
		case _:
			raca = 'Mestico'
	clear()
	return raca

def criar_personagem():
	nome = criar_nome()
	print(f'Nome: {nome}')
	genero = criar_genero()
	print(f'Nome: {nome}\nGenero: {genero}\n')
	classe = criar_classe()
	print(f'Nome: {nome}\nGenero: {genero}\nClasse: {classe}\n')
	raca = criar_raca()
	print(f'Nome: {nome}\nGenero: {genero}\nClasse: {classe}\nRaca: {raca}\n')
	personagem = Personagem("", nome.capitalize(), genero, classe, raca)
	post_personagem(personagem)
	return personagem

def menu_selecionar_personagens(personagem, personagem_index, quantidade_personagens):
	opcao = input("[0] Sair\n[ENTER] Selecionar\n[1] Proximo\n[2] Voltar\n[3] Deletar\n")
	match opcao:
		case "0":
			return -1
		case "": #Enter
			return -2 #Personagem selecionado
		case "1":
			if personagem_index + 1 > quantidade_personagens:
				return personagem_index
			else:
				personagem_index += 1
		case "2":
			if personagem_index <= 1:
				personagem_index == 1
			else:
				personagem_index -= 1
		case "3":
			deletar_personagem(personagem._id)
			return -1
		case _:
			print("Opcao invalida")
			return -1
	return personagem_index

def selecionar_personagens():
	clear()
	personagens = get("tb_personagens")
	quantidade_personagens = len(personagens)
	personagem_index = 1
	while personagens[personagem_index - 1]:
		row = format_row(personagens[personagem_index - 1])
		personagem = Personagem(row[0], row[1], row[2], row[3], row[4])
		print(f"Personagens[{personagem_index}/{len(personagens)}]:")
		personagem.__str__()
		user_input = menu_selecionar_personagens(personagem, personagem_index, quantidade_personagens)
		if user_input == -1:
			clear()
			break
		if user_input == -2:
			return personagem
		if not user_input:
			return
		personagem_index = user_input
		clear()
	return

def deletar_personagem(id):
	delete("tb_personagens", id)

def format_row(row):
	row = str(row).split(",")
	formated_row = []
	for string in row:
		formated_row.append(string.lstrip("(").strip("\"").lstrip("b").strip(" ").rstrip(")").strip("\'"))
	return formated_row