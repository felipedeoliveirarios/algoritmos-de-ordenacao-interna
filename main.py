from mergesort.py import mergesort

def notificar(string)
	if string == "comp":
		global comparações
		comparações += 1

	if string == "mov":
		global movimentações
		movimentações += 1


def main():
	comparações = 0
	modificações = 0
	"""
	Oferece a escolha de arquivo
	Oferece a escolha do algoritmo
	Usa o algoritmo de ordenação
	Exibe a lista de dados ordenados
	Pergunta se quer sair ou inserir outro arquivo
	"""

# Executa a função main() diretamente caso o programa seja executado no terminal
if __name__ == "__main__":
	main()