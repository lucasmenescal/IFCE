from random import randint
import timeit
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
def geralista(tam):
    lista =[]
    lista = random.sample(range(0,tam),tam)
    return lista  

def merge_sort(lista):
    if len(lista)>1:
        meio = len(lista)//2
        metadeesquerda = lista[:meio]
        metadedireita = lista[meio:]

        merge_sort(metadeesquerda)
        merge_sort(metadedireita)

        i=0
        j=0
        k=0
        while i < len(metadeesquerda) and j < len(metadedireita):
            if metadeesquerda[i] <= metadedireita[j]:
                lista[k]=metadeesquerda[i]
                i=i+1
            else:
                lista[k]=metadedireita[j]
                j=j+1
            k=k+1

        while i < len(metadeesquerda):
            lista[k]=metadeesquerda[i]
            i=i+1
            k=k+1

        while j < len(metadedireita):
            lista[k]=metadedireita[j]
            j=j+1
            k=k+1
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
    
    z = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
    lista = []
    newlista = []
    x = []
    for i in range(len(z)):
        x.append(geralista(z[i]))
    y = []
    for i in range(len(x)):
        y.append(timeit.timeit("merge_sort({})".format(x[i]), setup="from __main__ import merge_sort", number=1))

    desenhaGrafico(z,y)
    
    
