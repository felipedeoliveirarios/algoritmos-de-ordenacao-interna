import metrics

def selectionsort(array):
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):

            nome1 = array[min_index]["first_name"]
            nome2 = array[right]["first_name"]
            if nome2 < nome1:
                min_index = right
            metrics.comparacao(1)

        if index != min_index:
            metrics.movimentacao(1)
            array[index], array[min_index] = array[min_index], array[index]