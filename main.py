# coding: utf-8
from csv import DictReader
import mergesort
import insertionsort
import selectionsort
import quicksort
from pathlib import Path, PureWindowsPath
from tabulate import tabulate

global metricas
metricas = {'comp':0, 'mov':0}

def notificar(indice, valor):
	global metricas
	if indice == "comp":
		metricas["comp"] += valor

	if indice == "mov":
		metricas["mov"] += valor


def main():
	# Permite alterar as metricas diretamente
	global metricas

	# Flag que mantém o loop principal
	executando = True

	# Loop principal
	while executando:

		# Zera os valores das metricas
		metricas["comp"] = 0
		metricas["mov"] = 0

		print("Digite o número do diretório:")
		print("1. 1000")
		print("2. 2000")
		print("3. 3000")
		print("4. 5000")
		print("0. SAIR DO PROGRAMA")
		folder = int(input())

		if folder == 0:
			print("Saindo do programa...")
			executando = False
			continue

		elif folder > 0 or folder < 5:
			print("Digite o numero do arquivo:")
			print("1. crescente.csv")
			print("2. decrescente.csv")
			print("3. random.csv")
			print("0. Voltar ao menu anterior")
			file_index = int(input())

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
				algo = int(input())

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
			data = list(DictReader(file))

			if algo == 1:
				insertionsort.startInsertionsort(data)
			elif algo == 2:
				mergesort.startMergesort(data)
			elif algo == 3:
				quicksort.quicksort(data)
			else:
				selectionsort.selectionsort (data)
				pass

			header = data[0].keys()
			rows = [x.values() for x in data]
			print(tabulate(rows, header))



# Executa a função main() diretamente caso o programa seja executado no terminal
if __name__ == "__main__":
	main()