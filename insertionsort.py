# coding: utf-8
import metrics

def insertionsort(lista):
	
	# Cria uma nova lista onde os itens serão inseridos de forma ordenada
	novaLista = []

	# Comprimento da lista dada como parâmetro
	comprimento = len(lista)

	# Percorre a lista
	for indice in range(comprimento):

		# Cria uma string de nome completo para usar na comparação
		nome = lista[indice]["first_name"] + " " + lista[indice]["last_name"]

		if len(novaLista) == 0:
			novaLista.insert(0, lista[indice])
			continue

		# Percorre os itens já inseridos na nova lista
		for indiceNL in range(len(novaLista)):

			# Cria uma string de nome completo do item da nova lista
			nomeAtual = novaLista[indiceNL]["first_name"] + " " + novaLista[indiceNL]["last_name"]

			# Encontra o primeiro elemento maior que o que está sendo inserido.
			if nomeAtual > nome:

				"""
				Insere o item na posição correta (empurrando os elementos à 
				partir de novaLista[indiceNL] para frente).
				"""
				novaLista.insert(indiceNL, lista[indice])

				# Adiciona movimentações para os deslocamentos dos elementos do vetor
				metrics.movimentacao( (len(lista) - indiceNL) )

				# Para de percorrer a nova lista
				break

			# Adiciona nas métricas a comparação feita.
			metrics.comparacao(1)

			"""
			Caso toda a nova lista tenha sido percorrida e não tenha sido
			encontrado um elemento na lista maior que o elemento atual...
			"""
			if indiceNL == len(novaLista)-1:
				# O elemento é adicionado no fim
				novaLista.append(lista[indice])
				metrics.movimentacao(1)


			# fim if
		# fim for indiceNL
	# fim for indice

	# Troca a lista pela nova lista, agora ordenada.
	return novaLista