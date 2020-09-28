# coding: utf-8

from csv import DictReader
from pathlib import Path, PureWindowsPath
from tabulate import tabulate

import time
import sys

import mergesort
import insertionsort
import selectionsort
import Quick_Sort2
import metrics

def main():
	# Aumenta o limite de recursão padrão
	sys.setrecursionlimit(10**6)

	# Flag que mantém o loop principal
	executando = True

	# Loop principal
	while executando:
		print("Digite o número do diretório:")
		print(" 1 |\t./1000/")
		print(" 2 |\t./2000/")
		print(" 3 |\t./3000/")
		print(" 4 |\t./5000/")
		print("   |")
		print(" 0 |\tSAIR DO PROGRAMA")
		folder = int(input())
		print()

		if folder == 0:
			print("FINALIZANDO EXECUÇÃO...")
			executando = False
			continue

		elif folder > 0 or folder < 5:
			print("Digite o numero do arquivo:")
			print(" 1 |\t./crescente.csv")
			print(" 2 |\t./decrescente.csv")
			print(" 3 |\t./random.csv")
			print("   |")
			print(" 0 |\tVOLTAR")
			file_index = int(input())
			print()

			if file_index == 0:
				continue
			elif file_index < 0 or file_index > 3:
				print("Opção inválida.")
			else:
				print("Digite a opção do algoritmo de ordenação")
				print(" 1 |\tInsertion Sort")
				print(" 2 |\tMerge Sort")
				print(" 3 |\tQuick Sort")
				print(" 4 |\tSelection Sort")
				print("   |")
				print(" 0 |\tMENU INICIAL")
				algo = int(input())
				print()

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
			tempo_total = 0

			if algo == 1:
				start_time = time.time()
				data = insertionsort.insertionsort(data)
				tempo_total = (time.time() - start_time)
			elif algo == 2:
				start_time = time.time()
				mergesort.mergesort(data, 0, len(data))
				tempo_total = (time.time() - start_time)
			elif algo == 3:
				start_time = time.time()
				Quick_Sort2.quicksort(data)
				tempo_total = (time.time() - start_time)

			else:
				start_time = time.time()
				selectionsort.selectionsort (data)
				tempo_total = (time.time() - start_time)

			header = data[0].keys()
			rows = [x.values() for x in data]
			print("\n##############################################################################################")
			print(tabulate(rows, header))
			print("##############################################################################################\n")
			print("Concluído em {} segundos, com {} comparações e {} movimentações.".format(tempo_total, metrics.comp, metrics.mov) )

		# Zera os valores das metricas
		metrics.resetmetrics()



# Executa a função main() diretamente caso o programa seja executado no terminal
if __name__ == "__main__":
	main()