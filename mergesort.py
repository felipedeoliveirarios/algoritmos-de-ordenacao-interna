# coding: utf-8
import metrics

# Implementação recursiva do Merge Sort
def mergesort(lista, inicio, fim):

	# Condição de parada da recursão (sublista com apenas um elemento)
	if inicio < fim-1:
		meio = int( (inicio + fim) / 2 )

		mergesort(lista, inicio, meio)
		mergesort(lista, meio, fim)

		merge(lista, inicio, meio, fim)

# Realiza a fusão de duas sublistas de forma ordenada.
def merge(lista, inicio, meio, fim):

	# Cria listas de backup para as duas partes
	listaEsq = lista[inicio:meio]
	listaDir = lista[meio:fim]

	# Declara os índices das duas sublistas
	indiceEsq = 0
	indiceDir = 0

	# Declara o índice da lista principal
	indicePrinc = inicio

	# Gera as strings de nomes para a comparação
	nomeEsq = listaEsq[indiceEsq]["first_name"]
	nomeDir = listaDir[indiceDir]["first_name"]

	# flag que indica qual dos subvetores foi usado por último
	flagEsq = True


	# Enquanto nenhuma das sublistas tiver sido totalmente inserida...
	while indiceEsq < len(listaEsq) and indiceDir < len(listaDir):

		# Compara as strings contendo nome e sobrenome.
		# Caso o item da sublista esquerda seja maior (ou igual) que da direita
		if nomeEsq <= nomeDir:

			# Insere o item da sublista esquerda na posição correta
			lista[indicePrinc] = listaEsq[indiceEsq]

			# Itera o índice da lista esquerda.
			indiceEsq += 1

			# Caso ainda haja um próximo elemento na sublista esquerda
			if indiceEsq < len(listaEsq):
				# Cria a nova string de nome para a sublista esquerda, para a próxima comparação
				nomeEsq = listaEsq[indiceEsq]["first_name"]

		# Caso o item da sublista direita seja maior que da esquerda...
		else:

			# Insere o item da sublista direita
			lista[indicePrinc] = listaDir[indiceDir]

			# Itera o índice da segunda lista.
			indiceDir += 1

			# Caso ainda haja um próximo elemento na sublista direita
			if indiceDir < len(listaDir):
				# Cria a nova string de nome para a sublista direita, para a próxima comparação
				nomeDir = listaDir[indiceDir]["first_name"]

			# Notifica a movimentação para controle de desempenho.
			metrics.movimentacao(1)

		# Notifica a comparação entre elementos para controle de desempenho.
		metrics.comparacao(1)

		# Itera o índice da lista principal.
		indicePrinc += 1

	"""
	Caso uma das sublistas tenha sido exaurida, a outra será colocada
	diretamente dentro da lista extra.
	"""
	while indiceEsq < len(listaEsq):
		lista[indicePrinc] = listaEsq[indiceEsq]

		indiceEsq += 1
		indicePrinc += 1

	while indiceDir < len(listaDir):
		lista[indicePrinc] = listaDir[indiceDir]

		indiceDir += 1
		indicePrinc += 1
