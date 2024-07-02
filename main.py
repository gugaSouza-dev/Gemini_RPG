import os
from menu import *
from mensagens import welcome_message, mischief_mensagem
from server import connect_to_sql

CONNECTION = connect_to_sql()

def main():
	clear()
	welcome_message()
	while True:
		if (menu() == False):
			break
	mischief_mensagem()
	CONNECTION.close()
	

def clear():
	os.system('cls')

if __name__ == "__main__":
	main()