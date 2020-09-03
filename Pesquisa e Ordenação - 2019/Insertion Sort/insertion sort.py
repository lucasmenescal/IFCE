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

def insertion_sort(lista):
    for i in range(1, len(lista)):
        val = lista[i]
        j = i - 1
    while (j >= 0) and (lista[j] > val):
        interaction += 1
        lista[j+1] = lista[j]
        j = j - 1
        lista[j+1] = val
    interaction += 1
    return lista

def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas", z='Tempo'):
    fig = plt.figure(figsize=(10, 8))
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
        y.append(timeit.timeit("insertion_sort({})".format(x[i]),setup="from __main__ import insertion_sort",number=1))

    desenhaGrafico(z,y)

    y = []
    for i in range(len(x)):
        y.append(timeit.timeit("insertion_sort({})".format(x[i]),setup="from __main__ import insertion_sort",number=1))

    desenhaGrafico(z,y)
