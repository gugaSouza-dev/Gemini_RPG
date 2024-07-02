from personagem import criar_personagem, selecionar_personagens
from main import clear
from aventura import aventura

def show_menu():
	return (input('Menu: \n[1] Criar personagem \n[2] Selecionar personagens \n[0] Sair\n'))

def menu():
	opcao = show_menu()
	match opcao:
		case '1':
			personagem = criar_personagem()
			clear()
			personagem.__str__()
		case '2':
			personagem = selecionar_personagens()
			if not personagem:
				return False
			aventura(personagem)
		case '0':
			return False
		case _:
			print('Opcao inválida!')
	return True



