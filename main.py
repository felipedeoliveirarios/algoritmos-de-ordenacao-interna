import csv
import mergesort
import insertionsort
import quicksort
import csv

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

		print("Digite o número do diretório:")
		print("1. 1000")
		print("2. 2000")
		print("3. 3000")
		print("4. 5000")
		print("0. SAIR DO PROGRAMA")
		folder = input()

		if folder == 0:
			print("Saindo do programa")

		elif folder > 0 or folder < 5:
			print("Digite o numero do arquivo:")
			print("1. crescente.csv")
			print("2. decrescente.csv")
			print("3. random.csv")
			print("0. Voltar ao menu anterior")
			file = input()

			if file == 0:
				continue
			elif file < 0 or file > 3:
				print("Opção inválida.")
			else:
				print("Digite a opção do algoritmo de ordenação")
				print("1. Insertion Sort")
				print("2. Merge Sort")
				print("3. Quick Sort")
				print("4. Selection Sort")
				print("0. Voltar ao menu inicial")
				algo = input()

				if algo == 0:
					continue
				elif algo < 0 or algo > 4:
					print("Opção inválida")
					continue
		else:
			print("Opção inválida.")

	file_name = "datasets_prontos/"

	if folder == 1:
		file_name += "1000/"
	elif folder == 2:
		file_name += "2000/"
	elif folder == 3:
		file_name += "3000/"
	else:
		file_name += "4000/"

	if file == 1:
		file_name += "crescente.csv"
	elif file == 2:
		file_name += "decrescente.csv"
	else:
		file_name += "random.csv"


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