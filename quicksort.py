# coding: utf-8
import main

def quicksort(lista, inicio = 0, fim = None):
    if(fim is None):
        fim = len(lista) - 1
    if(inicio < fim):
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p - 1)
        quicksort(lista, p + 1, fim)

def partition(lista, inicio, fim):
    pivo = lista[fim]
    nome_pivo = lista[fim]["first_name"] + " " + lista[fim]["last_name"]

    i = inicio
    for j in range(inicio, fim):

        auxiliar = lista[j]["first_name"] + " " + lista[j]["last_name"]

        main.notificar("comp", 1)

        if auxiliar <= nome_pivo:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
            main.notificar("mov", 1)
    # Coloca o Pivô no lugar
    lista[i], lista[fim] = lista[fim], lista[inicio]
    return i
