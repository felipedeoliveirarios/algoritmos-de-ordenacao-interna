import csv
import mergesort
import insertionsort
import quicksort

métricas = []

def notificar(indice, valor):
	if indice == "comp":
		global métricas
		métricas["comp"] += valor

	if indice == "mov":
		global métricas
		métricas["mov"] += valor


def main():
	# Permite alterar as métricas diretamente
	global métricas

	# Flag que mantém o loop principal
	executando = True

	# Loop principal
	while executando:

		# Zera os valores das métricas
		métricas["comp"] = 0
		métricas["mov"] = 0

		"""
		Oferece a escolha de arquivo
		Lê o arquivo como lista de dicts (https://thispointer.com/python-read-csv-into-a-list-of-lists-or-tuples-or-dictionaries-import-csv-to-list/)
		Oferece a escolha do algoritmo
		Usa o algoritmo de ordenação
		Exibe a lista de dados ordenados
		Pergunta se quer sair ou inserir outro arquivo
		"""

# Executa a função main() diretamente caso o programa seja executado no terminal
if __name__ == "__main__":
	main()