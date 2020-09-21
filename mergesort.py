from main import notificar

# Função de início do Merge Sort sobre uma lista
def startMergesort(lista):
	mergesort(lista, 0, len(lista))

# Implementação recursiva do Merge Sort
def mergesort(lista, inicio, fim):

	# Condição de parada da recursão (sublista com apenas um elemento)
	if inicio < fim:
		meio = int( (inicio + fim) / 2 )

		mergesort(lista, inicio, meio)
		mergesort(lista, meio, fim)

		merge(lista, inicio, meio, fim)


# Realiza a fusão de duas sublistas de forma ordenada.
def merge(lista, inicio, meio, fim):

	# Garante que o valor da variável lista seja alterado fora da função.
	global lista

	# Cria uma lista onde serão inseridos os valores ordenados.
	listaExtra = lista

	# Declara os índices das duas sublistas e da lista extra.
	indice1 = inicio
	indice2 = meio
	indice3 = inicio

	# Enquanto nenhuma das sublistas tiver sido totalmente inserida...
	while indice1 < meio and indice2 < fim:
		
		# Concatena nome e sobrenome para usar na ordenação
		nome1 = lista[indice1].first_name + " " + lista[indice1].last_name
		nome2 = lista[indice2].first_name + " " + lista[indice2].last_name
		
		# Compara as strings contendo nome e sobrenome.
		# Caso o item da primeira lista seja maior ou igual que da segunda...
		if nome1 >= nome2:
			# Insere o item da primeira lista na lista extra.
			listaExtra[indice3] = lista[indice1]
			# Itera o índice da primeira lista.
			indice1 += 1
			# Notifica a movimentação para controle de desempenho.
			notificar("mov")
		
		# Caso o item da segunda lista seja maior que o da primeira...
		else:
			# Insere o item da segunda lista na lista extra.
			listaExtra[indice3] = lista[indice2]
			# Itera o índice da segunda lista.
			indice2 += 1
			# Notifica a movimentação para controle de desempenho.
			notificar("mov")

		# Notifica a comparação entre elementos para controle de desempenho.
		notificar("comp")
		# Itera o índice da lista extra.
		indice3 += 1

	# Caso uma das listas tenha sido exaurida, a outra será colocada diretamente dentro da lista extra.
	while indice1 < meio:
		listaExtra[indice3] = lista[indice1]
		indice1 += 1
		indice3 += 3

	while indice2 < fim:
		listaExtra[indice3] = lista[indice2]
		indice2 += 1
		indice3 += 3

	# Por fim, a lista inicial assume os valores da lista extra.
	lista = listaExtra
