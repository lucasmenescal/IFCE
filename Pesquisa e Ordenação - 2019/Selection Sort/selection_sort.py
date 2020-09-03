from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def selection_sort(lista):
    for i in range(len(lista) - 1):
        minIndx = i
        minVal= lista[i]
        j = i + 1
        while j < len(lista):
            if minVal > lista[j]:
                minIndx = j
                minVal= lista[j]
            j += 1
        temp = lista[i]
        lista[i] = lista[minIndx]
        lista[minIndx] = temp       
    return lista

def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas", z='Tempo'):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = z)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig('teste.png', format='png')
    plt.show()

if __name__ == '__main__':
    z = [10000,20000,50000,100000]
    x = []
    for i in z:
        x.append(geraLista(i))
    y =[]
    for i in range(len(x)):
        y.append(timeit.timeit("selection_sort({})".format(x[i]),setup="from __main__ import selection_sort",number=1))
    desenhaGrafico(z,y)
    y = []
    for i in range(len(x)):
            y.append(selection_sort(x[i]))
desenhaGrafico(z,y, z='Qtd de swaps')
