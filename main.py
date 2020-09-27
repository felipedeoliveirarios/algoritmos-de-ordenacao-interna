import csv
from csv import DictReader
from mergesort import startMergesort
from insertionsort import startInsertionsort
from quicksort import quicksort
import tabulate

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
			file_index = input()

			if file_index == 0:
				continue
			elif file_index < 0 or file_index > 3:
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

		if file_index == 1:
			file_name += "crescente.csv"
		elif file_index == 2:
			file_name += "decrescente.csv"
		else:
			file_name += "random.csv"

		with open(Path(file_name)) as file:
			data = DictReader(file)

			if algo == 1:
				startInsertionsort(data)
			elif algo == 2:
				startMergesort(data)
			elif algo == 3:
				quicksort(data)
			else:
				# selectionsort(data)

			header = data[0].keys()
			rows = [x.values() for x in data]
			print(tabulate.tabulate(rows, header))



# Executa a função main() diretamente caso o programa seja executado no terminal
if __name__ == "__main__":
	main()