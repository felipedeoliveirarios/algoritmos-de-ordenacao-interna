from main import notificar

def startInsertionsort(lista):
	insertionsort(lista)


def insertionsort(lista):

	# Cria uma nova lista onde os itens serão inseridos de forma ordenada
	novaLista = []

	# Comprimento da lista dada como parâmetro
	comprimento = len(lista)

	# Percorre a lista
	for indice in comprimento:

		# Cria uma string de nome completo para usar na comparação
		nome = lista[indice].first_name + " " + lista[indice].last_name

		if len(novaLista) == 0:
			novaLista[0] = lista[indice]
			break

		# Percorre os itens já inseridos na nova lista
		for indiceNL in len(novaLista):

			# Cria uma string de nome completo do item da nova lista
			nomeAtual = novaLista[indiceNL].first_name + " " + novaLista[indiceNL].last_name

			# Adiciona nas métricas a comparação feita.
			notificar("comp", 1)

			# Encontra o primeiro elemento maior que o que está sendo inserido.
			if nomeAtual > nome:

				"""
				Insere o item na posição correta (empurrando os elementos à 
				partir de novaLista[indiceNL] para frente).
				"""
				novaLista.insert(indiceNL, lista[indice])
				# Para de percorrer a nova lista
				break

			"""
			Caso toda a nova lista tenha sido percorrida e não tenha sido
			encontrado um elemento na lista maior que o elemento atual...
			"""
			if indiceNL == len(novaLista)-1:
				# O elemento é adicionado no fim
				novaLista.append(indiceNL, lista[indice])


			# fim if
		# fim for indiceNL
	# fim for indice

	# Troca a lista pela nova lista, agora ordenada.
	lista = novaLista