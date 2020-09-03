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

def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
          if lista[i] > lista[i+1]:
               lista[i], lista[i+1] = lista[i+1],lista[i]
               ordenado = False        
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
        y.append(timeit.timeit("bubble_sort({})".format(x[i]),setup="from __main__ import bubble_sort",number=1))
    desenhaGrafico(z,y)

    y = []

    for i in range(len(x)):

        y.append(bubble_sort(x[i]))



    desenhaGrafico(z,y, z='Qtd de swaps')
