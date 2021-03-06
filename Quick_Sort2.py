# coding: utf-8
import metrics

def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
    if len(lista) == 1:
        return lista
    if inicio < fim:
        pi = partition(lista, inicio, fim)
        quicksort(lista, inicio, pi - 1)
        quicksort(lista, pi + 1, fim)

def partition(lista, inicio, fim):
    i = (inicio - 1)
    pivot = lista[fim]
    nome_pivo = lista[fim]["first_name"]

    for j in range(inicio, fim):
        auxiliar = lista[j]["first_name"]

        metrics.comparacao(1)
        if auxiliar <= nome_pivo:
            i = i + 1
            metrics.movimentacao(1)
            lista[i], lista[j] = lista[j], lista[i]

    metrics.movimentacao(1)
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return (i + 1)